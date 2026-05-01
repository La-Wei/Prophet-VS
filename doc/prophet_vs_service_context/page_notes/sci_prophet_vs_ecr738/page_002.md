# sci_prophet_vs_ecr738 pagina 2

Source: `doc/sci_prophet_vs_ecr738.pdf` pagina 2  
Immagine: [sci_prophet_vs_ecr738/page_002.png](../../page_images/sci_prophet_vs_ecr738/page_002.png)  
Testo/OCR: [sci_prophet_vs_ecr738/page_002.txt](../../extracted_text/sci_prophet_vs_ecr738/page_002.txt)  
Metodo testo: `ocr`, confidenza: `medium`

## Cosa sembra contenere questa pagina
ECR 738, modifica area pressure sensor su main analog/sample & hold. Tipo pagina: ECR / engineering change record, pressure circuit, sample & hold, board revision.

## Etichette / componenti / IC / net visibili
- IC / chip: U440, U459, 5530
- Resistenze / capacitori / reti: R458
- Connettori / test point: [NON CHIARO]
- Rail: +12V, -12V, +8V, GND, VSS
- Net nominate: LEFT, RIGHT, PAN, LEV, VCA, VCF, PRESSURE, SENSOR, CHORUS, LEFT CHORUS, RIGHT CHORUS

## Riassunto funzione del circuito
Confermato dalle etichette:
- L'immagine mostra PRESSURE SENSOR, U459 op amp, R458 annotata come 15K, rail +12V e -12V, e uscite VCA/VCF/PAN/LEV da un 5530.
- Si leggono modifiche/annotazioni vicino a R458, una resistenza da 1K e una indicazione manoscritta vicino a +12V.

Inferenza ragionevole:
- La modifica sembra intervenire sul bias/scala del pressure sensor e quindi sulla tensione SENSOR inviata alla logica/ADC.
- La vicinanza al blocco 5530 rende la pagina rilevante per CV VCA/VCF/PAN/LEV, ma non prova un guasto del 5530.

Incerto / da verificare manualmente:
- OCR e scansione non garantiscono valori completi; verificare sempre l'immagine pagina.
- Non assumere che una modifica ECR sia presente sulla macchina reale senza ispezione fisica.

## Rilevanza per riparazione
- Utile per collegare sintomi a pagine sorgente e localizzare componenti o net sul Prophet VS.
- Se la pagina contiene artwork/layout, usarla per ispezione fisica: piste, jumper, tagli, saldature, riparazioni precedenti.
- Se la pagina contiene schema, usarla per ragionare su rail, segnali, connettori e possibili cause, senza trattare l'OCR come prova definitiva.

## Possibili failure mode collegati a questa pagina
- Saldatura crepata, pista/via danneggiata, connettore ossidato o riparazione precedente non conforme.
- Componente attivo guasto o alimentazione fuori specifica nei blocchi mostrati.
- Condensatore in perdita, valore resistenza errato o rete resistiva modificata male, se applicabile alla pagina.
- CV bleed/droop, op amp guasto, analog switch/S&H guasto, ground analogico/digitale contaminato o ripple sui rail quando la pagina mostra circuiti analogici/CV.

## Cross-reference
- [pvs_service pagina 6](../pvs_service/page_006.md)
- [sci_prophet_vs_ecr739 pagina 4](../sci_prophet_vs_ecr739/page_004.md)
- [5530 pagina 1](../5530/page_001.md)
