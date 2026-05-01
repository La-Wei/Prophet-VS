# pvs_service pagina 9

Source: `doc/pvs_service.pdf` pagina 9  
Immagine: [pvs_service/page_009.png](../../page_images/pvs_service/page_009.png)  
Testo/OCR: [pvs_service/page_009.txt](../../extracted_text/pvs_service/page_009.txt)  
Metodo testo: `ocr`, confidenza: `medium`

## Cosa sembra contenere questa pagina
Main analog 2400 voice/audio path: VCF/VCA/PAN. Tipo pagina: schema elettrico, audio path, VCA, VCF, pan, analog board.

## Etichette / componenti / IC / net visibili
- IC / chip: U457, U458, U455, U456
- Resistenze / capacitori / reti: C4124, R462, R463, R476, C4162
- Connettori / test point: P4093
- Rail: +12V, GND
- Net nominate: LEFT, RIGHT, PAN, VCA, VCF

## Riassunto funzione del circuito
Confermato dalle etichette:
- OCR legge LEFT, VCF OUT, VCAOUT, PAN, VOICE, VCAIN e vari riferimenti R4xx/C4xx.

Inferenza ragionevole:
- Pagina rilevante per audio distorto, bleed a volume zero, VCA/VCF/PAN e percorso voce analogico.

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
- [pvs_service pagina 11](page_011.md)
- [pvs_service pagina 12](page_012.md)
