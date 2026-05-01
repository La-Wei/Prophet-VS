# pvs_service pagina 12

Source: `doc/pvs_service.pdf` pagina 12  
Immagine: [pvs_service/page_012.png](../../page_images/pvs_service/page_012.png)  
Testo/OCR: [pvs_service/page_012.txt](../../extracted_text/pvs_service/page_012.txt)  
Metodo testo: `ocr`, confidenza: `medium`

## Cosa sembra contenere questa pagina
Audio output / 7 kHz lowpass / right voice. Tipo pagina: schema elettrico, audio path, chorus, lowpass.

## Etichette / componenti / IC / net visibili
- IC / chip: TL082
- Resistenze / capacitori / reti: C903, C450, C904, C947, C323, C969, R924, R921, R940, C966, C937, R520, R922, R455, R953, C954, C938, R947, R954, C975, C968, C988
- Connettori / test point: [NON CHIARO]
- Rail: +12V, -12V, +8V
- Net nominate: RIGHT, LEV, CHORUS, RIGHT CHORUS

## Riassunto funzione del circuito
Confermato dalle etichette:
- OCR legge RIGHT VOICES, LEV, 7 KHZ LOWPASS, TL082/082, C9xx/R9xx e +12V/-12V.

Inferenza ragionevole:
- Pagina importante per filtro di uscita, chorus/output e distorsione sui canali finali.

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
- [pvs_service pagina 9](page_009.md)
- [pvs_service pagina 11](page_011.md)
