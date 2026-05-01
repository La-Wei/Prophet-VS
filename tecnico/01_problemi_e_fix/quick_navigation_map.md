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
| `../06_pdf_originali/5530.pdf` | 3 | `../05_pagine_rilevanti/immagini/5530/page_003.png` | `../05_pagine_rilevanti/note/5530/page_003.md` | Limiti alimentazione e comportamento uscite CEM5530 | Carichi e capacita' sulle uscite CV, rail CEM5530 |
| `../06_pdf_originali/5530.pdf` | 4 | `../05_pagine_rilevanti/immagini/5530/page_004.png` | `../05_pagine_rilevanti/note/5530/page_004.md` | Timing, inhibit e droop dello sample & hold | Droop, ripple o modulazione sulle uscite hold |

Se la modulazione sembra seguire patch/LFO/envelope, partire da CV e S&H prima di sostituire audio op amp.

## 3. Pressure / aftertouch

| PDF sorgente | Pagina | Immagine | Nota | Perche importante | Ispezionare per primo |
| --- | --- | --- | --- | --- | --- |
| `../06_pdf_originali/pvs_service.pdf` | 4 | `../05_pagine_rilevanti/immagini/pvs_service/page_004.png` | `../05_pagine_rilevanti/note/pvs_service/page_004.md` | Pressure circuit su keyboard/power board | `U310`, `R321`, `R307/R308/R309/R320/R304`, `TP301/TP302` |
| `../06_pdf_originali/pvs_service.pdf` | 6 | `../05_pagine_rilevanti/immagini/pvs_service/page_006.png` | `../05_pagine_rilevanti/note/pvs_service/page_006.md` | Pressure/SENSOR collegato a main analog/S&H | `U459`, `R458`, net `PRESSURE/SENSOR`, connettori `P402/P403` |
| `../06_pdf_originali/sci_prophet_vs_ecr738.pdf` | 2 | `../05_pagine_rilevanti/immagini/sci_prophet_vs_ecr738/page_002.png` | `../05_pagine_rilevanti/note/sci_prophet_vs_ecr738/page_002.md` | ECR738 modifica pressure sensor lato main analog | Valore `R458`, jumper/tagli, saldature nella modifica |
| `../06_pdf_originali/sci_prophet_vs_ecr739.pdf` | 4 | `../05_pagine_rilevanti/immagini/sci_prophet_vs_ecr739/page_004.png` | `../05_pagine_rilevanti/note/sci_prophet_vs_ecr739/page_004.md` | ECR739 pressure/power/reset su keyboard board | Rete `U310` e valori resistenze, `SENSOR/PRESSURE` |

Non assumere che ECR738/ECR739 siano presenti: verificarle fisicamente sulla macchina.

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
