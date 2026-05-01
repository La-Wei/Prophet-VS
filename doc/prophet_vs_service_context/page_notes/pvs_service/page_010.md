# pvs_service pagina 10

Source: `doc/pvs_service.pdf` pagina 10  
Immagine: [pvs_service/page_010.png](../../page_images/pvs_service/page_010.png)  
Testo/OCR: [pvs_service/page_010.txt](../../extracted_text/pvs_service/page_010.txt)  
Metodo testo: `ocr`, confidenza: `medium`

## Cosa sembra contenere questa pagina
PCB artwork/layout main analog. Tipo pagina: board artwork / layout, riparazione fisica, analog board.

## Etichette / componenti / IC / net visibili
- IC / chip: U406, U424, U440, U463
- Resistenze / capacitori / reti: C466, C440, C495, R474, C445, C497
- Connettori / test point: [NON CHIARO]
- Rail: GND
- Net nominate: PAN

## Riassunto funzione del circuito
Confermato dalle etichette:
- OCR mostra molti riferimenti R4xx/C4xx/U4xx tipici della main analog board.

Inferenza ragionevole:
- Probabile layout/artwork fisico per la main analog board.

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
- [pvs_service pagina 6](page_006.md)
- [pvs_service pagina 9](page_009.md)
