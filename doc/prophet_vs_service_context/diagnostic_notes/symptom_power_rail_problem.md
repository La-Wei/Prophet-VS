# Sintomo: Power rail problem

## Descrizione sintomo
Sintomi multipli, reset, distorsione, rumore o instabilita che suggeriscono alimentazione.

## Aree circuito piu rilevanti
7805/7812/7912/78L05/78M08/78M05/7905, rettificatori, condensatori, AGND/DGND.

## Pagine sorgente da ispezionare
- [pvs_service pagina 4](../page_notes/pvs_service/page_004.md)
- [pvs_service pagina 6](../page_notes/pvs_service/page_006.md)
- [sci_prophet_vs_ecr739 pagina 4](../page_notes/sci_prophet_vs_ecr739/page_004.md)
- [5530 pagina 3](../page_notes/5530/page_003.md)

## Possibili cause ordinate dalla piu probabile alla meno probabile
1. Ripple eccessivo
2. Regolatore guasto
3. Condensatore elettrolitico/tantalio in perdita
4. Ground aperto o sporco
5. Carico eccessivo a valle

## Quale evidenza supporterebbe ogni causa
- Il sintomo cambia quando si osservano/isolano concettualmente le aree circuito indicate nelle pagine sorgente.
- Le misure mostrano rail, CV o audio fuori range rispetto alle etichette presenti nello schema.
- Ispezione visiva trova saldature, jumper, piste o componenti nella stessa zona delle pagine linkate.

## Quale evidenza la escluderebbe
- Rail e ground stabili, nessun ripple anomalo, e segnale/CV corretto prima e dopo il blocco sospetto.
- Il difetto resta invariato dopo esclusione documentata del blocco indicato.
- Continuita e componenti fisici corrispondono agli schemi/ECR.

## Misure/controlli da eseguire
- Prima controllare rail principali e locali indicati nelle page note.
- Poi osservare segnali etichettati nella pagina sorgente con massa corretta e strumenti adatti.
- Confrontare comportamento statico e dinamico: valore DC, ripple, risposta a patch/controlli, eventuale modulazione residua.

## Aree scheda/componenti da ispezionare visivamente
- Connettori citati nelle page note.
- Zone ECR e riparazioni precedenti, soprattutto tagli piste/jumper.
- Regolatori, op amp, CEM5530/S&H, condensatori tantalio/elettrolitici e jack/output.

## Rischi / cautele
- Non operare su mains/trasformatore senza tecnico qualificato.
- Evitare corti con puntali; vecchie PCB possono sollevare pad con calore o forza.
- Non sostituire parti rare senza prova; alcuni IC possono essere difficili da reperire.

## Domande per un tecnico
- Il difetto cambia tra uscita left/right, cuffie/line out o chorus on/off?
- Il bleed segue VCA/VCF/PAN/LEV o resta nel percorso audio finale?
- I rail locali e reference sono stabili a freddo/caldo?
- La board mostra ECR738/ECR739 applicati, parziali o assenti?
