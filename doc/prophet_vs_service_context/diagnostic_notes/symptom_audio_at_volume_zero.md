# Sintomo: Prophet VS emette suono / bleed distorto anche con volume a zero

## Descrizione sintomo
Suono o bleed distorto resta udibile a volume zero; in alcune patch sembra passare LFO/modulazione anche con volume a zero.

## Aree circuito piu rilevanti
VCA/VCF/PAN/LEV CV, audio path dopo volume, chorus/output, S&H CEM5530, rail analogici, ground, riparazioni precedenti.

## Pagine sorgente da ispezionare
- [pvs_service pagina 6](../page_notes/pvs_service/page_006.md)
- [pvs_service pagina 9](../page_notes/pvs_service/page_009.md)
- [pvs_service pagina 11](../page_notes/pvs_service/page_011.md)
- [pvs_service pagina 12](../page_notes/pvs_service/page_012.md)
- [5530 pagina 1](../page_notes/5530/page_001.md)
- [5530 pagina 3](../page_notes/5530/page_003.md)
- [5530 pagina 4](../page_notes/5530/page_004.md)

## Possibili cause ordinate dalla piu probabile alla meno probabile
1. Leakage controllo VCA o CV VCA non torna a valore di chiusura.
2. Audio path che bypassa o si accoppia dopo il volume control.
3. Chorus/output op amp o filtro finale che distorce o inietta segnale.
4. CEM5530/S&H con droop, hold step o timing INH/address errato.
5. Ripple/rail analogici o ground AGND/DGND problematici.
6. Riparazione precedente, pista sollevata, connettore o jack difettoso.
7. Contaminazione CV da pannello/controlli o pressure sensor.

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
