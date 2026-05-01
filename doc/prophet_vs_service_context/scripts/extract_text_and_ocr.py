#!/usr/bin/env python3
"""Extract native PDF text where possible, otherwise OCR local page images."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SOURCE_PDFS = [
    "doc/sci_prophet_vs_ecr738.pdf",
    "doc/sci_prophet_vs_ecr739.pdf",
    "doc/pvs_service.pdf",
    "doc/5508.pdf",
    "doc/5530.pdf",
]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def context_root() -> Path:
    return Path(__file__).resolve().parents[1]


def rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(repo_root()).as_posix()
    except ValueError:
        return path.as_posix()


def normalized_text_score(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9+/_\-.]{1,}", text))


def native_text_with_fitz(pdf_path: Path) -> dict[int, str] | None:
    try:
        import fitz  # type: ignore
    except Exception:
        return None

    doc = fitz.open(pdf_path)
    return {idx: page.get_text("text") or "" for idx, page in enumerate(doc, start=1)}


def native_text_with_pypdf(pdf_path: Path) -> dict[int, str] | None:
    try:
        from pypdf import PdfReader  # type: ignore
    except Exception:
        try:
            from PyPDF2 import PdfReader  # type: ignore
        except Exception:
            return None

    reader = PdfReader(str(pdf_path))
    texts: dict[int, str] = {}
    for idx, page in enumerate(reader.pages, start=1):
        try:
            texts[idx] = page.extract_text() or ""
        except Exception:
            texts[idx] = ""
    return texts


def load_manifest(pdf_stem: str) -> dict[str, Any] | None:
    manifest_path = context_root() / "page_images" / pdf_stem / "manifest.json"
    if not manifest_path.exists():
        return None
    return json.loads(manifest_path.read_text(encoding="utf-8"))


def ocr_image(image_path: Path) -> tuple[str, str]:
    tesseract = shutil.which("tesseract")
    if not tesseract:
        return (
            "",
            "OCR locale non disponibile: `tesseract` non trovato. "
            f"Immagine pagina: {rel(image_path)}",
        )

    cmd = [tesseract, str(image_path), "stdout", "-l", "eng", "--psm", "11"]
    try:
        proc = subprocess.run(
            cmd,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=180,
        )
    except subprocess.TimeoutExpired:
        return "", f"OCR timeout su immagine: {rel(image_path)}"

    if proc.returncode != 0:
        return "", f"OCR fallito su {rel(image_path)}: {proc.stderr.strip()}"
    return proc.stdout.strip(), ""


def confidence_for(method: str, text: str) -> str:
    if method == "native_text":
        return "high" if normalized_text_score(text) >= 25 else "medium"
    if method == "ocr":
        score = normalized_text_score(text)
        if score >= 80:
            return "medium"
        if score >= 15:
            return "low"
    return "unavailable"


def write_page_text(
    out_path: Path,
    source_pdf: str,
    page_num: int,
    method: str,
    confidence: str,
    content: str,
) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    body = (
        f"SOURCE: {source_pdf}\n"
        f"PAGE: {page_num}\n"
        f"METHOD: {method}\n"
        f"CONFIDENCE: {confidence}\n\n"
        "CONTENT:\n"
        f"{content.rstrip()}\n"
    )
    out_path.write_text(body, encoding="utf-8")


def process_pdf(source: str) -> dict[str, Any]:
    pdf_path = repo_root() / source
    native_pages = native_text_with_fitz(pdf_path) or native_text_with_pypdf(pdf_path) or {}
    manifest = load_manifest(pdf_path.stem)
    page_count = manifest["page_count"] if manifest else len(native_pages)
    tesseract_available = shutil.which("tesseract") is not None

    out_dir = context_root() / "extracted_text" / pdf_path.stem
    pages: list[dict[str, Any]] = []
    for page_num in range(1, page_count + 1):
        native_text = native_pages.get(page_num, "")
        if normalized_text_score(native_text) >= 20:
            method = "native_text"
            content = native_text.strip()
        else:
            image_path = context_root() / "page_images" / pdf_path.stem / f"page_{page_num:03d}.png"
            if image_path.exists() and tesseract_available:
                ocr_text, error = ocr_image(image_path)
                if normalized_text_score(ocr_text) > 0:
                    method = "ocr"
                    content = ocr_text
                else:
                    method = "unavailable"
                    content = error or f"OCR locale senza testo leggibile. Immagine pagina: {rel(image_path)}"
            else:
                method = "unavailable"
                content = (
                    "OCR non disponibile o immagine pagina mancante. "
                    f"Immagine attesa: {rel(image_path)}"
                )
        confidence = confidence_for(method, content)
        out_path = out_dir / f"page_{page_num:03d}.txt"
        write_page_text(out_path, source, page_num, method, confidence, content)
        pages.append(
            {
                "page": page_num,
                "text_path": rel(out_path),
                "method": method,
                "confidence": confidence,
                "token_score": normalized_text_score(content),
            }
        )

    summary = {
        "source_pdf": source,
        "pdf_stem": pdf_path.stem,
        "page_count": page_count,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "native_text_attempted": bool(native_pages),
        "tesseract_available": tesseract_available,
        "pages": pages,
    }
    (out_dir / "manifest.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return summary


def main() -> int:
    summaries = []
    for source in SOURCE_PDFS:
        if not (repo_root() / source).exists():
            print(f"[WARN] sorgente mancante: {source}", file=sys.stderr)
            continue
        print(f"[INFO] estrazione testo/OCR {source}")
        summaries.append(process_pdf(source))

    aggregate = context_root() / "extracted_text" / "manifest_all.json"
    aggregate.parent.mkdir(parents=True, exist_ok=True)
    aggregate.write_text(
        json.dumps(
            {
                "generated_at": datetime.now(timezone.utc).isoformat(),
                "source_count": len(summaries),
                "sources": summaries,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"[INFO] manifest aggregato: {rel(aggregate)}")
    return 0 if summaries else 1


if __name__ == "__main__":
    raise SystemExit(main())
