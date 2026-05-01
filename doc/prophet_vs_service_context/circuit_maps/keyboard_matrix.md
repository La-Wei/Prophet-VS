# Keyboard Matrix / Controls

## Ruolo nel Prophet VS
Mappa di lavoro per diagnosi e lettura incrociata. Le affermazioni sotto derivano dalle pagine/sorgenti linkate.

## Pagine/sorgenti
- [pvs_service pagina 1](../page_notes/pvs_service/page_001.md)
- [pvs_service pagina 2](../page_notes/pvs_service/page_002.md)
- [pvs_service pagina 4](../page_notes/pvs_service/page_004.md)
- [sci_prophet_vs_ecr739 pagina 4](../page_notes/sci_prophet_vs_ecr739/page_004.md)

## Componenti importanti
Keyboard matrix contacts, front panel switches S2xx/S6xx/S7xx, HC logic, ADC/front panel controls, pressure sensor.

## Rail importanti
+5VD, DGND and pressure circuit analog references.

## Flusso del segnale, per quanto leggibile
Switch/contact matrix and panel controls feed digital logic/ADC; pressure path is partly analog and shares board interconnects.

## Cosa puo andare storto
- Op amp o IC guasto, condensatore in perdita, saldatura crepata, via/pista danneggiata, connettore ossidato.
- Rail basso/con ripple o ground analogico/digitale disturbato.
- Valori ECR errati, jumper/tagli non documentati o riparazioni precedenti malfatte.

## Come potrebbe collegarsi ai sintomi
Stuck controls, false pressure, panel CV contamination, keyboard scan faults, intermittent connectors.

## Cose da misurare in sicurezza
- Verificare concettualmente i rail indicati nelle pagine sorgente prima di inseguire segnali piccoli.
- Confrontare ground analogico/digitale solo come da schema e senza creare corti accidentali.
- Osservare uscite/ingressi etichettati nelle pagine linkate con strumenti adeguati e massa corretta.
- Nelle aree mains/trasformatore, operare solo con tecnico qualificato e isolamento appropriato.

## Cose da non assumere
- Non assumere che le modifiche ECR738/ECR739 siano presenti sullo strumento reale.
- Non assumere valori OCR se l'immagine non li conferma chiaramente.
- Non sostituire componenti per somiglianza del sintomo senza prova elettrica o ispezione fisica.
