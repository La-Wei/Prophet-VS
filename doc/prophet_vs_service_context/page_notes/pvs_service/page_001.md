# pvs_service pagina 1

Source: `doc/pvs_service.pdf` pagina 1  
Immagine: [pvs_service/page_001.png](../../page_images/pvs_service/page_001.png)  
Testo/OCR: [pvs_service/page_001.txt](../../extracted_text/pvs_service/page_001.txt)  
Metodo testo: `ocr`, confidenza: `medium`

## Cosa sembra contenere questa pagina
Schematic PCB left front panel. Tipo pagina: schema elettrico, front panel, controlli, ADC, joystick/pitch/mod.

## Etichette / componenti / IC / net visibili
- IC / chip: HC244, ADC0808
- Resistenze / capacitori / reti: [NON CHIARO]
- Connettori / test point: [NON CHIARO]
- Rail: +5V, +8V, GND
- Net nominate: LEFT, RIGHT, PAN, LEV, CHORUS, CART, MIDI, SWIN

## Riassunto funzione del circuito
Confermato dalle etichette:
- Title block leggibile nell'immagine: SCHEMATIC PCB LEFT FRONT PANEL.
- Sono visibili ADC0808, LCD/front panel, switch e controlli come pitch/mod wheel, joystick, data entry, volume/balance e linee +5V.

Inferenza ragionevole:
- Pagina utile per controlli pannello, contaminazione CV dai potenziometri e routing verso logica/ADC.

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
- [pvs_service pagina 2](page_002.md)
- [pvs_service pagina 3](page_003.md)
- [pvs_service pagina 4](page_004.md)
