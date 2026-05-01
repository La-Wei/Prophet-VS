# Sample & Hold / CV Generation

## Ruolo nel Prophet VS
Mappa di lavoro per diagnosi e lettura incrociata. Le affermazioni sotto derivano dalle pagine/sorgenti linkate.

## Pagine/sorgenti
- [pvs_service pagina 6](../05_pagine_rilevanti/note/pvs_service/page_006.md)
- [pvs_service pagina 9](../05_pagine_rilevanti/note/pvs_service/page_009.md)
- [5530 pagina 1](../05_pagine_rilevanti/note/5530/page_001.md)
- [5530 pagina 3](../05_pagine_rilevanti/note/5530/page_003.md)
- [5530 pagina 4](../05_pagine_rilevanti/note/5530/page_004.md)
- [CEM5530: diagnosi, ricambi e dissipazione](../01_problemi_e_fix/cem5530_diagnosi_ricambi.md)
- PDF supplementare: [5508.pdf](../06_pdf_originali/5508.pdf), utile come riferimento S&H generico ma non trattato come prova che quel chip sia montato nel Prophet VS esaminato.

## Componenti importanti
U449/U425 CEM5530, DAC/U451 6012, U453/U454 HC174 e concetti CEM5530/5508 per hold, droop e timing.

Nota pratica: `U449/U425` sono anche componenti storicamente fragili; prima di sostituirli controllare rail/timing/socket/piste, e valutare dissipatori o cloni solo con conferma strumentale.

## Rail importanti
+12V, -12V, +8V, +5.6V, -5V, +5VD, VDD/VSS/VREF.

## Flusso del segnale, per quanto leggibile
Digital data/address/timing -> DAC/reference -> CEM5530 input/inhibit/address -> held CV outputs such as VCA, VCF, PAN, LEV, chorus/final CV.

## Cosa puo andare storto
- Op amp o IC guasto, condensatore in perdita, saldatura crepata, via/pista danneggiata, connettore ossidato.
- Rail basso/con ripple o ground analogico/digitale disturbato.
- Valori ECR errati, jumper/tagli non documentati o riparazioni precedenti malfatte.

## Come potrebbe collegarsi ai sintomi
CV droop, modulation leak, VCA not closing, pan/level drift, distorted control voltages, output bleed with volume low.

## Cose da misurare in sicurezza
- Verificare concettualmente i rail indicati nelle pagine sorgente prima di inseguire segnali piccoli.
- Confrontare ground analogico/digitale solo come da schema e senza creare corti accidentali.
- Osservare uscite/ingressi etichettati nelle pagine linkate con strumenti adeguati e massa corretta.
- Nelle aree mains/trasformatore, operare solo con tecnico qualificato e isolamento appropriato.

## Cose da non assumere
- Non assumere che le modifiche ECR738/ECR739 siano presenti sullo strumento reale.
- Non assumere valori OCR se l'immagine non li conferma chiaramente.
- Non sostituire componenti per somiglianza del sintomo senza prova elettrica o ispezione fisica.
