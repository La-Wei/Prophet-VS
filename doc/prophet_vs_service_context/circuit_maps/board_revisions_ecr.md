# Board Revisions / ECR738 / ECR739

## Ruolo nel Prophet VS
Questa mappa confronta gli engineering change records scannerizzati. Non assumere che il Prophet VS reale abbia una di queste modifiche: va verificato sulla board.

## Pagine/sorgenti
- [sci_prophet_vs_ecr738 pagina 1](../page_notes/sci_prophet_vs_ecr738/page_001.md)
- [sci_prophet_vs_ecr738 pagina 2](../page_notes/sci_prophet_vs_ecr738/page_002.md)
- [sci_prophet_vs_ecr738 pagina 3](../page_notes/sci_prophet_vs_ecr738/page_003.md)
- [sci_prophet_vs_ecr739 pagina 1](../page_notes/sci_prophet_vs_ecr739/page_001.md)
- [sci_prophet_vs_ecr739 pagina 4](../page_notes/sci_prophet_vs_ecr739/page_004.md)
- [pvs_service pagina 4](../page_notes/pvs_service/page_004.md)
- [pvs_service pagina 6](../page_notes/pvs_service/page_006.md)

## ECR738
Motivo dichiarato della modifica: [NON CHIARO] nella scansione/OCR della pagina 1. La pagina 2 mostra una modifica nell'area pressure sensor / sample & hold sensor.

Componenti/piste visibili:
- PRESSURE SENSOR, U459, R458, +12V, -12V, C4148/C4147 circa, P402/SENSOR/DGND sono visibili o inferibili dall'immagine ECR738 pagina 2.
- R458 appare annotata come 15K; nell'immagine e' anche visibile una rete con +12V e valori manoscritti, incluso 6.8K e 1K vicino al nodo pressure. Verificare sull'immagine e sulla board.

Perche puo essere importante:
- Cambiare resistenze o bias nel pressure sensor puo alterare offset, range e saturazione dell'aftertouch.
- Una modifica errata puo far arrivare CV fuori scala, contaminare letture o creare sintomi intermittenti se jumper/tagli sono fragili.

Cosa verificare fisicamente:
- Revisione board e presenza di tagli piste/jumper nella zona pressure sensor.
- Valore reale di R458 e delle resistenze annotate vicino a +12V.
- Qualita saldature, piste sollevate, flussante/ossidazione e continuita verso P402/SENSOR/DGND.

## ECR739
Motivo dichiarato della modifica: [NON CHIARO] nelle pagine 1-3. La pagina 4 mostra chiaramente pressure circuit, keyboard/power supply e reset/power rails.

Componenti/piste visibili:
- R321 OFFSET 50K, R307 20K, R308 10K, R309 47K, R320 10K, R304 15K, R305 470K, U310 op amp, U305 HC132, U301 7805, U302 7812, U303 7912, U304 78L05.
- TP301/TP302, SENSOR, PRESSURE, +5VD, +12V, -12V, DGND, AGND sono leggibili sulla pagina 4.

Confronto con ECR738:
- Entrambi toccano il pressure/aftertouch path, ma ECR738 e' mostrato sul lato main analog/sample & hold sensor, mentre ECR739 e' mostrato sul lato digital/keyboard/power supply.
- Rete, connettori e nomi net non vanno fusi automaticamente: confrontare le pagine ECR con pvs_service pagine 4 e 6.

## Checklist verifica ECR
- Revisione board stampata/silkscreen corrisponde ai documenti?
- Ci sono piste tagliate? Sono pulite e isolate?
- Ci sono jumper aggiunti? Sono meccanicamente stabili?
- Valori resistenze corrispondono alle annotazioni ECR e allo schema di servizio?
- Le saldature nella zona pressure sensor/regolatori sono lucide e non sollevano pad?
- Il routing fisico corrisponde all'artwork scannerizzato?
- I rail +5VD, +12V, -12V, +8V/+5.6V/-5V sono presenti prima di interpretare il segnale pressure?
