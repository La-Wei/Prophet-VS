#!/usr/bin/env python3
"""Generate Markdown knowledge base files from extracted Prophet VS material."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Iterable


SOURCE_ORDER = [
    "sci_prophet_vs_ecr738",
    "sci_prophet_vs_ecr739",
    "pvs_service",
    "5508",
    "5530",
]

SOURCE_PDF = {
    "sci_prophet_vs_ecr738": "doc/sci_prophet_vs_ecr738.pdf",
    "sci_prophet_vs_ecr739": "doc/sci_prophet_vs_ecr739.pdf",
    "pvs_service": "doc/pvs_service.pdf",
    "5508": "doc/5508.pdf",
    "5530": "doc/5530.pdf",
}

PAGE_META = {
    ("sci_prophet_vs_ecr738", 1): {
        "title": "ECR 738, modulo engineering change record",
        "types": ["ECR / engineering change record", "board revision"],
        "confirmed": [
            "Pagina modulo ECR Sequential con campi di approvazione, priorita e motivo modifica.",
            "OCR legge ECR, Sequential, type of change, release/design/standard record.",
        ],
        "inferred": [
            "Probabile copertina/amministrazione della modifica ECR 738; i dettagli tecnici stanno nelle pagine successive.",
        ],
        "related": [("sci_prophet_vs_ecr738", 2), ("sci_prophet_vs_ecr739", 1)],
    },
    ("sci_prophet_vs_ecr738", 2): {
        "title": "ECR 738, modifica area pressure sensor su main analog/sample & hold",
        "types": ["ECR / engineering change record", "pressure circuit", "sample & hold", "board revision"],
        "confirmed": [
            "L'immagine mostra PRESSURE SENSOR, U459 op amp, R458 annotata come 15K, rail +12V e -12V, e uscite VCA/VCF/PAN/LEV da un 5530.",
            "Si leggono modifiche/annotazioni vicino a R458, una resistenza da 1K e una indicazione manoscritta vicino a +12V.",
        ],
        "inferred": [
            "La modifica sembra intervenire sul bias/scala del pressure sensor e quindi sulla tensione SENSOR inviata alla logica/ADC.",
            "La vicinanza al blocco 5530 rende la pagina rilevante per CV VCA/VCF/PAN/LEV, ma non prova un guasto del 5530.",
        ],
        "related": [("pvs_service", 6), ("sci_prophet_vs_ecr739", 4), ("5530", 1)],
    },
    ("sci_prophet_vs_ecr738", 3): {
        "title": "ECR 738, dettaglio board/artwork poco leggibile",
        "types": ["board artwork / layout", "ECR / engineering change record"],
        "confirmed": ["OCR molto scarso; si legge solo parzialmente OSCIL/BOARD e testo non affidabile."],
        "inferred": ["Probabile immagine di riferimento fisico/artwork collegata alla modifica ECR 738."],
        "related": [("sci_prophet_vs_ecr738", 2)],
    },
    ("sci_prophet_vs_ecr739", 1): {
        "title": "ECR 739, modulo engineering change record",
        "types": ["ECR / engineering change record", "board revision"],
        "confirmed": [
            "Pagina modulo ECR Sequential con campi release/design, approval, effective date e controllo documentale.",
        ],
        "inferred": ["Copertina/amministrazione della modifica ECR 739."],
        "related": [("sci_prophet_vs_ecr739", 4), ("sci_prophet_vs_ecr738", 1)],
    },
    ("sci_prophet_vs_ecr739", 2): {
        "title": "ECR 739, testo descrittivo poco leggibile",
        "types": ["ECR / engineering change record", "board revision"],
        "confirmed": ["OCR poco chiaro; molte parole sono [NON CHIARO]."],
        "inferred": ["Probabile pagina descrittiva o istruzioni della modifica ECR 739."],
        "related": [("sci_prophet_vs_ecr739", 4)],
    },
    ("sci_prophet_vs_ecr739", 3): {
        "title": "ECR 739, pagina quasi illeggibile",
        "types": ["ECR / engineering change record", "board revision"],
        "confirmed": ["OCR quasi nullo; non usare questa pagina senza ispezione immagine manuale."],
        "inferred": ["Possibile pagina intermedia o allegato della modifica ECR 739."],
        "related": [("sci_prophet_vs_ecr739", 4)],
    },
    ("sci_prophet_vs_ecr739", 4): {
        "title": "ECR 739, pressure circuit e power supply su digital/keyboard board",
        "types": ["pressure circuit", "keyboard matrix", "alimentazione", "reset", "ECR / engineering change record"],
        "confirmed": [
            "L'immagine mostra PRESSURE CIRCUIT, R321 OFFSET 50K, R307 20K, R308 10K, R309 47K, R320 10K, R304 15K, U310 op amp, U305 HC132, U301 7805, U302 7812, U303 7912 e U304 78L05.",
            "Sono visibili TP301, TP302, SENSOR, PRESSURE, +5VD, +12V, -12V, DGND, AGND e hardware mains/trasformatore.",
        ],
        "inferred": [
            "Questa pagina collega il pressure sensor al circuito keyboard/power/reset e va confrontata fisicamente con eventuali tagli piste o jumper ECR.",
        ],
        "related": [("pvs_service", 4), ("pvs_service", 6), ("sci_prophet_vs_ecr738", 2)],
    },
    ("pvs_service", 1): {
        "title": "Schematic PCB left front panel",
        "types": ["schema elettrico", "front panel", "controlli", "ADC", "joystick/pitch/mod"],
        "confirmed": [
            "Title block leggibile nell'immagine: SCHEMATIC PCB LEFT FRONT PANEL.",
            "Sono visibili ADC0808, LCD/front panel, switch e controlli come pitch/mod wheel, joystick, data entry, volume/balance e linee +5V.",
        ],
        "inferred": ["Pagina utile per controlli pannello, contaminazione CV dai potenziometri e routing verso logica/ADC."],
        "related": [("pvs_service", 2), ("pvs_service", 3), ("pvs_service", 4)],
    },
    ("pvs_service", 2): {
        "title": "Schematic PCB right front panel and main cartridge",
        "types": ["schema elettrico", "front panel", "cartridge board", "keyboard/pannello"],
        "confirmed": [
            "Title block leggibile: SCHEMATIC PCB RIGHT FRONT PANEL AND MAIN CARTRIDGE, 2400.",
            "Sono visibili MAIN CARTRIDGE BD 2400-6, P201/P602/J601, CD0-CD15, CA1-CA13, CART OE/WE/CE, PROT, +5VD/GND e LED front panel.",
        ],
        "inferred": ["Pagina rilevante per cartridge board, switch/LED del pannello e linee digitali condivise."],
        "related": [("pvs_service", 1), ("pvs_service", 3)],
    },
    ("pvs_service", 3): {
        "title": "Schematic PCB digital processor",
        "types": ["schema elettrico", "digital board", "CPU", "MIDI", "reset", "RAM/ROM"],
        "confirmed": [
            "Title block leggibile: SCHEMATIC PCB DIGITAL, 2400 PROCESSOR.",
            "Sono visibili 68000, 27256 ROM, 6264 non-volatile RAM, 6116 RAM, 68B50 UART, MIDI OUT/THRU/IN, data/address bus, clock/reset.",
        ],
        "inferred": ["Pagina utile per reset, bus digitale, MIDI e cause digitali che possono influire sul refresh CV."],
        "related": [("pvs_service", 4), ("pvs_service", 6), ("pvs_service", 13)],
    },
    ("pvs_service", 4): {
        "title": "Digital keyboard and power supply, pressure circuit",
        "types": ["schema elettrico", "keyboard matrix", "pressure circuit", "alimentazione", "reset"],
        "confirmed": [
            "Title block leggibile: SCHEMATIC PCB DIGITAL 2400 KEYBOARD AND POWER SUPPLY.",
            "Sono visibili KEYBOARD MATRIX, PRESSURE CIRCUIT, R321 OFFSET, R307/R308/R309/R320/R304/R305, U310 op amp, U301 7805, U302 7812, U303 7912, U304 78L05, U305 HC132, TP301/TP302, +5VD, +12V, -12V, DGND, AGND.",
        ],
        "inferred": ["Questa pagina e' centrale per pressure/aftertouch, alimentazione, reset e diagnostica rails."],
        "related": [("sci_prophet_vs_ecr739", 4), ("pvs_service", 6)],
    },
    ("pvs_service", 5): {
        "title": "PCB artwork/layout digital or keyboard board",
        "types": ["board artwork / layout", "riparazione fisica"],
        "confirmed": ["OCR mostra molti riferimenti fisici U30x, C30x, J30x/P30x e componenti della famiglia 2400."],
        "inferred": ["Probabile layout/artwork fisico utile per localizzare componenti della board digital/keyboard."],
        "related": [("pvs_service", 3), ("pvs_service", 4)],
    },
    ("pvs_service", 6): {
        "title": "Main analog 2400 sample & hold / sensor, sheet 1 of 4",
        "types": ["schema elettrico", "sample & hold", "pressure circuit", "generazione CV", "alimentazione analogica"],
        "confirmed": [
            "Title block leggibile: SCHEMATIC PCB MAIN ANALOG 2400 SAMPLE & HOLD - SENSOR.",
            "Sono visibili U449 5530, U425 5530, DAC/U451 6012, U459 741, R458, P402/P403, U450 78M08, U402 78M05, U401 7905, pressure sensor, VCA/VCF/PAN/LEV outputs, LEFT/RIGHT CHORUS CV, LEFT/RIGHT FINAL CV, +12V, -12V, +5.6V, +8V, -5V, AGND.",
        ],
        "inferred": ["Pagina chiave per CV bleed/droop, pressione, VCA/VCF/PAN/LEV e possibili problemi da S&H o rails analogici."],
        "related": [("5530", 1), ("5530", 3), ("sci_prophet_vs_ecr738", 2), ("pvs_service", 9)],
    },
    ("pvs_service", 7): {
        "title": "Main analog 2400 waveform / voice CV area",
        "types": ["schema elettrico", "generazione waveform", "sample & hold", "analog board"],
        "confirmed": [
            "OCR mostra bus +5VD/+SVx, componenti U4xx/R4xx/C4xx e segnali analogici della board main analog.",
        ],
        "inferred": ["Probabile foglio main analog successivo al S&H, con circuiti voice/wave o routing CV."],
        "related": [("pvs_service", 6), ("pvs_service", 8), ("pvs_service", 9)],
    },
    ("pvs_service", 8): {
        "title": "Main analog 2400 waveform / voice analog area",
        "types": ["schema elettrico", "generazione waveform", "analog board"],
        "confirmed": ["OCR mostra U4xx/C4xx/R4xx, +5VD/+5VPN e riferimenti a FET/circuiti analogici."],
        "inferred": ["Probabile foglio main analog legato a voice/waveform e switching analogico."],
        "related": [("pvs_service", 7), ("pvs_service", 9)],
    },
    ("pvs_service", 9): {
        "title": "Main analog 2400 voice/audio path: VCF/VCA/PAN",
        "types": ["schema elettrico", "audio path", "VCA", "VCF", "pan", "analog board"],
        "confirmed": [
            "OCR legge LEFT, VCF OUT, VCAOUT, PAN, VOICE, VCAIN e vari riferimenti R4xx/C4xx.",
        ],
        "inferred": ["Pagina rilevante per audio distorto, bleed a volume zero, VCA/VCF/PAN e percorso voce analogico."],
        "related": [("pvs_service", 6), ("pvs_service", 11), ("pvs_service", 12)],
    },
    ("pvs_service", 10): {
        "title": "PCB artwork/layout main analog",
        "types": ["board artwork / layout", "riparazione fisica", "analog board"],
        "confirmed": ["OCR mostra molti riferimenti R4xx/C4xx/U4xx tipici della main analog board."],
        "inferred": ["Probabile layout/artwork fisico per la main analog board."],
        "related": [("pvs_service", 6), ("pvs_service", 9)],
    },
    ("pvs_service", 11): {
        "title": "Audio output / chorus area, left/right",
        "types": ["schema elettrico", "audio path", "chorus", "output"],
        "confirmed": ["OCR mostra LEFT, C9xx/R9xx, output, valori come 301K/100pF e riferimenti a left/right voices."],
        "inferred": ["Probabile sezione chorus/output o filtro audio correlato ai canali left/right."],
        "related": [("pvs_service", 9), ("pvs_service", 12)],
    },
    ("pvs_service", 12): {
        "title": "Audio output / 7 kHz lowpass / right voice",
        "types": ["schema elettrico", "audio path", "chorus", "lowpass"],
        "confirmed": [
            "OCR legge RIGHT VOICES, LEV, 7 KHZ LOWPASS, TL082/082, C9xx/R9xx e +12V/-12V.",
        ],
        "inferred": ["Pagina importante per filtro di uscita, chorus/output e distorsione sui canali finali."],
        "related": [("pvs_service", 9), ("pvs_service", 11)],
    },
    ("pvs_service", 13): {
        "title": "Digital bus / board interconnect page",
        "types": ["schema elettrico", "digital board", "bus", "interconnect"],
        "confirmed": ["OCR mostra DATA BUS, +5V, CS, ABxx, D0/D1/D2 e segnali digitali/interconnect."],
        "inferred": ["Probabile foglio di interconnessione digitale o decoding bus."],
        "related": [("pvs_service", 3)],
    },
    ("5508", 1): {
        "title": "PD508 datasheet overview",
        "types": ["datasheet", "sample & hold"],
        "confirmed": [
            "Datasheet OnChip Systems PD508 Octal Sample & Hold, con highlights: 8 sample-and-hold, acquisition time, low hold step, low droop, internal hold capacitors.",
        ],
        "inferred": ["Utile per capire comportamento S&H, droop e bleed CV in circuiti compatibili."],
        "related": [("5508", 2), ("5530", 1), ("pvs_service", 6)],
    },
    ("5508", 2): {
        "title": "PD508 specifications and application hints",
        "types": ["datasheet", "sample & hold"],
        "confirmed": ["Pagina specifiche/application hints con supply, acquisition, aperture/jitter e range di alimentazione."],
        "inferred": ["Rilevante per valutare se rail o timing S&H possono causare errore/droop."],
        "related": [("5508", 1), ("5508", 3)],
    },
    ("5508", 3): {
        "title": "PD508 timing/address/inhibit notes",
        "types": ["datasheet", "sample & hold", "timing"],
        "confirmed": ["Pagina con ADDRESS, INHIBIT, SAMPLE AND HOLD SWITCH e note su timing minimo."],
        "inferred": ["Utile per controllare problemi di refresh CV e gating/inhibit."],
        "related": [("5508", 2), ("5508", 4)],
    },
    ("5508", 4): {
        "title": "PD508 input/output considerations",
        "types": ["datasheet", "sample & hold"],
        "confirmed": ["Pagina con input/output considerations, sorgente a bassa impedenza/op amp e capacitori di feedback."],
        "inferred": ["Utile per leakage, caricamento uscita e stabilita dei CV."],
        "related": [("5508", 3), ("5530", 4)],
    },
    ("5530", 1): {
        "title": "CEM5530 preliminary datasheet overview",
        "types": ["datasheet", "sample & hold", "CEM5530"],
        "confirmed": [
            "Datasheet preliminare CEM5530 30-channel multiplexed Sample and Hold; descrive auto-zero op amp, analog multiplexer, 5-bit decoder e 30 S&H.",
            "OCR legge settling to 12 bits under 2 us, error <2 mV, outputs about -5 to +5V with +/-7.5V supplies.",
        ],
        "inferred": ["Molto rilevante per generazione CV Prophet VS e sintomi di droop/bleed/modulation leak."],
        "related": [("5530", 3), ("5530", 4), ("pvs_service", 6)],
    },
    ("5530", 2): {
        "title": "CEM5530 pinout/diagram, OCR scarso",
        "types": ["datasheet", "sample & hold", "pinout"],
        "confirmed": ["OCR scarso; sembra diagramma/pinout del CEM5530."],
        "inferred": ["Usare l'immagine per pinout se serve, non affidarsi solo all'OCR."],
        "related": [("5530", 1), ("5530", 3)],
    },
    ("5530", 3): {
        "title": "CEM5530 application hints and power supplies",
        "types": ["datasheet", "sample & hold", "alimentazione"],
        "confirmed": [
            "Pagina application hints: supply voltage tra VDD e VSS non deve superare 16V; supplies positive/negative influenzano swing input/output.",
        ],
        "inferred": ["Utile per collegare rail analogici fuori tolleranza a clipping/errore CV."],
        "related": [("5530", 1), ("pvs_service", 6)],
    },
    ("5530", 4): {
        "title": "CEM5530 inhibit/address timing",
        "types": ["datasheet", "sample & hold", "timing"],
        "confirmed": [
            "Pagina timing: INHIBIT deve restare high abbastanza per auto-zero, almeno 2 us; address hold/settling citati.",
        ],
        "inferred": ["Rilevante per refresh CV, aggiornamento canali e possibili errori temporali."],
        "related": [("5530", 1), ("pvs_service", 6)],
    },
}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def ctx_root() -> Path:
    return Path(__file__).resolve().parents[1]


def read_text_file(stem: str, page: int) -> tuple[str, str, str]:
    path = ctx_root() / "extracted_text" / stem / f"page_{page:03d}.txt"
    raw = path.read_text(encoding="utf-8")
    method = re.search(r"^METHOD: (.+)$", raw, re.M)
    confidence = re.search(r"^CONFIDENCE: (.+)$", raw, re.M)
    content = raw.split("CONTENT:", 1)[-1].strip()
    return method.group(1) if method else "unknown", confidence.group(1) if confidence else "unknown", content


def page_count(stem: str) -> int:
    manifest = ctx_root() / "page_images" / stem / "manifest.json"
    return json.loads(manifest.read_text(encoding="utf-8"))["page_count"]


def ensure_dirs() -> None:
    for sub in [
        "page_notes",
        "circuit_maps",
        "diagnostic_notes",
        "component_index",
    ]:
        (ctx_root() / sub).mkdir(parents=True, exist_ok=True)


def page_note_path(stem: str, page: int) -> Path:
    return ctx_root() / "page_notes" / stem / f"page_{page:03d}.md"


def link_to_page_note(stem: str, page: int, label: str | None = None, prefix: str = "") -> str:
    label = label or f"{stem} pagina {page}"
    return f"[{label}]({prefix}page_notes/{stem}/page_{page:03d}.md)"


def link_from_page_note(current_stem: str, target_stem: str, page: int, label: str | None = None) -> str:
    label = label or f"{target_stem} pagina {page}"
    if current_stem == target_stem:
        href = f"page_{page:03d}.md"
    else:
        href = f"../{target_stem}/page_{page:03d}.md"
    return f"[{label}]({href})"


def note_relative_image(stem: str, page: int) -> str:
    return f"../../page_images/{stem}/page_{page:03d}.png"


def note_relative_text(stem: str, page: int) -> str:
    return f"../../extracted_text/{stem}/page_{page:03d}.txt"


def clean_cell(value: str) -> str:
    return value.replace("|", "/").replace("\n", " ").strip()


def extract_refs(text: str) -> dict[str, list[str]]:
    patterns = {
        "ics": r"\b(?:U\d{3,4}|CEM\s*5530|CEM5530|PD\s*508|PD508|ADC0808|68B50|68000|5530|4051|TL0?82|TL0?81|HC\d{2,3}|LS\d{2,3}|LM\d{3,4}|78M?0?5|78M?08|7905|7812|7912)\b",
        "res_caps": r"\b(?:R\d{3,4}|C\d{3,4}|RA\d{3,4}|RP\d{3,4}|RB\d{1,4})\b",
        "connectors": r"\b(?:P\d{3,4}|J\d{3,4}|TB\d{3,4}|TP\d{3,4})\b",
    }
    out: dict[str, list[str]] = {}
    for key, pat in patterns.items():
        vals = []
        for match in re.findall(pat, text, flags=re.I):
            value = re.sub(r"\s+", "", match.upper())
            if value not in vals:
                vals.append(value)
        out[key] = vals
    rails = [
        "+5V",
        "+5VD",
        "+5VA",
        "-5V",
        "+12V",
        "-12V",
        "+8V",
        "+5.6V",
        "AGND",
        "DGND",
        "GND",
        "VDD",
        "VSS",
        "VREF",
    ]
    nets = [
        "LEFT",
        "RIGHT",
        "PAN",
        "LEV",
        "VCA",
        "VCF",
        "PRESSURE",
        "SENSOR",
        "RESET",
        "INH",
        "DAC",
        "DATA BUS",
        "ADDRESS BUS",
        "CHORUS",
        "CART",
        "MIDI",
        "KEYBOARD",
        "SWIN",
        "OUTPUT EN",
        "LEFT CHORUS",
        "RIGHT CHORUS",
        "LEFT FINAL CV",
        "RIGHT FINAL CV",
    ]
    up = text.upper()
    out["rails"] = [r for r in rails if r in up]
    out["nets"] = [n for n in nets if n in up]
    return out


def source_page_label(stem: str, page: int) -> str:
    return f"{SOURCE_PDF[stem]} pagina {page}"


def refs_to_lines(refs: dict[str, list[str]]) -> str:
    sections = [
        ("IC / chip", "ics"),
        ("Resistenze / capacitori / reti", "res_caps"),
        ("Connettori / test point", "connectors"),
        ("Rail", "rails"),
        ("Net nominate", "nets"),
    ]
    lines = []
    for label, key in sections:
        vals = refs.get(key, [])
        shown = ", ".join(vals[:80]) if vals else "[NON CHIARO]"
        if len(vals) > 80:
            shown += f", ... ({len(vals)} totali OCR)"
        lines.append(f"- {label}: {shown}")
    return "\n".join(lines)


def make_page_notes() -> None:
    for stem in SOURCE_ORDER:
        out_dir = ctx_root() / "page_notes" / stem
        out_dir.mkdir(parents=True, exist_ok=True)
        for page in range(1, page_count(stem) + 1):
            method, confidence, content = read_text_file(stem, page)
            meta = PAGE_META.get((stem, page), {})
            title = meta.get("title", f"{stem} pagina {page}")
            refs = extract_refs(content + "\n" + " ".join(meta.get("confirmed", [])))
            related = meta.get("related", [])
            related_links = (
                "\n".join(f"- {link_from_page_note(stem, s, p)}" for s, p in related)
                if related
                else "- [NON CHIARO]"
            )
            types = ", ".join(meta.get("types", ["[NON CHIARO]"]))
            confirmed = "\n".join(f"- {x}" for x in meta.get("confirmed", ["[NON CHIARO]"]))
            inferred = "\n".join(f"- {x}" for x in meta.get("inferred", ["[NON CHIARO]"]))
            uncertain = (
                "- OCR e scansione non garantiscono valori completi; verificare sempre l'immagine pagina.\n"
                "- Non assumere che una modifica ECR sia presente sulla macchina reale senza ispezione fisica."
            )
            body = f"""# {stem} pagina {page}

Source: `{SOURCE_PDF[stem]}` pagina {page}  
Immagine: [{stem}/page_{page:03d}.png]({note_relative_image(stem, page)})  
Testo/OCR: [{stem}/page_{page:03d}.txt]({note_relative_text(stem, page)})  
Metodo testo: `{method}`, confidenza: `{confidence}`

## Cosa sembra contenere questa pagina
{title}. Tipo pagina: {types}.

## Etichette / componenti / IC / net visibili
{refs_to_lines(refs)}

## Riassunto funzione del circuito
Confermato dalle etichette:
{confirmed}

Inferenza ragionevole:
{inferred}

Incerto / da verificare manualmente:
{uncertain}

## Rilevanza per riparazione
- Utile per collegare sintomi a pagine sorgente e localizzare componenti o net sul Prophet VS.
- Se la pagina contiene artwork/layout, usarla per ispezione fisica: piste, jumper, tagli, saldature, riparazioni precedenti.
- Se la pagina contiene schema, usarla per ragionare su rail, segnali, connettori e possibili cause, senza trattare l'OCR come prova definitiva.

## Possibili failure mode collegati a questa pagina
- Saldatura crepata, pista/via danneggiata, connettore ossidato o riparazione precedente non conforme.
- Componente attivo guasto o alimentazione fuori specifica nei blocchi mostrati.
- Condensatore in perdita, valore resistenza errato o rete resistiva modificata male, se applicabile alla pagina.
- CV bleed/droop, op amp guasto, analog switch/S&H guasto, ground analogico/digitale contaminato o ripple sui rail quando la pagina mostra circuiti analogici/CV.

## Cross-reference
{related_links}
"""
            page_note_path(stem, page).write_text(body, encoding="utf-8")


def make_source_files() -> None:
    body = """# Source files

Ogni riassunto e' basato sul materiale scannerizzato visibile e sull'OCR locale; non e' garantito completo.

| File | Scopo apparente | Affidabilita |
| --- | --- | --- |
| `doc/sci_prophet_vs_ecr738.pdf` | ECR 738, engineering change record Sequential. Sembra relativo a Prophet VS PCB 2400/main analog sample & hold / sensor e modifiche al pressure sensor. | Medio/basso: scansione chiara solo in parte; pagina 2 mostra il dettaglio piu utile. |
| `doc/sci_prophet_vs_ecr739.pdf` | ECR 739, engineering change record Sequential. Sembra relativo a Prophet VS PCB 2400 digital/keyboard/power supply e pressure circuit changes. | Medio/basso: pagina 4 e' la piu leggibile; pagine 2-3 sono poco chiare. |
| `doc/pvs_service.pdf` | Pacchetto schemi Prophet VS: front panel, cartridge, digital processor, keyboard/power/pressure, main analog sample & hold/sensor, voice/audio/chorus/output e artwork/layout. | Medio: OCR rumoroso ma immagini renderizzate sono leggibili. |
| `doc/5508.pdf` | Datasheet OnChip Systems PD508 Octal Sample & Hold. | Medio: OCR leggibile; verificare formule e tabelle sull'immagine. |
| `doc/5530.pdf` | Datasheet preliminare CEM5530 30-channel Sample & Hold. | Medio: pagine 1, 3, 4 leggibili; pagina 2/pinout richiede verifica immagine. |
"""
    (ctx_root() / "source_files.md").write_text(body, encoding="utf-8")


def page_list(items: Iterable[tuple[str, int, str | None]]) -> str:
    return "\n".join(f"- {link_to_page_note(stem, page, label)}" for stem, page, label in items)


def make_index() -> None:
    body = f"""# Prophet VS service context index

## Pressure / aftertouch circuit
{page_list([
    ("sci_prophet_vs_ecr738", 2, "ECR738 pressure sensor modification"),
    ("sci_prophet_vs_ecr739", 4, "ECR739 pressure circuit / power supply"),
    ("pvs_service", 4, "Digital keyboard and power supply: pressure circuit"),
    ("pvs_service", 6, "Main analog sample & hold / sensor"),
    ("5530", 1, "CEM5530 overview, CV generation context"),
])}

## Sample & Hold / generazione CV
{page_list([
    ("pvs_service", 6, "Main analog S&H/sensor, CEM5530 outputs"),
    ("pvs_service", 7, "Main analog wave/CV area"),
    ("pvs_service", 8, "Main analog wave/voice area"),
    ("pvs_service", 9, "VCF/VCA/PAN audio/CV area"),
    ("5508", 1, "PD508 overview"),
    ("5508", 2, "PD508 specifications"),
    ("5508", 3, "PD508 timing"),
    ("5508", 4, "PD508 input/output"),
    ("5530", 1, "CEM5530 overview"),
    ("5530", 3, "CEM5530 application hints"),
    ("5530", 4, "CEM5530 timing"),
])}

## Audio path / VCA / filtri / chorus
{page_list([
    ("pvs_service", 6, "CV outputs for VCA/VCF/PAN/LEV and chorus/final CV"),
    ("pvs_service", 9, "Main analog VCF/VCA/PAN"),
    ("pvs_service", 11, "Audio output / chorus area"),
    ("pvs_service", 12, "Right voices / 7 kHz lowpass / output"),
])}

## Keyboard / pannello / controlli
{page_list([
    ("pvs_service", 1, "Left front panel controls"),
    ("pvs_service", 2, "Right front panel and cartridge"),
    ("pvs_service", 4, "Keyboard matrix / pressure"),
    ("sci_prophet_vs_ecr739", 4, "Pressure/keyboard/power ECR page"),
])}

## Alimentazione / rail
{page_list([
    ("pvs_service", 4, "Digital keyboard and power supply"),
    ("pvs_service", 6, "Main analog local regulators and analog rails"),
    ("pvs_service", 3, "Digital reset/clock/bus"),
    ("sci_prophet_vs_ecr739", 4, "Power supply and reset on ECR739"),
    ("5530", 3, "CEM5530 power supply limits"),
])}

## Board artwork / riparazione fisica
{page_list([
    ("pvs_service", 5, "Digital/keyboard PCB artwork/layout"),
    ("pvs_service", 10, "Main analog PCB artwork/layout"),
    ("sci_prophet_vs_ecr738", 3, "ECR738 artwork/layout reference"),
    ("sci_prophet_vs_ecr739", 2, "ECR739 support page, low confidence"),
])}
"""
    (ctx_root() / "index.md").write_text(body, encoding="utf-8")


def gather_ref_pages() -> dict[str, dict[str, set[tuple[str, int]]]]:
    gathered: dict[str, dict[str, set[tuple[str, int]]]] = {
        "ics": defaultdict(set),
        "res_caps": defaultdict(set),
        "connectors": defaultdict(set),
        "rails": defaultdict(set),
        "nets": defaultdict(set),
    }
    for stem in SOURCE_ORDER:
        for page in range(1, page_count(stem) + 1):
            _, _, content = read_text_file(stem, page)
            meta = PAGE_META.get((stem, page), {})
            text = content + "\n" + " ".join(meta.get("confirmed", []))
            refs = extract_refs(text)
            for group, values in refs.items():
                for value in values:
                    gathered[group][value].add((stem, page))
    return gathered


CURATED_REFS = {
    "ics": [
        ("CEM5530", "pvs_service pagina 6; 5530.pdf pagine 1-4", "30-channel sample & hold per generazione CV", "Molto rilevante per droop/bleed CV; verificare U449/U425 sullo schema."),
        ("PD508", "5508.pdf pagine 1-4", "Octal sample & hold datasheet", "Usare per concetti di hold step, droop e timing; non necessariamente montato nel Prophet VS esaminato."),
        ("U449", "pvs_service pagina 6", "CEM5530 con uscite VCA/VCF/PAN e chorus/final CV", "Visibile nello schema; parte esatta indicata come 5530."),
        ("U425", "pvs_service pagina 6", "CEM5530 con uscite LEV", "Visibile nello schema; verificare sulla board."),
        ("U459", "pvs_service pagina 6; sci_prophet_vs_ecr738 pagina 2", "Op amp pressure sensor", "ECR738 mostra R458 vicino a U459; verificare valori fisici."),
        ("U310", "pvs_service pagina 4; sci_prophet_vs_ecr739 pagina 4", "Op amp pressure circuit / keyboard board", "Visibile nello schema pressure ECR739."),
        ("U301/U302/U303", "pvs_service pagina 4; sci_prophet_vs_ecr739 pagina 4", "Regolatori 7805/7812/7912", "Sezione alimentazione; attenzione a mains/trasformatore."),
    ],
    "res_caps": [
        ("R458", "sci_prophet_vs_ecr738 pagina 2; pvs_service pagina 6", "Resistenza modificata vicino a pressure sensor/U459", "ECR immagine indica 15K; verificare fisicamente e non assumere applicazione."),
        ("R321", "pvs_service pagina 4; sci_prophet_vs_ecr739 pagina 4", "Offset pressure circuit", "Visibile come 50K nello schema ECR739/pvs."),
        ("R307/R308/R309/R320/R304", "pvs_service pagina 4; sci_prophet_vs_ecr739 pagina 4", "Rete pressure circuit", "Valori leggibili su ECR739: 20K/10K/47K/10K/15K, da verificare."),
        ("C401/C402", "pvs_service pagina 6", "Capacitori/regolatori locali analogici", "Vicino a 7905/78M05; verificare polarita e ripple."),
    ],
    "connectors": [
        ("P402/P403", "pvs_service pagina 6", "Interconnessione S&H/sensor/CV", "Mostra SENSOR, DGND e vari rail/CV; usare per tracciamento non invasivo."),
        ("P302/P305", "pvs_service pagina 4; pvs_service pagina 6", "Connettori digital/analog board", "Visibili in circuiti pressure/power e S&H."),
        ("J401/J306", "pvs_service pagina 6; sci_prophet_vs_ecr739 pagina 4", "Pressure sensor connector, lettura incerta per numerazione", "OCR/immagine non sempre concordano; verificare visivamente."),
    ],
    "rails": [
        ("+5VD", "pvs_service pagine 3-4, 6", "Logica digitale", "Rail digitale, possibile causa di reset o refresh CV se basso/ripple."),
        ("+12V / -12V", "pvs_service pagine 4, 6, 12", "Rail analogici/op amp e alimentazione", "Rilevanti per headroom op amp e S&H; misurare con cautela."),
        ("+8V / +5.6V / -5V", "pvs_service pagina 6", "Rail locali main analog/S&H", "Visibili vicino a regolatori 78M08/78M05/7905."),
        ("AGND / DGND", "pvs_service pagine 4, 6", "Ground analogico/digitale", "Contaminazione o connessioni difettose possono causare bleed/rumore."),
    ],
    "nets": [
        ("PRESSURE / SENSOR", "pvs_service pagine 4, 6; ECR738 pagina 2; ECR739 pagina 4", "Pressure/aftertouch sense path", "Non assumere taratura o ECR applicata senza ispezione."),
        ("VCA / VCF / PAN / LEV", "pvs_service pagine 6, 9", "CV verso VCA, filtri, pan e livelli", "Candidati per bleed/modulation leak."),
        ("LEFT / RIGHT / CHORUS", "pvs_service pagine 6, 9, 11, 12", "Audio/output e chorus", "Rilevante per suono con volume a zero o uscita distorta."),
        ("RESET", "pvs_service pagine 3-4; ECR739 pagina 4", "Reset digitale/logica", "Problemi qui possono alterare inizializzazione e controllo CV."),
    ],
}


def make_component_index() -> None:
    gathered = gather_ref_pages()
    files = {
        "ics": "ics.md",
        "res_caps": "resistors_caps.md",
        "connectors": "connectors.md",
        "rails": "power_rails.md",
        "nets": "named_nets.md",
    }
    titles = {
        "ics": "ICs",
        "res_caps": "Resistenze e capacitori",
        "connectors": "Connettori e test point",
        "rails": "Power rails",
        "nets": "Named nets",
    }
    for group, filename in files.items():
        rows = []
        for ref, src, func, note in CURATED_REFS.get(group, []):
            rows.append((ref, src, func, note))
        curated_names = {r[0] for r in rows}
        for ref in sorted(gathered[group]):
            if ref in curated_names:
                continue
            pages = sorted(gathered[group][ref])
            page_refs = "; ".join(f"{s} pagina {p}" for s, p in pages[:8])
            if len(pages) > 8:
                page_refs += f"; ... {len(pages)} occorrenze"
            rows.append((ref, page_refs, "OCR/immagine: contesto da verificare nella page note", "Estratto automaticamente; possibili falsi OCR."))
        body = [f"# {titles[group]}", "", "| Riferimento / Net | Visto in pagina sorgente | Funzione / contesto | Note / incertezza |", "| --- | --- | --- | --- |"]
        for ref, src, func, note in rows:
            body.append(f"| {clean_cell(ref)} | {clean_cell(src)} | {clean_cell(func)} | {clean_cell(note)} |")
        (ctx_root() / "component_index" / filename).write_text("\n".join(body) + "\n", encoding="utf-8")


def make_circuit_maps() -> None:
    maps = {
        "pressure_aftertouch.md": {
            "title": "Pressure / Aftertouch",
            "sources": [("pvs_service", 4), ("pvs_service", 6), ("sci_prophet_vs_ecr738", 2), ("sci_prophet_vs_ecr739", 4)],
            "components": "U310, U459, R321, R307, R308, R309, R320, R304, R458, pressure sensor connector, TP301/TP302.",
            "rails": "+12V, -12V, +5VD, AGND/DGND; ECR738 page 2 also shows local +12V biasing near pressure sensor.",
            "flow": "Pressure sensor -> op amp/scale network -> SENSOR/PRESSURE net -> digital/analog interconnect. Confermato sulle pagine sopra; dettagli di pin/value vanno verificati sulle immagini.",
            "symptoms": "Aftertouch non lineare, pressione sempre alta/bassa, CV contaminato, reset/rumore se ground/rail condivisi hanno problemi.",
        },
        "sample_hold_cv.md": {
            "title": "Sample & Hold / CV Generation",
            "sources": [("pvs_service", 6), ("pvs_service", 7), ("pvs_service", 8), ("pvs_service", 9), ("5530", 1), ("5530", 3), ("5530", 4), ("5508", 1), ("5508", 3)],
            "components": "U449/U425 CEM5530, DAC/U451 6012, U453/U454 HC174, U405 HC174, 4051/logic shown on later analog pages, PD508/CEM5530 datasheet concepts.",
            "rails": "+12V, -12V, +8V, +5.6V, -5V, +5VD, VDD/VSS/VREF.",
            "flow": "Digital data/address/timing -> DAC/reference -> CEM5530 input/inhibit/address -> held CV outputs such as VCA, VCF, PAN, LEV, chorus/final CV.",
            "symptoms": "CV droop, modulation leak, VCA not closing, pan/level drift, distorted control voltages, output bleed with volume low.",
        },
        "audio_path.md": {
            "title": "Audio Path / VCA / VCF / Output",
            "sources": [("pvs_service", 6), ("pvs_service", 9), ("pvs_service", 11), ("pvs_service", 12)],
            "components": "VCF/VCA/PAN/LEV CV outputs, op amps on audio pages, left/right voice/output sections, 7 kHz lowpass section.",
            "rails": "+12V, -12V, AGND and any local analog rails shown on the page images.",
            "flow": "Voice/filter/VCA stages -> pan/left/right routing -> chorus/output/filter stages. CV from S&H controls VCA/VCF/PAN/LEV.",
            "symptoms": "Bleed with volume at zero can come from VCA control leakage, audio coupling after volume, output/chorus leakage, op amp bias issues, rail ripple, or bad ground.",
        },
        "power_reset.md": {
            "title": "Power / Reset",
            "sources": [("pvs_service", 3), ("pvs_service", 4), ("pvs_service", 6), ("sci_prophet_vs_ecr739", 4), ("5530", 3)],
            "components": "U301 7805, U302 7812, U303 7912, U304 78L05, U401 7905, U402 78M05, U450 78M08, reset gates U305/HC132, transformer/rectifier area.",
            "rails": "+5VD, +12V, -12V, +8V, +5.6V, -5V, AGND/DGND.",
            "flow": "Transformer/rectifiers/regulators generate digital and analog rails; reset logic depends on supply behavior.",
            "symptoms": "Low/rippled rails can cause distortion, CV error, digital mis-refresh, reset instability, heat, or audio hum/bleed.",
        },
        "keyboard_matrix.md": {
            "title": "Keyboard Matrix / Controls",
            "sources": [("pvs_service", 1), ("pvs_service", 2), ("pvs_service", 4), ("sci_prophet_vs_ecr739", 4)],
            "components": "Keyboard matrix contacts, front panel switches S2xx/S6xx/S7xx, HC logic, ADC/front panel controls, pressure sensor.",
            "rails": "+5VD, DGND and pressure circuit analog references.",
            "flow": "Switch/contact matrix and panel controls feed digital logic/ADC; pressure path is partly analog and shares board interconnects.",
            "symptoms": "Stuck controls, false pressure, panel CV contamination, keyboard scan faults, intermittent connectors.",
        },
        "chorus.md": {
            "title": "Chorus / Output Control",
            "sources": [("pvs_service", 2), ("pvs_service", 6), ("pvs_service", 9), ("pvs_service", 11), ("pvs_service", 12)],
            "components": "LEFT CHORUS CV, RIGHT CHORUS CV, chorus LEDs/status, left/right output pages, op amps and filters on C9xx/R9xx pages.",
            "rails": "+12V, -12V, +5VD for control, AGND.",
            "flow": "Front panel/status/control lines enable chorus; analog audio path routes left/right through chorus/output/filter sections.",
            "symptoms": "Distorted self-sound, channel imbalance, bleed after volume, chorus stuck on/off, noisy output.",
        },
    }
    for filename, data in maps.items():
        links = "\n".join(f"- {link_to_page_note(s, p, prefix='../')}" for s, p in data["sources"])
        body = f"""# {data['title']}

## Ruolo nel Prophet VS
Mappa di lavoro per diagnosi e lettura incrociata. Le affermazioni sotto derivano dalle pagine/sorgenti linkate.

## Pagine/sorgenti
{links}

## Componenti importanti
{data['components']}

## Rail importanti
{data['rails']}

## Flusso del segnale, per quanto leggibile
{data['flow']}

## Cosa puo andare storto
- Op amp o IC guasto, condensatore in perdita, saldatura crepata, via/pista danneggiata, connettore ossidato.
- Rail basso/con ripple o ground analogico/digitale disturbato.
- Valori ECR errati, jumper/tagli non documentati o riparazioni precedenti malfatte.

## Come potrebbe collegarsi ai sintomi
{data['symptoms']}

## Cose da misurare in sicurezza
- Verificare concettualmente i rail indicati nelle pagine sorgente prima di inseguire segnali piccoli.
- Confrontare ground analogico/digitale solo come da schema e senza creare corti accidentali.
- Osservare uscite/ingressi etichettati nelle pagine linkate con strumenti adeguati e massa corretta.
- Nelle aree mains/trasformatore, operare solo con tecnico qualificato e isolamento appropriato.

## Cose da non assumere
- Non assumere che le modifiche ECR738/ECR739 siano presenti sullo strumento reale.
- Non assumere valori OCR se l'immagine non li conferma chiaramente.
- Non sostituire componenti per somiglianza del sintomo senza prova elettrica o ispezione fisica.
"""
        (ctx_root() / "circuit_maps" / filename).write_text(body, encoding="utf-8")


def make_ecr_map() -> None:
    body = f"""# Board Revisions / ECR738 / ECR739

## Ruolo nel Prophet VS
Questa mappa confronta gli engineering change records scannerizzati. Non assumere che il Prophet VS reale abbia una di queste modifiche: va verificato sulla board.

## Pagine/sorgenti
- {link_to_page_note("sci_prophet_vs_ecr738", 1, prefix="../")}
- {link_to_page_note("sci_prophet_vs_ecr738", 2, prefix="../")}
- {link_to_page_note("sci_prophet_vs_ecr738", 3, prefix="../")}
- {link_to_page_note("sci_prophet_vs_ecr739", 1, prefix="../")}
- {link_to_page_note("sci_prophet_vs_ecr739", 4, prefix="../")}
- {link_to_page_note("pvs_service", 4, prefix="../")}
- {link_to_page_note("pvs_service", 6, prefix="../")}

## ECR738
Motivo dichiarato della modifica: [NON CHIARO] nella scansione/OCR della pagina 1. La pagina 2 mostra una modifica nell'area pressure sensor / sample & hold sensor.

Componenti/piste visibili:
- PRESSURE SENSOR, U459, R458, +12V, -12V, C4148/C4147 circa, P402/SENSOR/DGND sono visibili o inferibili dall'immagine ECR738 pagina 2.
- R458 appare annotata come 15K; nell'immagine e' anche visibile una rete con +12V e valori manoscritti, incluso 6.8K e 1K vicino al nodo pressure. Verificare sull'immagine e sulla board.

Perche puo essere importante:
- Cambiare resistenze o bias nel pressure sensor puo alterare offset, range e saturazione dell'aftertouch.
- Una modifica errata puo far arrivare CV fuori scala, contaminare letture o creare sintomi intermittenti se jumper/tagli sono fragili.

Cosa verificare fisicamente:
- Revisione board e presenza di tagli piste/jumper nella zona pressure sensor.
- Valore reale di R458 e delle resistenze annotate vicino a +12V.
- Qualita saldature, piste sollevate, flussante/ossidazione e continuita verso P402/SENSOR/DGND.

## ECR739
Motivo dichiarato della modifica: [NON CHIARO] nelle pagine 1-3. La pagina 4 mostra chiaramente pressure circuit, keyboard/power supply e reset/power rails.

Componenti/piste visibili:
- R321 OFFSET 50K, R307 20K, R308 10K, R309 47K, R320 10K, R304 15K, R305 470K, U310 op amp, U305 HC132, U301 7805, U302 7812, U303 7912, U304 78L05.
- TP301/TP302, SENSOR, PRESSURE, +5VD, +12V, -12V, DGND, AGND sono leggibili sulla pagina 4.

Confronto con ECR738:
- Entrambi toccano il pressure/aftertouch path, ma ECR738 e' mostrato sul lato main analog/sample & hold sensor, mentre ECR739 e' mostrato sul lato digital/keyboard/power supply.
- Rete, connettori e nomi net non vanno fusi automaticamente: confrontare le pagine ECR con pvs_service pagine 4 e 6.

## Checklist verifica ECR
- Revisione board stampata/silkscreen corrisponde ai documenti?
- Ci sono piste tagliate? Sono pulite e isolate?
- Ci sono jumper aggiunti? Sono meccanicamente stabili?
- Valori resistenze corrispondono alle annotazioni ECR e allo schema di servizio?
- Le saldature nella zona pressure sensor/regolatori sono lucide e non sollevano pad?
- Il routing fisico corrisponde all'artwork scannerizzato?
- I rail +5VD, +12V, -12V, +8V/+5.6V/-5V sono presenti prima di interpretare il segnale pressure?
"""
    (ctx_root() / "circuit_maps" / "board_revisions_ecr.md").write_text(body, encoding="utf-8")


SYMPTOMS = {
    "symptom_audio_at_volume_zero.md": {
        "name": "Prophet VS emette suono / bleed distorto anche con volume a zero",
        "desc": "Suono o bleed distorto resta udibile a volume zero; in alcune patch sembra passare LFO/modulazione anche con volume a zero.",
        "areas": "VCA/VCF/PAN/LEV CV, audio path dopo volume, chorus/output, S&H CEM5530, rail analogici, ground, riparazioni precedenti.",
        "sources": [("pvs_service", 6), ("pvs_service", 9), ("pvs_service", 11), ("pvs_service", 12), ("5530", 1), ("5530", 3), ("5530", 4)],
        "causes": [
            "Leakage controllo VCA o CV VCA non torna a valore di chiusura.",
            "Audio path che bypassa o si accoppia dopo il volume control.",
            "Chorus/output op amp o filtro finale che distorce o inietta segnale.",
            "CEM5530/S&H con droop, hold step o timing INH/address errato.",
            "Ripple/rail analogici o ground AGND/DGND problematici.",
            "Riparazione precedente, pista sollevata, connettore o jack difettoso.",
            "Contaminazione CV da pannello/controlli o pressure sensor.",
        ],
    },
    "symptom_distorted_self_sound.md": {
        "name": "Suono proprio distorto",
        "desc": "Il timbro del Prophet VS risulta distorto o instabile anche senza input esterni.",
        "areas": "Audio path, VCA/VCF, chorus/output, rail analogici, CV sample & hold.",
        "sources": [("pvs_service", 6), ("pvs_service", 9), ("pvs_service", 11), ("pvs_service", 12)],
        "causes": ["Rail analogici fuori tolleranza", "Op amp o filtro output guasto", "VCA/VCF pilotati da CV errato", "Condensatori audio in perdita", "Ground o connettori intermittenti"],
    },
    "symptom_aftertouch_pressure_fault.md": {
        "name": "Aftertouch / pressure fault",
        "desc": "Pressure assente, sempre attiva, non lineare o rumorosa.",
        "areas": "Pressure sensor, U310/U459, reti R321/R458/R304/R320, ECR738/ECR739, alimentazione.",
        "sources": [("pvs_service", 4), ("pvs_service", 6), ("sci_prophet_vs_ecr738", 2), ("sci_prophet_vs_ecr739", 4)],
        "causes": ["Valori ECR non corrispondenti", "Op amp pressure guasto", "Offset/range fuori taratura", "Connettore pressure ossidato", "Rail/ground instabili"],
    },
    "symptom_overheating_component.md": {
        "name": "Componente che scalda",
        "desc": "Un regolatore, op amp, IC logico o resistenza scalda in modo anomalo.",
        "areas": "Power supply, regolatori locali, analog board, riparazioni fisiche.",
        "sources": [("pvs_service", 4), ("pvs_service", 6), ("sci_prophet_vs_ecr739", 4)],
        "causes": ["Corto a valle", "Condensatore in perdita", "Regolatore sovraccarico", "IC guasto", "Jumper/pista errata dopo riparazione"],
    },
    "symptom_cv_bleed_or_modulation_leak.md": {
        "name": "CV bleed o modulation leak",
        "desc": "LFO/modulazione o livelli CV sembrano entrare dove non dovrebbero.",
        "areas": "CEM5530/PD508 S&H, DAC/reference, VCA/VCF/PAN/LEV, ground analogico.",
        "sources": [("pvs_service", 6), ("pvs_service", 9), ("5530", 1), ("5530", 4), ("5508", 3)],
        "causes": ["Droop/hold step S&H", "Timing INH/address errato", "Op amp buffer guasto", "Rail/reference rumoroso", "Leakage switch o condensatore"],
    },
    "symptom_power_rail_problem.md": {
        "name": "Power rail problem",
        "desc": "Sintomi multipli, reset, distorsione, rumore o instabilita che suggeriscono alimentazione.",
        "areas": "7805/7812/7912/78L05/78M08/78M05/7905, rettificatori, condensatori, AGND/DGND.",
        "sources": [("pvs_service", 4), ("pvs_service", 6), ("sci_prophet_vs_ecr739", 4), ("5530", 3)],
        "causes": ["Ripple eccessivo", "Regolatore guasto", "Condensatore elettrolitico/tantalio in perdita", "Ground aperto o sporco", "Carico eccessivo a valle"],
    },
}


def make_symptom_file(filename: str, data: dict[str, object]) -> None:
    sources = "\n".join(f"- {link_to_page_note(s, p, prefix='../')}" for s, p in data["sources"])  # type: ignore[index]
    causes = "\n".join(f"{idx}. {cause}" for idx, cause in enumerate(data["causes"], start=1))  # type: ignore[index]
    body = f"""# Sintomo: {data['name']}

## Descrizione sintomo
{data['desc']}

## Aree circuito piu rilevanti
{data['areas']}

## Pagine sorgente da ispezionare
{sources}

## Possibili cause ordinate dalla piu probabile alla meno probabile
{causes}

## Quale evidenza supporterebbe ogni causa
- Il sintomo cambia quando si osservano/isolano concettualmente le aree circuito indicate nelle pagine sorgente.
- Le misure mostrano rail, CV o audio fuori range rispetto alle etichette presenti nello schema.
- Ispezione visiva trova saldature, jumper, piste o componenti nella stessa zona delle pagine linkate.

## Quale evidenza la escluderebbe
- Rail e ground stabili, nessun ripple anomalo, e segnale/CV corretto prima e dopo il blocco sospetto.
- Il difetto resta invariato dopo esclusione documentata del blocco indicato.
- Continuita e componenti fisici corrispondono agli schemi/ECR.

## Misure/controlli da eseguire
- Prima controllare rail principali e locali indicati nelle page note.
- Poi osservare segnali etichettati nella pagina sorgente con massa corretta e strumenti adatti.
- Confrontare comportamento statico e dinamico: valore DC, ripple, risposta a patch/controlli, eventuale modulazione residua.

## Aree scheda/componenti da ispezionare visivamente
- Connettori citati nelle page note.
- Zone ECR e riparazioni precedenti, soprattutto tagli piste/jumper.
- Regolatori, op amp, CEM5530/S&H, condensatori tantalio/elettrolitici e jack/output.

## Rischi / cautele
- Non operare su mains/trasformatore senza tecnico qualificato.
- Evitare corti con puntali; vecchie PCB possono sollevare pad con calore o forza.
- Non sostituire parti rare senza prova; alcuni IC possono essere difficili da reperire.

## Domande per un tecnico
- Il difetto cambia tra uscita left/right, cuffie/line out o chorus on/off?
- Il bleed segue VCA/VCF/PAN/LEV o resta nel percorso audio finale?
- I rail locali e reference sono stabili a freddo/caldo?
- La board mostra ECR738/ECR739 applicati, parziali o assenti?
"""
    (ctx_root() / "diagnostic_notes" / filename).write_text(body, encoding="utf-8")


def make_diagnostics() -> None:
    readme = """# Diagnostic notes

Queste note sono un albero di ipotesi, non una diagnosi certa. Ogni ipotesi rimanda alle pagine sorgente generate in questa knowledge base. Partire da `symptom_audio_at_volume_zero.md` se il problema principale e' bleed/distorsione a volume zero.
"""
    (ctx_root() / "diagnostic_notes" / "README.md").write_text(readme, encoding="utf-8")
    for filename, data in SYMPTOMS.items():
        make_symptom_file(filename, data)
    visual = """# Visual inspection checklist

## Prima di alimentare
- Cercare componenti anneriti, crepati, montati al contrario o con valore non coerente con le ECR.
- Cercare pad sollevati, piste tagliate, jumper volanti, fili stressati e saldature fredde.
- Ispezionare connettori P/J/TB citati nelle page note e jack/output.
- Verificare zone pressure sensor, regolatori, main analog S&H e audio output.

## Dopo confronto con documenti
- Confrontare board revision con ECR738/ECR739.
- Verificare R458, R321, R307/R308/R309/R320/R304 solo con riferimento immagine e misura fisica.
- Marcare ogni punto non leggibile come [NON CHIARO], non indovinare.
"""
    (ctx_root() / "diagnostic_notes" / "visual_inspection_checklist.md").write_text(visual, encoding="utf-8")
    safe = """# Safe measurement plan

## Ordine consigliato
1. Ispezione visiva a strumento spento.
2. Verifica concettuale di ground e assenza di corti evidenti.
3. Misura rail a basso rischio: +5VD, +12V, -12V, +8V, +5.6V, -5V dove indicati dagli schemi.
4. Solo dopo rail stabili, osservare SENSOR/PRESSURE, VCA/VCF/PAN/LEV e output audio.

## Cautele
- Mains/trasformatore: tecnico qualificato.
- Usare puntali sicuri e massa corretta; evitare corti tra pin adiacenti.
- Non usare forza su vecchi connettori o pad.
- Non dissaldare componenti rari prima di avere evidenza.
"""
    (ctx_root() / "diagnostic_notes" / "safe_measurement_plan.md").write_text(safe, encoding="utf-8")


def make_readme() -> None:
    body = """# Prophet VS service context

Questa cartella contiene una knowledge base locale generata dai PDF scannerizzati in `doc/`, senza modificare i PDF originali.

## Come e' stata creata
- `scripts/extract_pdf_pages.py` renderizza ogni pagina come PNG in `page_images/`.
- PyMuPDF/fitz non era disponibile in questo ambiente; lo script ha usato fallback locale macOS CUPS + `rastertotiff` + Pillow a 300 DPI.
- `scripts/extract_text_and_ocr.py` tenta testo nativo e poi OCR locale con Tesseract.
- `scripts/generate_markdown_kb.py` genera note pagina, indici, mappe circuito, indici componenti e note diagnostiche.

## Affidabilita OCR
OCR medio su datasheet e molte pagine schematiche; basso o incerto su alcune ECR/artwork. Ogni file pagina riporta `METHOD` e `CONFIDENCE`. Se un valore non e' chiaro, e' trattato come [NON CHIARO].

## Come navigare
- Inizia da `index.md` per argomento.
- Usa `source_files.md` per capire i PDF.
- Usa `page_notes/` per pagina specifica.
- Usa `circuit_maps/` per ragionare su pressure, S&H, audio, power/reset, keyboard e ECR.
- Usa `diagnostic_notes/` per partire dai sintomi.

## Da dove partire per riparazione
- Bleed/distorsione a volume zero: `diagnostic_notes/symptom_audio_at_volume_zero.md`, poi `circuit_maps/audio_path.md` e `circuit_maps/sample_hold_cv.md`.
- Pressure/aftertouch: `circuit_maps/pressure_aftertouch.md` e `circuit_maps/board_revisions_ecr.md`.
- Alimentazione: `circuit_maps/power_reset.md`.

## Avvisi
- Non sostituisce un tecnico synth qualificato.
- Sezioni alimentazione/mains possono essere pericolose.
- Vecchie PCB possono danneggiarsi con calore eccessivo, forza, puntali sbagliati o corti durante le misure.
"""
    (ctx_root() / "README.md").write_text(body, encoding="utf-8")


def main() -> int:
    ensure_dirs()
    make_page_notes()
    make_source_files()
    make_index()
    make_component_index()
    make_circuit_maps()
    make_ecr_map()
    make_diagnostics()
    make_readme()
    print("Knowledge base Markdown generata.")
    print("Punti di partenza: README.md, index.md, diagnostic_notes/symptom_audio_at_volume_zero.md, circuit_maps/board_revisions_ecr.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
