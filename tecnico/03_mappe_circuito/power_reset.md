# Power / Reset

## Ruolo nel Prophet VS
Mappa di lavoro per diagnosi e lettura incrociata. Le affermazioni sotto derivano dalle pagine/sorgenti linkate.

## Pagine/sorgenti
- [pvs_service pagina 4](../05_pagine_rilevanti/note/pvs_service/page_004.md)
- [pvs_service pagina 6](../05_pagine_rilevanti/note/pvs_service/page_006.md)
- [sci_prophet_vs_ecr739 pagina 4](../05_pagine_rilevanti/note/sci_prophet_vs_ecr739/page_004.md)
- [5530 pagina 3](../05_pagine_rilevanti/note/5530/page_003.md)

## Componenti importanti
U301 7805, U302 7812, U303 7912, U304 78L05, U401 7905, U402 78M05, U450 78M08, reset gates U305/HC132, transformer/rectifier area.

## Rail importanti
+5VD, +12V, -12V, +8V, +5.6V, -5V, AGND/DGND.

## Flusso del segnale, per quanto leggibile
Transformer/rectifiers/regulators generate digital and analog rails; reset logic depends on supply behavior.

## Cosa puo andare storto
- Op amp o IC guasto, condensatore in perdita, saldatura crepata, via/pista danneggiata, connettore ossidato.
- Rail basso/con ripple o ground analogico/digitale disturbato.
- Valori ECR errati, jumper/tagli non documentati o riparazioni precedenti malfatte.

## Come potrebbe collegarsi ai sintomi
Low/rippled rails can cause distortion, CV error, digital mis-refresh, reset instability, heat, or audio hum/bleed.

## Cose da misurare in sicurezza
- Verificare concettualmente i rail indicati nelle pagine sorgente prima di inseguire segnali piccoli.
- Confrontare ground analogico/digitale solo come da schema e senza creare corti accidentali.
- Osservare uscite/ingressi etichettati nelle pagine linkate con strumenti adeguati e massa corretta.
- Nelle aree mains/trasformatore, operare solo con tecnico qualificato e isolamento appropriato.

## Cose da non assumere
- Non assumere che le modifiche ECR738/ECR739 siano presenti sullo strumento reale.
- Non assumere valori OCR se l'immagine non li conferma chiaramente.
- Non sostituire componenti per somiglianza del sintomo senza prova elettrica o ispezione fisica.
