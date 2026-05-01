# 5530 pagina 3

Source: `../../../06_pdf_originali/5530.pdf` pagina 3  
Immagine: [5530/page_003.png](../../immagini/5530/page_003.png)  

## Cosa sembra contenere questa pagina
CEM5530 application hints and power supplies. Tipo pagina: datasheet, sample & hold, alimentazione.

## Etichette / componenti / IC / net visibili
- IC / chip: [NON CHIARO]
- Resistenze / capacitori / reti: [NON CHIARO]
- Connettori / test point: [NON CHIARO]
- Rail: +5V, -5V, -12V, +8V, VDD, VSS
- Net nominate: LEV, INH, DAC, SWIN

## Riassunto funzione del circuito
Confermato dalle etichette:
- Pagina application hints: supply voltage tra VDD e VSS non deve superare 16V; supplies positive/negative influenzano swing input/output.

Inferenza ragionevole:
- Utile per collegare rail analogici fuori tolleranza a clipping/errore CV.

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
- [5530 pagina 1](page_001.md)
- [pvs_service pagina 6](../pvs_service/page_006.md)
