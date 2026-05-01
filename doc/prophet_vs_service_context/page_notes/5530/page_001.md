# 5530 pagina 1

Source: `doc/5530.pdf` pagina 1  
Immagine: [5530/page_001.png](../../page_images/5530/page_001.png)  
Testo/OCR: [5530/page_001.txt](../../extracted_text/5530/page_001.txt)  
Metodo testo: `ocr`, confidenza: `medium`

## Cosa sembra contenere questa pagina
CEM5530 preliminary datasheet overview. Tipo pagina: datasheet, sample & hold, CEM5530.

## Etichette / componenti / IC / net visibili
- IC / chip: 5530, CEM5530
- Resistenze / capacitori / reti: [NON CHIARO]
- Connettori / test point: [NON CHIARO]
- Rail: +5V
- Net nominate: INH, DAC, SWIN

## Riassunto funzione del circuito
Confermato dalle etichette:
- Datasheet preliminare CEM5530 30-channel multiplexed Sample and Hold; descrive auto-zero op amp, analog multiplexer, 5-bit decoder e 30 S&H.
- OCR legge settling to 12 bits under 2 us, error <2 mV, outputs about -5 to +5V with +/-7.5V supplies.

Inferenza ragionevole:
- Molto rilevante per generazione CV Prophet VS e sintomi di droop/bleed/modulation leak.

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
- [5530 pagina 3](page_003.md)
- [5530 pagina 4](page_004.md)
- [pvs_service pagina 6](../pvs_service/page_006.md)
