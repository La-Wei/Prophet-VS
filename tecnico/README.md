# Pacchetto tecnico pulito

Questa cartella e' pensata per un tecnico che deve diagnosticare un Sequential Circuits Prophet VS con due problemi da tenere separati finche le misure non li collegano:

- audio/modulazione/bleed che passa anche con volume a zero
- case posteriore molto caldo nella zona dei tre regolatori TO-220 fissati al dissipatore

## Da aprire per primi

1. `01_problemi_e_fix/cause_e_fix.md`
2. `01_problemi_e_fix/technician_briefing_volume_zero_bleed.md`
3. `01_problemi_e_fix/quick_navigation_map.md`
4. `01_problemi_e_fix/cem5530_diagnosi_ricambi.md`
5. `07_autocostruzione_ricambi/cem5530_clone_build_dossier.md`
6. `07_autocostruzione_ricambi/max5167_v2_like_pre_design.md`
7. `07_autocostruzione_ricambi/rev_a_max5167_prototipo/README.md`
8. `07_autocostruzione_ricambi/straylight_x5530_moduli_trovati.md`
9. `07_autocostruzione_ricambi/contatti_acquisto_eld5530_cem5530.md`
10. `01_problemi_e_fix/batteria_memoria_nvram.md`
11. `01_problemi_e_fix/jack_sostituzione.md`
12. `01_problemi_e_fix/pannello_posteriore_ricambi.md`
13. `02_checklist_misure/visual_inspection_checklist.md`
14. `02_checklist_misure/safe_measurement_plan.md`

## Identificazione regolatori nella foto

La foto `foto/IMG_5543.jpg` mostra la board `PC2400-3 REV B` con tre TO-220 fissati al case/dissipatore. Dai documenti sono regolatori lineari:

- sinistra: `U301 7805`, rail `+5VD`
- centro: `U302 7812`, rail `+12V`
- destra: `U303 7912`, rail `-12V`

L'ordine sinistra->destra deriva dalla designator map `pvs_service` pagina 5; confermare sulla serigrafia reale se visibile.

## Struttura

- `01_problemi_e_fix/`: cause, fix, briefing e mappa rapida.
- `02_checklist_misure/`: controlli visivi e piano misure sicure.
- `03_mappe_circuito/`: mappe brevi per audio, S&H/CV, power/reset, pressure, ECR e chorus.
- `04_componenti_net_rail/`: indici componenti, rail, net e connettori utili.
- `05_pagine_rilevanti/`: note e immagini delle sole pagine utili.
- `06_pdf_originali/`: PDF sorgenti principali.
- `07_autocostruzione_ricambi/`: dossier per valutare cloni/ricostruzione di ricambi non reperibili e prototipo Rev A `MAX5167`.
- `foto/`: foto utente dell'area regolatori.

PDF inclusi in `06_pdf_originali/`: `pvs_service.pdf`, `sci_prophet_vs_ecr738.pdf`, `sci_prophet_vs_ecr739.pdf`, `5530.pdf`, `5508.pdf`. La sottocartella `06_pdf_originali/component_datasheets/` contiene link ai datasheet esterni `MAX5167` e `SSM2300`.

## Escluso apposta

Non ci sono prompt, OCR grezzo, script di estrazione, manifest JSON, cache o pagine non citate. La knowledge base completa resta in `doc/prophet_vs_service_context/` se serve tornare al materiale grezzo.
