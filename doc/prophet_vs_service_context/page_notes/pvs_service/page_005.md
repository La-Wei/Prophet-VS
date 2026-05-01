# pvs_service pagina 5

Source: `doc/pvs_service.pdf` pagina 5  
Immagine: [pvs_service/page_005.png](../../page_images/pvs_service/page_005.png)  
Testo/OCR: [pvs_service/page_005.txt](../../extracted_text/pvs_service/page_005.txt)  
Metodo testo: `ocr`, confidenza: `medium`

## Cosa sembra contenere questa pagina
PCB artwork/layout digital or keyboard board. Tipo pagina: board artwork / layout, riparazione fisica.

## Etichette / componenti / IC / net visibili
- IC / chip: U303, U334, U314, U319, U320, U307, U308, U309, U335, U332, U333, U329
- Resistenze / capacitori / reti: C304, C337, C325, C329, C334, C335, C317, R313, R314, C331, C339, C3238, R303, R320, R334
- Connettori / test point: J304, J302, P302, TP302, J306, P3206, P2400
- Rail: [NON CHIARO]
- Net nominate: [NON CHIARO]

## Riassunto funzione del circuito
Confermato dalle etichette:
- OCR mostra molti riferimenti fisici U30x, C30x, J30x/P30x e componenti della famiglia 2400.

Inferenza ragionevole:
- Probabile layout/artwork fisico utile per localizzare componenti della board digital/keyboard.

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
- [pvs_service pagina 4](page_004.md)
