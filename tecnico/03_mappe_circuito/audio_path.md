# Audio Path / VCA / VCF / Output

## Ruolo nel Prophet VS
Mappa di lavoro per diagnosi e lettura incrociata. Le affermazioni sotto derivano dalle pagine/sorgenti linkate.

## Pagine/sorgenti
- [pvs_service pagina 6](../05_pagine_rilevanti/note/pvs_service/page_006.md)
- [pvs_service pagina 9](../05_pagine_rilevanti/note/pvs_service/page_009.md)
- [pvs_service pagina 11](../05_pagine_rilevanti/note/pvs_service/page_011.md)
- [pvs_service pagina 12](../05_pagine_rilevanti/note/pvs_service/page_012.md)

## Componenti importanti
VCF/VCA/PAN/LEV CV outputs, op amps on audio pages, left/right voice/output sections, 7 kHz lowpass section.

## Rail importanti
+12V, -12V, AGND and any local analog rails shown on the page images.

## Flusso del segnale, per quanto leggibile
Voice/filter/VCA stages -> pan/left/right routing -> chorus/output/filter stages. CV from S&H controls VCA/VCF/PAN/LEV.

## Cosa puo andare storto
- Op amp o IC guasto, condensatore in perdita, saldatura crepata, via/pista danneggiata, connettore ossidato.
- Rail basso/con ripple o ground analogico/digitale disturbato.
- Valori ECR errati, jumper/tagli non documentati o riparazioni precedenti malfatte.

## Come potrebbe collegarsi ai sintomi
Bleed with volume at zero can come from VCA control leakage, audio coupling after volume, output/chorus leakage, op amp bias issues, rail ripple, or bad ground.

## Cose da misurare in sicurezza
- Verificare concettualmente i rail indicati nelle pagine sorgente prima di inseguire segnali piccoli.
- Confrontare ground analogico/digitale solo come da schema e senza creare corti accidentali.
- Osservare uscite/ingressi etichettati nelle pagine linkate con strumenti adeguati e massa corretta.
- Nelle aree mains/trasformatore, operare solo con tecnico qualificato e isolamento appropriato.

## Cose da non assumere
- Non assumere che le modifiche ECR738/ECR739 siano presenti sullo strumento reale.
- Non assumere valori OCR se l'immagine non li conferma chiaramente.
- Non sostituire componenti per somiglianza del sintomo senza prova elettrica o ispezione fisica.
