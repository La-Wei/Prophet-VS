# Prophet VS service context

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
