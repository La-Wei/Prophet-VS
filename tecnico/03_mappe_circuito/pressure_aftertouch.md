# Pressure / Aftertouch

## Ruolo nel Prophet VS
Mappa di lavoro per diagnosi e lettura incrociata. Le affermazioni sotto derivano dalle pagine/sorgenti linkate.

## Pagine/sorgenti
- [pvs_service pagina 4](../05_pagine_rilevanti/note/pvs_service/page_004.md)
- [pvs_service pagina 6](../05_pagine_rilevanti/note/pvs_service/page_006.md)
- [sci_prophet_vs_ecr738 pagina 2](../05_pagine_rilevanti/note/sci_prophet_vs_ecr738/page_002.md)
- [sci_prophet_vs_ecr739 pagina 4](../05_pagine_rilevanti/note/sci_prophet_vs_ecr739/page_004.md)

## Componenti importanti
U310, U459, R321, R307, R308, R309, R320, R304, R458, pressure sensor connector, TP301/TP302.

## Rail importanti
+12V, -12V, +5VD, AGND/DGND; ECR738 page 2 also shows local +12V biasing near pressure sensor.

## Flusso del segnale, per quanto leggibile
Pressure sensor -> op amp/scale network -> SENSOR/PRESSURE net -> digital/analog interconnect. Confermato sulle pagine sopra; dettagli di pin/value vanno verificati sulle immagini.

## Cosa puo andare storto
- Op amp o IC guasto, condensatore in perdita, saldatura crepata, via/pista danneggiata, connettore ossidato.
- Rail basso/con ripple o ground analogico/digitale disturbato.
- Valori ECR errati, jumper/tagli non documentati o riparazioni precedenti malfatte.

## Come potrebbe collegarsi ai sintomi
Aftertouch non lineare, pressione sempre alta/bassa, CV contaminato, reset/rumore se ground/rail condivisi hanno problemi.

## Cose da misurare in sicurezza
- Verificare concettualmente i rail indicati nelle pagine sorgente prima di inseguire segnali piccoli.
- Confrontare ground analogico/digitale solo come da schema e senza creare corti accidentali.
- Osservare uscite/ingressi etichettati nelle pagine linkate con strumenti adeguati e massa corretta.
- Nelle aree mains/trasformatore, operare solo con tecnico qualificato e isolamento appropriato.

## Cose da non assumere
- Non assumere che le modifiche ECR738/ECR739 siano presenti sullo strumento reale.
- Non assumere valori OCR se l'immagine non li conferma chiaramente.
- Non sostituire componenti per somiglianza del sintomo senza prova elettrica o ispezione fisica.
