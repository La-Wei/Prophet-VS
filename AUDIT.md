# Audit repository

Data audit: 2026-05-02

## Esito rapido

- `5508.pdf` copiato in `tecnico/06_pdf_originali/5508.pdf`.
- Aggiunto dossier `CEM5530/ELD5530` per clone/ricostruzione in `tecnico/07_autocostruzione_ricambi/`.
- Aggiunto progetto preliminare `ELD5530 V2-like` basato su `MAX5167`, con pin mapping, rail locali, vincoli PCB e piano test.
- Aggiunta cartella `rev_a_max5167_prototipo/` con schema testuale, netlist CSV, BOM funzionale, vincoli PCB, collaudo e handoff CAD. E' marcata come prototipo non validato.
- Aggiunto progetto KiCad iniziale in `tecnico/07_autocostruzione_ricambi/rev_a_max5167_prototipo/cad_kicad/`.
- Aggiunta nota `batteria_memoria_nvram.md`: `ELD5530` non elimina la batteria; solo una mod SRAM non volatile puo' farlo.
- Correzione ELD5530 da fonte primaria Synthelectro 2014: V2 confermata su IC Maxim Integrated, ma `MAX5167` resta ipotesi tecnica non BOM ufficiale.
- Aggiunto file `contatti_acquisto_eld5530_cem5530.md` con destinatari e email inglesi per cercare 2 moduli.
- Aggiunta nota `straylight_x5530_moduli_trovati.md`: i due moduli in foto sembrano Straylight `X5530`, cloni/ricambi `CEM5530` basati su 4 x `SMP18`.
- Chiarito che i dissipatori consigliati sono per `CEM5530` originali; sui cloni `X5530` non vanno aggiunti senza misura o istruzione Straylight.
- Aggiunti link datasheet esterni `MAX5167` e `SSM2300` in `tecnico/06_pdf_originali/component_datasheets/README.md`.
- Link Markdown controllati: 364 link locali controllati, 0 rotti su 109 file Markdown.
- Pacchetto tecnico controllato: non contiene prompt, script, OCR grezzo, manifest JSON o cache.
- Vecchia cartella `doc/prophet_vs_technician_package/`: assente.
- Cartella consegnabile: `tecnico/`.
- Knowledge base completa: `doc/prophet_vs_service_context/`.

## Struttura attuale

- `README.md`: guida principale in root.
- `AUDIT.md`: questo report.
- `tecnico/`: materiale pulito per il tecnico.
- `doc/`: PDF originali e knowledge base completa/generata.
- `prompt/`: prompt di lavoro.

## Pacchetto tecnico

File principali da aprire:

1. `tecnico/01_problemi_e_fix/cause_e_fix.md`
2. `tecnico/01_problemi_e_fix/technician_briefing_volume_zero_bleed.md`
3. `tecnico/01_problemi_e_fix/quick_navigation_map.md`
4. `tecnico/01_problemi_e_fix/cem5530_diagnosi_ricambi.md`
5. `tecnico/07_autocostruzione_ricambi/cem5530_clone_build_dossier.md`
6. `tecnico/07_autocostruzione_ricambi/max5167_v2_like_pre_design.md`
7. `tecnico/07_autocostruzione_ricambi/rev_a_max5167_prototipo/README.md`
8. `tecnico/07_autocostruzione_ricambi/straylight_x5530_moduli_trovati.md`
9. `tecnico/07_autocostruzione_ricambi/contatti_acquisto_eld5530_cem5530.md`
10. `tecnico/01_problemi_e_fix/batteria_memoria_nvram.md`
11. `tecnico/01_problemi_e_fix/jack_sostituzione.md`
12. `tecnico/01_problemi_e_fix/pannello_posteriore_ricambi.md`
13. `tecnico/02_checklist_misure/visual_inspection_checklist.md`
14. `tecnico/02_checklist_misure/safe_measurement_plan.md`

PDF inclusi:

- `tecnico/06_pdf_originali/pvs_service.pdf`
- `tecnico/06_pdf_originali/sci_prophet_vs_ecr738.pdf`
- `tecnico/06_pdf_originali/sci_prophet_vs_ecr739.pdf`
- `tecnico/06_pdf_originali/5530.pdf`
- `tecnico/06_pdf_originali/5508.pdf`

Link datasheet esterni utili:

- `tecnico/06_pdf_originali/component_datasheets/README.md`
- `MAX5167-MAX5167N` Analog Devices
- `SSM2300` Analog Devices

## Controlli effettuati

- Validazione link Markdown su tutti i `.md` della repo: nessun link mancante.
- Ricerca percorsi obsoleti nel pacchetto tecnico: nessun riferimento a `doc/prophet_vs_technician_package`.
- Ricerca contenuti da escludere in `tecnico/`: nessun `prompt/`, `scripts/`, `extracted_text/`, `manifest*.json`.
- Dimensione indicativa: `tecnico/` circa 11M; `doc/prophet_vs_service_context/` circa 17M.

## Note residue

- `.DS_Store` era presente in root come file di sistema macOS. Aggiunto `.gitignore` per evitarne il tracking futuro; il file fisico non e' stato cancellato.
- `IMG_5543.jpg` resta sia in root sia in `tecnico/foto/IMG_5543.jpg`: la copia in `tecnico/` serve al pacchetto consegnabile, quella in root e' il sorgente originale dell'utente.
- Non sono stati trovati Gerber/schema/BOM pubblici e verificabili per `ELD5530`: il dossier documenta questa assenza. La pre-progettazione `MAX5167` e la cartella Rev A portano avanti la soluzione piu probabile, ma restano da verificare al banco prima di qualsiasi produzione o installazione.
