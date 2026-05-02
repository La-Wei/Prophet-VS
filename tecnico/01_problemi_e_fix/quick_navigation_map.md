# Mappa rapida di navigazione per riparazione Prophet VS

Usare questa mappa come indice pratico. I due sintomi principali, bleed a volume zero e case/regolatore caldo, possono essere collegati da un rail disturbato ma vanno diagnosticati separatamente finche le misure non li uniscono.

## 1. Audio che passa con volume a zero

| PDF sorgente | Pagina | Immagine | Nota | Perche importante | Ispezionare per primo |
| --- | --- | --- | --- | --- | --- |
| `../06_pdf_originali/pvs_service.pdf` | 9 | `../05_pagine_rilevanti/immagini/pvs_service/page_009.png` | `../05_pagine_rilevanti/note/pvs_service/page_009.md` | VCF/VCA/PAN e percorso voce analogico | `VCAIN/VCAOUT`, net `VCA/VCF/PAN`, saldature e R/C vicino a U455-U458 |
| `../06_pdf_originali/pvs_service.pdf` | 11 | `../05_pagine_rilevanti/immagini/pvs_service/page_011.png` | `../05_pagine_rilevanti/note/pvs_service/page_011.md` | Output/chorus left-right | Differenza left/right, op amp output, condensatori C9xx/R9xx |
| `../06_pdf_originali/pvs_service.pdf` | 12 | `../05_pagine_rilevanti/immagini/pvs_service/page_012.png` | `../05_pagine_rilevanti/note/pvs_service/page_012.md` | Output, lowpass 7 kHz, right voice/chorus | TL082, rail `+12V/-12V/+8V`, DC offset o saturazione |

Non concludere automaticamente che il pot volume sia guasto: prima capire se il segnale residuo nasce prima o dopo il controllo volume.

## 2. Contaminazione CV / modulazione

| PDF sorgente | Pagina | Immagine | Nota | Perche importante | Ispezionare per primo |
| --- | --- | --- | --- | --- | --- |
| `../06_pdf_originali/pvs_service.pdf` | 6 | `../05_pagine_rilevanti/immagini/pvs_service/page_006.png` | `../05_pagine_rilevanti/note/pvs_service/page_006.md` | Main analog sample & hold / sensor, CEM5530, DAC e CV `VCA/VCF/PAN/LEV` | `U449/U425`, `U451`, `INH`, `DAC`, rail `+8V/+5.6V/-5V` |
| `../06_pdf_originali/5530.pdf` | 2 | `../05_pagine_rilevanti/immagini/5530/page_002.png` | `../05_pagine_rilevanti/note/5530/page_002.md` | Pinout/diagramma CEM5530, utile anche per dissipatori e orientamento | Package `40` pin, `U449/U425` |
| `../06_pdf_originali/5530.pdf` | 3 | `../05_pagine_rilevanti/immagini/5530/page_003.png` | `../05_pagine_rilevanti/note/5530/page_003.md` | Limiti alimentazione e comportamento uscite CEM5530 | Carichi e capacita' sulle uscite CV, rail CEM5530 |
| `../06_pdf_originali/5530.pdf` | 4 | `../05_pagine_rilevanti/immagini/5530/page_004.png` | `../05_pagine_rilevanti/note/5530/page_004.md` | Timing, inhibit e droop dello sample & hold | Droop, ripple o modulazione sulle uscite hold |

Se la modulazione sembra seguire patch/LFO/envelope, partire da CV e S&H prima di sostituire audio op amp.

## 2b. CEM5530 / cloni / autocostruzione

| Sorgente | Pagina | Immagine | Nota | Perche importante | Ispezionare per primo |
| --- | --- | --- | --- | --- | --- |
| `../07_autocostruzione_ricambi/cem5530_clone_build_dossier.md` | dossier | n/a | `../07_autocostruzione_ricambi/cem5530_clone_build_dossier.md` | Stato reale schemi ELD5530, architetture `MAX5167`, `SSM2300`, `PD508/CEM5508` e test minimi | Non esistono Gerber/BOM pubblici verificati; usare come brief di progettazione |
| `../07_autocostruzione_ricambi/max5167_v2_like_pre_design.md` | progetto preliminare | n/a | `../07_autocostruzione_ricambi/max5167_v2_like_pre_design.md` | Pista `MAX5167` portata a pin mapping, rail locali, vincoli PCB e piano test | Non PCB-ready: verificare timing, carichi e spazio sulla macchina reale |
| `../07_autocostruzione_ricambi/rev_a_max5167_prototipo/README.md` | prototipo Rev A | n/a | `../07_autocostruzione_ricambi/rev_a_max5167_prototipo/README.md` | Schema testuale, netlist CSV, BOM funzionale, vincoli PCB e collaudo per prototipo `MAX5167` | Prototipo non validato: non montare senza test fuori macchina |
| `../06_pdf_originali/5530.pdf` | 2 | `../05_pagine_rilevanti/immagini/5530/page_002.png` | `../05_pagine_rilevanti/note/5530/page_002.md` | Pinout da ricavare manualmente prima di qualsiasi clone | Pin 1, 40 pin, output e rail |
| `../06_pdf_originali/5530.pdf` | 3-4 | `../05_pagine_rilevanti/immagini/5530/page_003.png` | `../05_pagine_rilevanti/note/5530/page_003.md` | Alimentazioni, swing, timing `INH`, droop e acquisition | Rail e timing reali da misurare su `U449/U425` |
| `../06_pdf_originali/component_datasheets/README.md` | link datasheet | n/a | `../06_pdf_originali/component_datasheets/README.md` | Link ufficiali `MAX5167` e `SSM2300` per lavoro offline/manuale | Scaricare datasheet esterni se si progetta una scheda |

## 3. Pressure / aftertouch

| PDF sorgente | Pagina | Immagine | Nota | Perche importante | Ispezionare per primo |
| --- | --- | --- | --- | --- | --- |
| `../06_pdf_originali/pvs_service.pdf` | 4 | `../05_pagine_rilevanti/immagini/pvs_service/page_004.png` | `../05_pagine_rilevanti/note/pvs_service/page_004.md` | Pressure circuit su keyboard/power board | `U310`, `R321`, `R307/R308/R309/R320/R304`, `TP301/TP302` |
| `../06_pdf_originali/pvs_service.pdf` | 6 | `../05_pagine_rilevanti/immagini/pvs_service/page_006.png` | `../05_pagine_rilevanti/note/pvs_service/page_006.md` | Pressure/SENSOR collegato a main analog/S&H | `U459`, `R458`, net `PRESSURE/SENSOR`, connettori `P402/P403` |
| `../06_pdf_originali/sci_prophet_vs_ecr738.pdf` | 2 | `../05_pagine_rilevanti/immagini/sci_prophet_vs_ecr738/page_002.png` | `../05_pagine_rilevanti/note/sci_prophet_vs_ecr738/page_002.md` | ECR738 modifica pressure sensor lato main analog | Valore `R458`, jumper/tagli, saldature nella modifica |
| `../06_pdf_originali/sci_prophet_vs_ecr739.pdf` | 4 | `../05_pagine_rilevanti/immagini/sci_prophet_vs_ecr739/page_004.png` | `../05_pagine_rilevanti/note/sci_prophet_vs_ecr739/page_004.md` | ECR739 pressure/power/reset su keyboard board | Rete `U310` e valori resistenze, `SENSOR/PRESSURE` |

Non assumere che ECR738/ECR739 siano presenti: verificarle fisicamente sulla macchina.

## 3b. Batteria memoria / SRAM / patch

| Sorgente | Pagina | Immagine | Nota | Perche importante | Ispezionare per primo |
| --- | --- | --- | --- | --- | --- |
| `batteria_memoria_nvram.md` | nota locale | n/a | `batteria_memoria_nvram.md` | Chiarisce che `ELD5530` non elimina la batteria: la mod senza batteria e' una modifica separata alle SRAM patch | Stato batteria, polarita', corrosione, backup patch/SysEx e tipo SRAM montate |
| `../06_pdf_originali/pvs_service.pdf` | board CPU/memoria | n/a | `../05_pagine_rilevanti/note/pvs_service/page_003.md` | Memoria programmi e area CPU da verificare se si lavora su SRAM/batteria | Due SRAM originali, ROM vicine, battery backup e piste corrose |
| Synthelectro 2015 | post web | n/a | `https://synthelectro-fr.blogspot.com/2015/07/how-to-upgrade-programm-memory-of.html` | Esempio di mod SRAM non volatile: due SRAM `32 Kbytes`, quattro banchi, batteria rimossa | Non confondere con i due `ELD5530` citati nello stesso post |

Se le SRAM originali sono ancora montate, la batteria serve ancora. Se si monta una vera SRAM non volatile compatibile, la batteria puo' essere rimossa.

## 4. Instabilita alimentazione / rail

| PDF sorgente | Pagina | Immagine | Nota | Perche importante | Ispezionare per primo |
| --- | --- | --- | --- | --- | --- |
| `../06_pdf_originali/pvs_service.pdf` | 4 | `../05_pagine_rilevanti/immagini/pvs_service/page_004.png` | `../05_pagine_rilevanti/note/pvs_service/page_004.md` | Power supply digital/keyboard e reset | `U301 7805`, `U302 7812`, `U303 7912`, `U304 78L05`, `U305 HC132` |
| `../06_pdf_originali/sci_prophet_vs_ecr739.pdf` | 4 | `../05_pagine_rilevanti/immagini/sci_prophet_vs_ecr739/page_004.png` | `../05_pagine_rilevanti/note/sci_prophet_vs_ecr739/page_004.md` | Conferma rail `+5VD/+12V/-12V`, reset e pressure | Ripple, Vin/Vout, `AGND/DGND`, `TP301/TP302` |
| `../06_pdf_originali/pvs_service.pdf` | 6 | `../05_pagine_rilevanti/immagini/pvs_service/page_006.png` | `../05_pagine_rilevanti/note/pvs_service/page_006.md` | Rail analogici locali per S&H/CV | `U401 7905`, `U402 78M05`, `U450 78M08`, `+8V/+5.6V/-5V` |

Misurare rail e ripple prima di interpretare segnali piccoli o sostituire IC rari.

## 5. Case caldo / regolatore che scalda troppo

| Sorgente | Pagina | Immagine | Nota | Perche importante | Ispezionare per primo |
| --- | --- | --- | --- | --- | --- |
| `../foto/IMG_5543.jpg` | foto utente | `../foto/IMG_5543.jpg` | `technician_briefing_volume_zero_bleed.md` | Mostra i tre TO-220 fissati al dissipatore/case | Identificare quale dei tre scalda: sinistra `U301`, centro `U302`, destra `U303` secondo layout |
| `../06_pdf_originali/pvs_service.pdf` | 5 | `../05_pagine_rilevanti/immagini/pvs_service/page_005.png` | `../05_pagine_rilevanti/note/pvs_service/page_005.md` | Designator map fisica della board | Confermare ordine `U301/U302/U303`, condensatori e connettori vicini |
| `../06_pdf_originali/pvs_service.pdf` | 4 | `../05_pagine_rilevanti/immagini/pvs_service/page_004.png` | `../05_pagine_rilevanti/note/pvs_service/page_004.md` | Schema rail dei tre regolatori | `U301 +5VD`, `U302 +12V`, `U303 -12V`, condensatori/diodi/filtro |
| `../06_pdf_originali/sci_prophet_vs_ecr739.pdf` | 4 | `../05_pagine_rilevanti/immagini/sci_prophet_vs_ecr739/page_004.png` | `../05_pagine_rilevanti/note/sci_prophet_vs_ecr739/page_004.md` | Conferma ECR/power supply | Vin/Vout/ripple, carico a valle, isolamento/pasta/vite |

Non concludere automaticamente che il regolatore sia guasto: e' gia' stato sostituito con uno piu capiente, quindi cercare carico eccessivo, condensatore in perdita/corto, caduta Vin-Vout o montaggio termico errato.

## 6. Riparazione precedente / pista sollevata / ECR sbagliata

| PDF sorgente | Pagina | Immagine | Nota | Perche importante | Ispezionare per primo |
| --- | --- | --- | --- | --- | --- |
| `../06_pdf_originali/sci_prophet_vs_ecr738.pdf` | 2 | `../05_pagine_rilevanti/immagini/sci_prophet_vs_ecr738/page_002.png` | `../05_pagine_rilevanti/note/sci_prophet_vs_ecr738/page_002.md` | Modifica pressure sensor lato main analog | `R458`, jumper, tagli piste, flussante, pad sollevati |
| `../06_pdf_originali/sci_prophet_vs_ecr738.pdf` | 3 | `../05_pagine_rilevanti/immagini/sci_prophet_vs_ecr738/page_003.png` | `../05_pagine_rilevanti/note/sci_prophet_vs_ecr738/page_003.md` | Riferimento artwork/layout ECR | Routing fisico e riparazioni non documentate |
| `../06_pdf_originali/sci_prophet_vs_ecr739.pdf` | 4 | `../05_pagine_rilevanti/immagini/sci_prophet_vs_ecr739/page_004.png` | `../05_pagine_rilevanti/note/sci_prophet_vs_ecr739/page_004.md` | ECR pressure/power/reset | Valori resistenze, tagli/jumper, saldature su `U310/U301-U303` |
| `../06_pdf_originali/pvs_service.pdf` | 5 | `../05_pagine_rilevanti/immagini/pvs_service/page_005.png` | `../05_pagine_rilevanti/note/pvs_service/page_005.md` | Layout per confronto fisico | Serigrafia, pad, vias, connettori e componenti attorno ai regolatori |

Prima ispezione a strumento spento; non correggere ECR "a memoria" senza confronto schema/foto/board reale.

## 7. Chorus / output

| PDF sorgente | Pagina | Immagine | Nota | Perche importante | Ispezionare per primo |
| --- | --- | --- | --- | --- | --- |
| `../06_pdf_originali/pvs_service.pdf` | 11 | `../05_pagine_rilevanti/immagini/pvs_service/page_011.png` | `../05_pagine_rilevanti/note/pvs_service/page_011.md` | Chorus/output left-right | `U903/U904/U920`, C9xx/R9xx, differenza canali |
| `../06_pdf_originali/pvs_service.pdf` | 12 | `../05_pagine_rilevanti/immagini/pvs_service/page_012.png` | `../05_pagine_rilevanti/note/pvs_service/page_012.md` | Right voices, chorus e lowpass 7 kHz | `TL082`, `RIGHT CHORUS`, `LEV`, rail `+12V/-12V/+8V` |
| `../06_pdf_originali/pvs_service.pdf` | 6 | `../05_pagine_rilevanti/immagini/pvs_service/page_006.png` | `../05_pagine_rilevanti/note/pvs_service/page_006.md` | CV chorus/final generate da S&H | `LEFT/RIGHT CHORUS CV`, `RIGHT FINAL CV`, CEM5530 |

Se chorus/output cambia il difetto, seguire prima questa sezione; se il difetto e' gia' presente a monte, tornare a VCA/S&H.
