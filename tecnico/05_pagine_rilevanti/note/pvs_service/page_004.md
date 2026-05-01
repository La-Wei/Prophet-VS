# pvs_service pagina 4

Source: `../../../06_pdf_originali/pvs_service.pdf` pagina 4  
Immagine: [pvs_service/page_004.png](../../immagini/pvs_service/page_004.png)  

## Cosa sembra contenere questa pagina
Digital keyboard and power supply, pressure circuit. Tipo pagina: schema elettrico, keyboard matrix, pressure circuit, alimentazione, reset.

## Etichette / componenti / IC / net visibili
- IC / chip: U307, U304, HC174, 7805, U305, U310, U301, U302, 7812, U303, 7912, HC132
- Resistenze / capacitori / reti: C309, R307, R321, R308, R309, R320, R305, C301, R304, R302, C305, C304, C307
- Connettori / test point: P3035, P202, P3201, P303, P3302, TP301, TP302
- Rail: +5V, +5VD, +12V, -12V, AGND, DGND, GND
- Net nominate: LEFT, PRESSURE, RESET, INH, CHORUS, KEYBOARD

## Riassunto funzione del circuito
Confermato dalle etichette:
- Title block leggibile: SCHEMATIC PCB DIGITAL 2400 KEYBOARD AND POWER SUPPLY.
- Sono visibili KEYBOARD MATRIX, PRESSURE CIRCUIT, R321 OFFSET, R307/R308/R309/R320/R304/R305, U310 op amp, U301 7805, U302 7812, U303 7912, U304 78L05, U305 HC132, TP301/TP302, +5VD, +12V, -12V, DGND, AGND.

Inferenza ragionevole:
- Questa pagina e' centrale per pressure/aftertouch, alimentazione, reset e diagnostica rails.

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
- [sci_prophet_vs_ecr739 pagina 4](../sci_prophet_vs_ecr739/page_004.md)
- [pvs_service pagina 6](page_006.md)
