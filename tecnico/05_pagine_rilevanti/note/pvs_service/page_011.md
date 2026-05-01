# pvs_service pagina 11

Source: `../../../06_pdf_originali/pvs_service.pdf` pagina 11  
Immagine: [pvs_service/page_011.png](../../immagini/pvs_service/page_011.png)  

## Cosa sembra contenere questa pagina
Audio output / chorus area, left/right. Tipo pagina: schema elettrico, audio path, chorus, output.

## Etichette / componenti / IC / net visibili
- IC / chip: U904, U903, U920
- Resistenze / capacitori / reti: C930, C926, C995, C972, C927, R420, C962, C928, R109, C964, R983, C988, R939, R957, R929, C963, C932, C986, C943, R936, C967, C534, C597, C940
- Connettori / test point: P3908, P901
- Rail: +8V, VSS
- Net nominate: LEFT, RIGHT, CHORUS, CART, LEFT CHORUS

## Riassunto funzione del circuito
Confermato dalle etichette:
- OCR mostra LEFT, C9xx/R9xx, output, valori come 301K/100pF e riferimenti a left/right voices.

Inferenza ragionevole:
- Probabile sezione chorus/output o filtro audio correlato ai canali left/right.

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
- [pvs_service pagina 12](page_012.md)
