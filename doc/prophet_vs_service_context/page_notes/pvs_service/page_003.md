# pvs_service pagina 3

Source: `doc/pvs_service.pdf` pagina 3  
Immagine: [pvs_service/page_003.png](../../page_images/pvs_service/page_003.png)  
Testo/OCR: [pvs_service/page_003.txt](../../extracted_text/pvs_service/page_003.txt)  
Metodo testo: `ocr`, confidenza: `medium`

## Cosa sembra contenere questa pagina
Schematic PCB digital processor. Tipo pagina: schema elettrico, digital board, CPU, MIDI, reset, RAM/ROM.

## Etichette / componenti / IC / net visibili
- IC / chip: U326, U332, U327, U330, U325, HC32, U323, U223, 68000, 68B50
- Resistenze / capacitori / reti: C322, R332, R327, C340, R334, R323, R333, C335, R324, C325, R328, C337, C327
- Connettori / test point: P305, P2305, P302, P3205, P202, P0900
- Rail: +5V, +5VD, GND
- Net nominate: PAN, RESET, ADDRESS BUS, MIDI

## Riassunto funzione del circuito
Confermato dalle etichette:
- Title block leggibile: SCHEMATIC PCB DIGITAL, 2400 PROCESSOR.
- Sono visibili 68000, 27256 ROM, 6264 non-volatile RAM, 6116 RAM, 68B50 UART, MIDI OUT/THRU/IN, data/address bus, clock/reset.

Inferenza ragionevole:
- Pagina utile per reset, bus digitale, MIDI e cause digitali che possono influire sul refresh CV.

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
- [pvs_service pagina 4](page_004.md)
- [pvs_service pagina 6](page_006.md)
- [pvs_service pagina 13](page_013.md)
