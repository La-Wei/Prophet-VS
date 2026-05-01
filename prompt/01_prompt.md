Stai lavorando su un workspace locale e privato per ricerca/riparazione di un Sequential Circuits Prophet VS.

Obiettivo:
Trasformare i PDF/documenti scannerizzati di servizio in una knowledge base tecnica strutturata e leggibile, così che un altro agente di codice/analisi possa usarla più avanti per ragionare su possibili guasti, comportamento dei circuiti, posizione dei componenti, revisioni delle schede e passi diagnostici.

Importante:
- Non modificare i PDF originali.
- Non cancellare nulla.
- I documenti sorgente sono dentro la cartella: doc/
- Lavora solo dentro una nuova sottocartella: doc/prophet_vs_service_context/
- Questi PDF sono quasi tutti scansioni/immagini, quindi l’estrazione normale del testo potrebbe essere incompleta o vuota.
- Preferisci script riproducibili e file Markdown generati, invece di note manuali sparse.
- Sii molto esplicito sull’incertezza. Se l’OCR non è chiaro, marca il punto come [NON CHIARO] invece di indovinare.
- L’output finale deve essere utile anche senza riaprire i PDF originali.
- Non usare servizi remoti, API esterne o upload online. Tutto deve rimanere locale.

File sorgente:
- doc/sci_prophet_vs_ecr738.pdf
- doc/sci_prophet_vs_ecr739.pdf
- doc/pvs_service.pdf
- doc/5508.pdf
- doc/5530.pdf

Contesto:
Lo strumento è un Sequential Circuits Prophet VS. L’utente vuole indagare possibili problemi di riparazione, tra cui audio distorto o bleed con volume a zero, possibile contaminazione di CV/controlli, comportamento del circuito pressure/aftertouch, problemi sample & hold, revisioni scheda, riparazioni fatte male, piste sollevate, componenti che scaldano, problemi di alimentazione e percorsi diagnostici generali.

Task:

1. Crea struttura cartelle

Crea:

doc/prophet_vs_service_context/
  README.md
  index.md
  source_files.md
  extracted_text/
  page_images/
  page_notes/
  circuit_maps/
  diagnostic_notes/
  component_index/
  scripts/

2. Estrai ogni pagina PDF come immagine ad alta risoluzione

Scrivi uno script:

doc/prophet_vs_service_context/scripts/extract_pdf_pages.py

Usa Python.
Usa PyMuPDF/fitz se disponibile. Se non è disponibile, documenta la dipendenza mancante e fornisci istruzioni di installazione.

Per ogni PDF:
- renderizza ogni pagina ad alta risoluzione, circa 300 DPI se pratico
- salva PNG in:
  doc/prophet_vs_service_context/page_images/<nome_pdf_senza_estensione>/page_001.png
- crea un manifest JSON con:
  - nome PDF sorgente
  - numero pagine
  - percorsi immagini generate
  - dimensioni immagini
  - timestamp estrazione

3. Estrai testo / OCR dove possibile

Scrivi lo script:

doc/prophet_vs_service_context/scripts/extract_text_and_ocr.py

Prima prova l’estrazione testo nativa dal PDF.
Se il testo estratto è vuoto o quasi vuoto, prova OCR solo se esiste uno strumento OCR locale disponibile.
Non usare servizi remoti.
Se l’OCR non è disponibile, crea file placeholder che dicano che l’OCR non è disponibile e indicano il percorso dell’immagine pagina.

Per ogni pagina crea:

doc/prophet_vs_service_context/extracted_text/<nome_pdf>/page_001.txt

Formato file:

SOURCE: <pdf>
PAGE: <n>
METHOD: native_text | ocr | unavailable
CONFIDENCE: high | medium | low | unavailable

CONTENT:
...

4. Crea note tecniche per ogni pagina

Per ogni pagina crea:

doc/prophet_vs_service_context/page_notes/<nome_pdf>/page_001.md

Ogni nota deve includere:

# <nome PDF> pagina <n>

## Cosa sembra contenere questa pagina
Descrivi in italiano semplice se la pagina sembra essere:
- schema elettrico
- artwork PCB
- datasheet
- ECR / engineering change record
- BOM / lista modifiche
- layout
- pressure circuit
- sample & hold
- chorus
- keyboard matrix
- alimentazione
- cartridge board
- generazione waveform
- ecc.

## Etichette / componenti / IC / net visibili
Estrai tutto quello che è chiaramente leggibile:
- riferimenti IC: Uxxx
- resistenze/capacitori: Rxxx, Cxxx
- connettori: Pxxx, Jxxx
- rail: +5V, -5V, +12V, -12V, AGND, DGND
- net nominate: LEFT, RIGHT, PAN, LEV, VCA, VCF, PRESSURE, RESET, ecc.
- chip: CEM5530, PD508, 4051, TL08x, 7805, 7905, 5530, ecc.

## Riassunto funzione del circuito
Spiega cosa probabilmente fa il circuito, separando:
- Confermato dalle etichette
- Inferenza ragionevole
- Incerto / da verificare manualmente

## Rilevanza per riparazione
Elenca perché questa pagina è utile per diagnosticare un Prophet VS.

## Possibili failure mode collegati a questa pagina
Elenca solo guasti elettronici plausibili. Esempi:
- op amp guasto
- condensatore in perdita
- regolatore guasto
- saldatura crepata
- via/pista danneggiata
- sample & hold IC guasto
- problema rete resistiva pressure sensor
- ossidazione connettore
- problema ground analogico/digitale
- rail alimentazione basso o con ripple
- CV bleed da sample & hold droop
- valore resistenza ECR errato
- circuito keyboard/pressure danneggiato

## Cross-reference
Collega pagine correlate di altri PDF se evidente.

5. Crea source_files.md

Riassumi lo scopo di ogni PDF sorgente:

- doc/sci_prophet_vs_ecr738.pdf:
  ECR 738, engineering change record Sequential. Sembra relativo a Prophet VS PCB 2400 board 4 / circuito main analog sample & hold / sensor e modifiche resistenze pressure sensor.

- doc/sci_prophet_vs_ecr739.pdf:
  ECR 739, engineering change record Sequential. Sembra relativo a Prophet VS PCB 2400 board 3 / keyboard and power supply / pressure circuit changes.

- doc/pvs_service.pdf:
  Pacchetto schemi Prophet VS, inclusi keyboard matrix, pressure circuit, sample & hold/sensor, wave circuits, chorus, cartridge board, artwork/layout schede.

- doc/5508.pdf:
  Datasheet OnChip Systems PD508 Octal Sample & Hold.

- doc/5530.pdf:
  Datasheet preliminare CEM5530 30-channel Sample & Hold.

Marca ogni riassunto come basato sul materiale scannerizzato visibile e non garantito completo.

6. Crea index.md

Crea un indice navigabile raggruppato per argomento:

## Pressure / aftertouch circuit
Linka tutte le pagine rilevanti da:
- ECR738
- ECR739
- pvs_service
- eventuali sezioni datasheet utili a capire comportamento S&H/tensioni

## Sample & Hold / generazione CV
Linka:
- datasheet PD508
- datasheet CEM5530
- pagine schematiche Prophet VS che mostrano S&H, LEV, PAN, VCF, VCA, WAVE A-D, ecc.

## Audio path / VCA / filtri / chorus
Linka tutte le pagine pvs_service che riguardano:
- chorus left/right
- filtri 7 kHz
- percorso uscita analogica
- controlli VCA/filtro se visibili

## Keyboard / pannello / controlli
Linka:
- keyboard matrix
- pressure sensor
- pagine ECR scannerizzate

## Alimentazione / rail
Linka tutte le pagine che mostrano:
- trasformatore
- regolatori 7805/7905
- +5V, -5V, +12V, -12V
- reset circuits
- ground analogico/digitale

## Board artwork / riparazione fisica
Linka pagine layout/artwork PCB dagli ECR e dal service PDF.

7. Crea indice componenti

Crea questi file Markdown:

doc/prophet_vs_service_context/component_index/ics.md
doc/prophet_vs_service_context/component_index/resistors_caps.md
doc/prophet_vs_service_context/component_index/connectors.md
doc/prophet_vs_service_context/component_index/power_rails.md
doc/prophet_vs_service_context/component_index/named_nets.md

Ogni file deve contenere una tabella:

| Riferimento / Net | Visto in pagina sorgente | Funzione / contesto | Note / incertezza |

Esempi:
| U459 | sci_prophet_vs_ecr738 pagina 2 | Op amp vicino al circuito pressure sensor | Visibile nello schema; verificare parte/valore esatto |
| R458 | sci_prophet_vs_ecr738 pagina 2 | Resistenza modificata in ECR 738 | ECR dice cambiata da 2K a 15K, verificare sulla board |
| CEM5530 | 5530.pdf pagine 1-4 | IC 30-channel sample & hold | Importante per generazione CV/droop/bleed |

8. Crea mappe circuitali

Crea:

doc/prophet_vs_service_context/circuit_maps/pressure_aftertouch.md
doc/prophet_vs_service_context/circuit_maps/sample_hold_cv.md
doc/prophet_vs_service_context/circuit_maps/audio_path.md
doc/prophet_vs_service_context/circuit_maps/power_reset.md
doc/prophet_vs_service_context/circuit_maps/keyboard_matrix.md
doc/prophet_vs_service_context/circuit_maps/chorus.md
doc/prophet_vs_service_context/circuit_maps/board_revisions_ecr.md

Ogni mappa circuito deve includere:

## Ruolo nel Prophet VS
## Pagine/sorgenti
## Componenti importanti
## Rail importanti
## Flusso del segnale, per quanto leggibile
## Cosa può andare storto
## Come potrebbe collegarsi ai sintomi
## Cose da misurare in sicurezza
## Cose da non assumere

Per “cose da misurare in sicurezza”, suggerisci test point concettuali, non procedure invasive precise, a meno che siano chiaramente mostrate nello schema.

9. Crea una knowledge base diagnostica

Crea:

doc/prophet_vs_service_context/diagnostic_notes/README.md
doc/prophet_vs_service_context/diagnostic_notes/symptom_audio_at_volume_zero.md
doc/prophet_vs_service_context/diagnostic_notes/symptom_distorted_self_sound.md
doc/prophet_vs_service_context/diagnostic_notes/symptom_aftertouch_pressure_fault.md
doc/prophet_vs_service_context/diagnostic_notes/symptom_overheating_component.md
doc/prophet_vs_service_context/diagnostic_notes/symptom_cv_bleed_or_modulation_leak.md
doc/prophet_vs_service_context/diagnostic_notes/symptom_power_rail_problem.md
doc/prophet_vs_service_context/diagnostic_notes/visual_inspection_checklist.md
doc/prophet_vs_service_context/diagnostic_notes/safe_measurement_plan.md

Per ogni file sintomo usa questa struttura:

# Sintomo: <nome>

## Descrizione sintomo
## Aree circuito più rilevanti
## Pagine sorgente da ispezionare
## Possibili cause ordinate dalla più probabile alla meno probabile
## Quale evidenza supporterebbe ogni causa
## Quale evidenza la escluderebbe
## Misure/controlli da eseguire
## Aree scheda/componenti da ispezionare visivamente
## Rischi / cautele
## Domande per un tecnico

Per questo sintomo specifico:
“Prophet VS emette suono / bleed distorto anche con volume a zero; in alcune patch sembra passare LFO/modulazione anche con volume a zero.”

Considera possibili aree:
- leakage controllo VCA
- audio path dopo il volume control
- sezione output/chorus
- uscite CV sample & hold che perdono/droopano
- op amp o analog switch guasto
- ripple alimentazione
- problema ground
- riparazione precedente fatta male / pista sollevata
- problema connettore o jack
- contaminazione CV da pannello/controlli
- possibile problema CEM5530/PD508 o circuiti collegati alla generazione CV, se applicabile

Non diagnosticare nulla come certo. Crea un albero di ipotesi.

10. Analisi specifica ECR

Crea:

doc/prophet_vs_service_context/circuit_maps/board_revisions_ecr.md

Riassumi con attenzione ECR738 e ECR739.

Per ECR738:
- identifica il motivo dichiarato della modifica
- identifica piste/componenti cambiati se visibili
- elenca valori resistenze menzionati
- spiega perché le modifiche a tensione/resistenze del pressure sensor possono essere importanti
- elenca cosa un tecnico dovrebbe verificare fisicamente sulla scheda

Per ECR739:
- stessa struttura
- confronto con ECR738

Importante:
Non assumere che il Prophet VS dell’utente abbia o non abbia queste modifiche ECR.
Crea una checklist per verificare:
- revisione board
- presenza di piste tagliate
- jumper aggiunti
- valori resistenze
- qualità saldature
- corrispondenza con artwork PCB scannerizzato

11. README.md finale

README.md deve spiegare:

- Cosa contiene questa cartella
- Come sono state estratte le pagine
- Quanto è affidabile l’OCR
- Come navigare il materiale
- Da dove partire per diagnosi riparazione
- Avviso importante: non sostituisce un tecnico synth qualificato
- Avviso importante: sezioni alimentazione/mains possono essere pericolose
- Avviso importante: vecchie PCB possono danneggiarsi con calore eccessivo, forza, probe sbagliati o corti durante le misure

12. Regole qualità

- Non inventare valori componenti.
- Se non sei sicuro, scrivi [NON CHIARO].
- Usa link relativi.
- Usa nomi file esatti e numeri pagina.
- Ogni affermazione su un circuito deve puntare a una pagina sorgente.
- Tieni separati “confermato”, “inferito” e “speculativo”.
- Dai priorità all’utilità per la riparazione, non alla formattazione perfetta.
- Genera Markdown conciso ma completo. Evita muri di testo enormi.
- Alla fine stampa un breve riassunto dei file creati e i file più importanti da cui partire per la diagnosi.