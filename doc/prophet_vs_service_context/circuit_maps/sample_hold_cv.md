# Sample & Hold / CV Generation

## Ruolo nel Prophet VS
Mappa di lavoro per diagnosi e lettura incrociata. Le affermazioni sotto derivano dalle pagine/sorgenti linkate.

## Pagine/sorgenti
- [pvs_service pagina 6](../page_notes/pvs_service/page_006.md)
- [pvs_service pagina 7](../page_notes/pvs_service/page_007.md)
- [pvs_service pagina 8](../page_notes/pvs_service/page_008.md)
- [pvs_service pagina 9](../page_notes/pvs_service/page_009.md)
- [5530 pagina 1](../page_notes/5530/page_001.md)
- [5530 pagina 3](../page_notes/5530/page_003.md)
- [5530 pagina 4](../page_notes/5530/page_004.md)
- [5508 pagina 1](../page_notes/5508/page_001.md)
- [5508 pagina 3](../page_notes/5508/page_003.md)

## Componenti importanti
U449/U425 CEM5530, DAC/U451 6012, U453/U454 HC174, U405 HC174, 4051/logic shown on later analog pages, PD508/CEM5530 datasheet concepts.

## Rail importanti
+12V, -12V, +8V, +5.6V, -5V, +5VD, VDD/VSS/VREF.

## Flusso del segnale, per quanto leggibile
Digital data/address/timing -> DAC/reference -> CEM5530 input/inhibit/address -> held CV outputs such as VCA, VCF, PAN, LEV, chorus/final CV.

## Cosa puo andare storto
- Op amp o IC guasto, condensatore in perdita, saldatura crepata, via/pista danneggiata, connettore ossidato.
- Rail basso/con ripple o ground analogico/digitale disturbato.
- Valori ECR errati, jumper/tagli non documentati o riparazioni precedenti malfatte.

## Come potrebbe collegarsi ai sintomi
CV droop, modulation leak, VCA not closing, pan/level drift, distorted control voltages, output bleed with volume low.

## Cose da misurare in sicurezza
- Verificare concettualmente i rail indicati nelle pagine sorgente prima di inseguire segnali piccoli.
- Confrontare ground analogico/digitale solo come da schema e senza creare corti accidentali.
- Osservare uscite/ingressi etichettati nelle pagine linkate con strumenti adeguati e massa corretta.
- Nelle aree mains/trasformatore, operare solo con tecnico qualificato e isolamento appropriato.

## Cose da non assumere
- Non assumere che le modifiche ECR738/ECR739 siano presenti sullo strumento reale.
- Non assumere valori OCR se l'immagine non li conferma chiaramente.
- Non sostituire componenti per somiglianza del sintomo senza prova elettrica o ispezione fisica.
