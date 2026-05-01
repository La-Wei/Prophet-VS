# sci_prophet_vs_ecr739 pagina 4

Source: `doc/sci_prophet_vs_ecr739.pdf` pagina 4  
Immagine: [sci_prophet_vs_ecr739/page_004.png](../../page_images/sci_prophet_vs_ecr739/page_004.png)  
Testo/OCR: [sci_prophet_vs_ecr739/page_004.txt](../../extracted_text/sci_prophet_vs_ecr739/page_004.txt)  
Metodo testo: `ocr`, confidenza: `medium`

## Cosa sembra contenere questa pagina
ECR 739, pressure circuit e power supply su digital/keyboard board. Tipo pagina: pressure circuit, keyboard matrix, alimentazione, reset, ECR / engineering change record.

## Etichette / componenti / IC / net visibili
- IC / chip: U204, U320, HC174, U305, U310, HC132, U301, 7805, U302, 7812, U303, 7912, U304
- Resistenze / capacitori / reti: R321, C308, R309, R320, C301, R305, R304, R302, C305, R330, R315, R307, R308
- Connettori / test point: P202, P308, P303, P3002, TP301, TP302
- Rail: +5V, +5VD, +12V, -12V, AGND, DGND, GND
- Net nominate: LEFT, PAN, LEV, PRESSURE, SENSOR, RESET, CHORUS, KEYBOARD

## Riassunto funzione del circuito
Confermato dalle etichette:
- L'immagine mostra PRESSURE CIRCUIT, R321 OFFSET 50K, R307 20K, R308 10K, R309 47K, R320 10K, R304 15K, U310 op amp, U305 HC132, U301 7805, U302 7812, U303 7912 e U304 78L05.
- Sono visibili TP301, TP302, SENSOR, PRESSURE, +5VD, +12V, -12V, DGND, AGND e hardware mains/trasformatore.

Inferenza ragionevole:
- Questa pagina collega il pressure sensor al circuito keyboard/power/reset e va confrontata fisicamente con eventuali tagli piste o jumper ECR.

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
- [pvs_service pagina 4](../pvs_service/page_004.md)
- [pvs_service pagina 6](../pvs_service/page_006.md)
- [sci_prophet_vs_ecr738 pagina 2](../sci_prophet_vs_ecr738/page_002.md)
