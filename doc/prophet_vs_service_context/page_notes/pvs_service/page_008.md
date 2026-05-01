# pvs_service pagina 8

Source: `doc/pvs_service.pdf` pagina 8  
Immagine: [pvs_service/page_008.png](../../page_images/pvs_service/page_008.png)  
Testo/OCR: [pvs_service/page_008.txt](../../extracted_text/pvs_service/page_008.txt)  
Metodo testo: `ocr`, confidenza: `medium`

## Cosa sembra contenere questa pagina
Main analog 2400 waveform / voice analog area. Tipo pagina: schema elettrico, generazione waveform, analog board.

## Etichette / componenti / IC / net visibili
- IC / chip: U424, HC273, U630, U465
- Resistenze / capacitori / reti: C449, C433, R424
- Connettori / test point: [NON CHIARO]
- Rail: +5V, +5VD, VSS
- Net nominate: LEV, RESET, ADDRESS BUS

## Riassunto funzione del circuito
Confermato dalle etichette:
- OCR mostra U4xx/C4xx/R4xx, +5VD/+5VPN e riferimenti a FET/circuiti analogici.

Inferenza ragionevole:
- Probabile foglio main analog legato a voice/waveform e switching analogico.

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
- [pvs_service pagina 7](page_007.md)
- [pvs_service pagina 9](page_009.md)
