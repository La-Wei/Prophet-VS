# pvs_service pagina 2

Source: `doc/pvs_service.pdf` pagina 2  
Immagine: [pvs_service/page_002.png](../../page_images/pvs_service/page_002.png)  
Testo/OCR: [pvs_service/page_002.txt](../../extracted_text/pvs_service/page_002.txt)  
Metodo testo: `ocr`, confidenza: `medium`

## Cosa sembra contenere questa pagina
Schematic PCB right front panel and main cartridge. Tipo pagina: schema elettrico, front panel, cartridge board, keyboard/pannello.

## Etichette / componenti / IC / net visibili
- IC / chip: [NON CHIARO]
- Resistenze / capacitori / reti: RA202
- Connettori / test point: P602, P201, J601
- Rail: +5V, +5VD, GND
- Net nominate: LEFT, RIGHT, PAN, CHORUS, CART

## Riassunto funzione del circuito
Confermato dalle etichette:
- Title block leggibile: SCHEMATIC PCB RIGHT FRONT PANEL AND MAIN CARTRIDGE, 2400.
- Sono visibili MAIN CARTRIDGE BD 2400-6, P201/P602/J601, CD0-CD15, CA1-CA13, CART OE/WE/CE, PROT, +5VD/GND e LED front panel.

Inferenza ragionevole:
- Pagina rilevante per cartridge board, switch/LED del pannello e linee digitali condivise.

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
- [pvs_service pagina 1](page_001.md)
- [pvs_service pagina 3](page_003.md)
