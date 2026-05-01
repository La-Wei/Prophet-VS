# pvs_service pagina 6

Source: `../../../06_pdf_originali/pvs_service.pdf` pagina 6  
Immagine: [pvs_service/page_006.png](../../immagini/pvs_service/page_006.png)  

## Cosa sembra contenere questa pagina
Main analog 2400 sample & hold / sensor, sheet 1 of 4. Tipo pagina: schema elettrico, sample & hold, pressure circuit, generazione CV, alimentazione analogica.

## Etichette / componenti / IC / net visibili
- IC / chip: U454, 78M08, U453, LS221, U449, 5530, U425, U451, U459, U450, U402, 78M05, U401, 7905
- Resistenze / capacitori / reti: C402, C466, C404, C403, C406, C470, C400, R458
- Connettori / test point: P4035, P4002, P402, P403
- Rail: +5V, -5V, +12V, -12V, +8V, +5.6V, AGND, DGND, GND, VSS, VREF
- Net nominate: LEFT, RIGHT, PAN, LEV, VCA, VCF, PRESSURE, SENSOR, INH, DAC, CHORUS, OUTPUT EN, LEFT CHORUS, RIGHT CHORUS, RIGHT FINAL CV

## Riassunto funzione del circuito
Confermato dalle etichette:
- Title block leggibile: SCHEMATIC PCB MAIN ANALOG 2400 SAMPLE & HOLD - SENSOR.
- Sono visibili U449 5530, U425 5530, DAC/U451 6012, U459 741, R458, P402/P403, U450 78M08, U402 78M05, U401 7905, pressure sensor, VCA/VCF/PAN/LEV outputs, LEFT/RIGHT CHORUS CV, LEFT/RIGHT FINAL CV, +12V, -12V, +5.6V, +8V, -5V, AGND.

Inferenza ragionevole:
- Pagina chiave per CV bleed/droop, pressione, VCA/VCF/PAN/LEV e possibili problemi da S&H o rails analogici.

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
- [5530 pagina 1](../5530/page_001.md)
- [5530 pagina 3](../5530/page_003.md)
- [sci_prophet_vs_ecr738 pagina 2](../sci_prophet_vs_ecr738/page_002.md)
- [pvs_service pagina 9](page_009.md)
