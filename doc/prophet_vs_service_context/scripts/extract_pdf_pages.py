#!/usr/bin/env python3
"""Render Prophet VS source PDFs into per-page PNG images.

Preferred renderer: PyMuPDF/fitz.
Local fallback: macOS CUPS cgpdftoraster + rastertotiff + Pillow.

No network services or uploads are used. If neither renderer is available,
the script writes a dependency note instead of modifying source PDFs.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
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

POST_RENDER_ROTATION = {
    # The scanned service package carries a PDF page rotation that the CUPS
    # fallback renders sideways. Rotate the generated bitmap so page labels and
    # title blocks are upright for OCR and visual review.
    "pvs_service": 270,
}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def context_root() -> Path:
    return Path(__file__).resolve().parents[1]


def rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(repo_root()).as_posix()
    except ValueError:
        return path.as_posix()


def ensure_dirs() -> None:
    base = context_root()
    for subdir in [
        "extracted_text",
        "page_images",
        "page_notes",
        "circuit_maps",
        "diagnostic_notes",
        "component_index",
        "scripts",
    ]:
        (base / subdir).mkdir(parents=True, exist_ok=True)


def write_dependency_note(message: str) -> None:
    note = context_root() / "scripts" / "MISSING_RENDER_DEPENDENCIES.md"
    note.write_text(message, encoding="utf-8")


def try_import_fitz():
    try:
        import fitz  # type: ignore

        return fitz
    except Exception:
        return None


def render_with_fitz(pdf_path: Path, out_dir: Path, dpi: int) -> dict[str, Any]:
    fitz = try_import_fitz()
    if fitz is None:
        raise RuntimeError("PyMuPDF/fitz non disponibile")

    doc = fitz.open(pdf_path)
    pages: list[dict[str, Any]] = []
    for idx, page in enumerate(doc, start=1):
        image_path = out_dir / f"page_{idx:03d}.png"
        pix = page.get_pixmap(dpi=dpi, alpha=False)
        pix.save(image_path)
        pages.append(
            {
                "page": idx,
                "image_path": rel(image_path),
                "width": pix.width,
                "height": pix.height,
                "dpi": dpi,
            }
        )
    return {
        "method": "pymupdf",
        "page_count": len(pages),
        "pages": pages,
    }


def cups_paths() -> tuple[Path | None, Path | None, Path | None]:
    cupsfilter = shutil.which("cupsfilter")
    rastertotiff = Path("/usr/libexec/cups/filter/rastertotiff")
    ppd = Path(
        "/System/Library/Frameworks/ApplicationServices.framework/Versions/A/"
        "Frameworks/PrintCore.framework/Versions/A/Resources/AirPrint.ppd"
    )
    return (
        Path(cupsfilter) if cupsfilter else None,
        rastertotiff if rastertotiff.exists() else None,
        ppd if ppd.exists() else None,
    )


def render_with_cups(pdf_path: Path, out_dir: Path, dpi: int) -> dict[str, Any]:
    from PIL import Image, ImageSequence

    cupsfilter, rastertotiff, ppd = cups_paths()
    missing = [
        name
        for name, value in [
            ("cupsfilter", cupsfilter),
            ("rastertotiff", rastertotiff),
            ("AirPrint.ppd", ppd),
        ]
        if value is None
    ]
    if missing:
        raise RuntimeError("Dipendenze CUPS mancanti: " + ", ".join(missing))

    with tempfile.TemporaryDirectory(prefix="prophet_pdf_render_") as tmp:
        tmpdir = Path(tmp)
        raster_path = tmpdir / f"{pdf_path.stem}.raster"
        tiff_path = tmpdir / f"{pdf_path.stem}.tiff"

        raster_cmd = [
            str(cupsfilter),
            "-P",
            str(ppd),
            "-o",
            f"Resolution={dpi}dpi",
            "-o",
            "outputorder=normal",
            "-m",
            "application/vnd.cups-raster",
            str(pdf_path),
        ]
        with raster_path.open("wb") as raster_file:
            subprocess.run(raster_cmd, check=True, stdout=raster_file)

        tiff_cmd = [
            str(rastertotiff),
            "1",
            "prophet",
            pdf_path.name,
            "1",
            "",
            str(raster_path),
        ]
        with tiff_path.open("wb") as tiff_file:
            subprocess.run(tiff_cmd, check=True, stdout=tiff_file)

        rendered = Image.open(tiff_path)
        pages: list[dict[str, Any]] = []
        for idx, frame in enumerate(ImageSequence.Iterator(rendered), start=1):
            image_path = out_dir / f"page_{idx:03d}.png"
            page_image = frame.convert("L")
            if pdf_path.stem in POST_RENDER_ROTATION:
                page_image = page_image.rotate(
                    POST_RENDER_ROTATION[pdf_path.stem], expand=True
                )
            page_image.save(image_path, format="PNG", dpi=(dpi, dpi), optimize=True)
            pages.append(
                {
                    "page": idx,
                    "image_path": rel(image_path),
                    "width": page_image.width,
                    "height": page_image.height,
                    "dpi": dpi,
                    "post_render_rotation": POST_RENDER_ROTATION.get(pdf_path.stem, 0),
                }
            )
    return {
        "method": "cups_airprint_rastertotiff",
        "page_count": len(pages),
        "pages": pages,
    }


def render_pdf(pdf_path: Path, dpi: int) -> dict[str, Any]:
    out_dir = context_root() / "page_images" / pdf_path.stem
    out_dir.mkdir(parents=True, exist_ok=True)

    if try_import_fitz() is not None:
        result = render_with_fitz(pdf_path, out_dir, dpi)
    else:
        result = render_with_cups(pdf_path, out_dir, dpi)
        write_dependency_note(
            "# Dipendenza PyMuPDF non disponibile\n\n"
            "PyMuPDF/fitz non e installato in questo ambiente. Lo script ha usato "
            "il fallback locale macOS CUPS (`cupsfilter` + `rastertotiff`) con "
            "Pillow per generare PNG a 300 DPI.\n\n"
            "Per usare il renderer preferito in futuro, installare localmente:\n\n"
            "```bash\npython3 -m pip install PyMuPDF\n```\n"
        )

    manifest = {
        "source_pdf": rel(pdf_path),
        "pdf_name": pdf_path.name,
        "pdf_stem": pdf_path.stem,
        "extraction_timestamp": datetime.now(timezone.utc).isoformat(),
        "renderer": result["method"],
        "page_count": result["page_count"],
        "pages": result["pages"],
        "notes": (
            "I PDF originali non sono stati modificati. Rendering eseguito "
            "localmente; se OCR/testo risultano incerti, usare [NON CHIARO]."
        ),
    }
    (out_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return manifest


def main() -> int:
    ensure_dirs()
    manifests: list[dict[str, Any]] = []
    dpi = 300
    for source in SOURCE_PDFS:
        pdf_path = repo_root() / source
        if not pdf_path.exists():
            print(f"[WARN] sorgente mancante: {source}", file=sys.stderr)
            continue
        print(f"[INFO] rendering {source}")
        try:
            manifests.append(render_pdf(pdf_path, dpi))
        except Exception as exc:
            message = (
                "# Rendering PDF non riuscito\n\n"
                f"Sorgente: `{source}`\n\n"
                f"Errore: `{exc}`\n\n"
                "Installare PyMuPDF localmente oppure eseguire su macOS con "
                "`cupsfilter`, `rastertotiff` e Pillow disponibili.\n"
            )
            write_dependency_note(message)
            print(f"[ERROR] {source}: {exc}", file=sys.stderr)
    aggregate = context_root() / "page_images" / "manifest_all.json"
    aggregate.write_text(
        json.dumps(
            {
                "generated_at": datetime.now(timezone.utc).isoformat(),
                "source_count": len(manifests),
                "sources": manifests,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"[INFO] manifest aggregato: {rel(aggregate)}")
    return 0 if manifests else 1


if __name__ == "__main__":
    raise SystemExit(main())
