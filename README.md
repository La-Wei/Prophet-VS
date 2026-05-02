# Prophet VS - diagnosi riparazione

Questa repository contiene materiale preparato per aiutare un tecnico a diagnosticare due problemi separati sul Sequential Circuits Prophet VS:

- audio/modulazione/bleed che passa anche con volume a zero
- retro case molto caldo nella zona dei tre regolatori TO-220

## Apri prima questi file

1. [Cause possibili e fix](tecnico/01_problemi_e_fix/cause_e_fix.md)
2. [Briefing tecnico](tecnico/01_problemi_e_fix/technician_briefing_volume_zero_bleed.md)
3. [Mappa rapida](tecnico/01_problemi_e_fix/quick_navigation_map.md)
4. [CEM5530: diagnosi e ricambi](tecnico/01_problemi_e_fix/cem5530_diagnosi_ricambi.md)
5. [CEM5530/ELD5530: dossier clone o ricostruzione](tecnico/07_autocostruzione_ricambi/cem5530_clone_build_dossier.md)
6. [Jack posteriori](tecnico/01_problemi_e_fix/jack_sostituzione.md)
7. [Ricambi pannello posteriore](tecnico/01_problemi_e_fix/pannello_posteriore_ricambi.md)
8. [Checklist ispezione](tecnico/02_checklist_misure/visual_inspection_checklist.md)
9. [Piano misure sicure](tecnico/02_checklist_misure/safe_measurement_plan.md)

## Cartelle

- `tecnico/`: pacchetto pulito da consegnare al tecnico.
- `doc/`: PDF originali e knowledge base completa usata per estrarre note e immagini.
- `prompt/`: prompt di lavoro usati per generare la documentazione.

## PDF nel pacchetto tecnico

La cartella `tecnico/06_pdf_originali/` contiene:

- `pvs_service.pdf`
- `sci_prophet_vs_ecr738.pdf`
- `sci_prophet_vs_ecr739.pdf`
- `5530.pdf`
- `5508.pdf`

La sottocartella `tecnico/06_pdf_originali/component_datasheets/` contiene link ai datasheet esterni `MAX5167` e `SSM2300` utili per valutare cloni `CEM5530`.

## Regolatori nella foto

Nella foto `tecnico/foto/IMG_5543.jpg`, i tre TO-220 fissati al case/dissipatore sono regolatori lineari:

- sinistra: `U301 7805`, rail `+5VD`
- centro: `U302 7812`, rail `+12V`
- destra: `U303 7912`, rail `-12V`

Il regolatore caldo non va considerato automaticamente guasto: e' gia' stato sostituito con uno piu capiente. La priorita' e' misurare rail, ripple, Vin/Vout, temperatura e carico a valle.
