# pvs_service pagina 13

Source: `doc/pvs_service.pdf` pagina 13  
Immagine: [pvs_service/page_013.png](../../page_images/pvs_service/page_013.png)  
Testo/OCR: [pvs_service/page_013.txt](../../extracted_text/pvs_service/page_013.txt)  
Metodo testo: `ocr`, confidenza: `medium`

## Cosa sembra contenere questa pagina
Digital bus / board interconnect page. Tipo pagina: schema elettrico, digital board, bus, interconnect.

## Etichette / componenti / IC / net visibili
- IC / chip: [NON CHIARO]
- Resistenze / capacitori / reti: [NON CHIARO]
- Connettori / test point: [NON CHIARO]
- Rail: +5V, VSS
- Net nominate: DAC, DATA BUS, ADDRESS BUS, CART

## Riassunto funzione del circuito
Confermato dalle etichette:
- OCR mostra DATA BUS, +5V, CS, ABxx, D0/D1/D2 e segnali digitali/interconnect.

Inferenza ragionevole:
- Probabile foglio di interconnessione digitale o decoding bus.

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
- [pvs_service pagina 3](page_003.md)
