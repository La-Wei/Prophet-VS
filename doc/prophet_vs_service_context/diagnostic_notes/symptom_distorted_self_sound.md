# Sintomo: Suono proprio distorto

## Descrizione sintomo
Il timbro del Prophet VS risulta distorto o instabile anche senza input esterni.

## Aree circuito piu rilevanti
Audio path, VCA/VCF, chorus/output, rail analogici, CV sample & hold.

## Pagine sorgente da ispezionare
- [pvs_service pagina 6](../page_notes/pvs_service/page_006.md)
- [pvs_service pagina 9](../page_notes/pvs_service/page_009.md)
- [pvs_service pagina 11](../page_notes/pvs_service/page_011.md)
- [pvs_service pagina 12](../page_notes/pvs_service/page_012.md)

## Possibili cause ordinate dalla piu probabile alla meno probabile
1. Rail analogici fuori tolleranza
2. Op amp o filtro output guasto
3. VCA/VCF pilotati da CV errato
4. Condensatori audio in perdita
5. Ground o connettori intermittenti

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
