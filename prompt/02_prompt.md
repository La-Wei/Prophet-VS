Ora usa la knowledge base generata in:

doc/prophet_vs_service_context/

per creare un briefing diagnostico mirato per un tecnico che deve lavorare su un Sequential Circuits Prophet VS.

Sintomo principale osservato:
- Con volume a zero, passa comunque qualcosa: suono, patch distorta o bleed audio.
- In alcune patch sembra passare un comportamento tipo LFO/modulazione anche con volume a zero.
- Nella foto locale `IMG_5543.jpg` si vede la board `PC2400-3 REV B` e tre dispositivi TO-220 fissati al case/dissipatore. L'utente li chiama "transistor", ma dai documenti sembrano i regolatori lineari della sezione alimentazione digital/keyboard:
  - `U301` = `7805`, rail `+5VD`
  - `U302` = `7812`, rail `+12V`
  - `U303` = `7912`, rail `-12V`
  La designator map `pvs_service` pagina 5 mostra questi tre TO-220 in ordine fisico sinistra->destra come `U301`, `U302`, `U303`; confermare comunque sulla serigrafia reale se visibile.
- Uno di questi tre regolatori scalda troppo: da dietro il case diventa molto caldo/brucia. E' stata aggiunta una ventola esterna come mitigazione, ma la causa non e' stata trovata.
- Quel regolatore e' gia stato sostituito con un componente piu capiente; quindi non trattare il regolatore stesso come causa certa. Considera invece carico eccessivo a valle, condensatore in perdita/corto, ponte/rectifier o filtro, rail sbilanciato, dissipazione anomala per tensione in ingresso, isolamento termico/mica/pasta termica, vite/dissipatore/case, ground o riparazione precedente.
- Potrebbero esserci riparazioni precedenti e alcune saldature/piste potrebbero richiedere ispezione.
- Lo strumento è rimasto inutilizzato per anni.
- L’utente vuole capire quali aree circuito possono plausibilmente causare questi sintomi prima di consegnarlo a un tecnico.

Foto utente da includere nel briefing:
- `IMG_5543.jpg`: area alimentazione `PC2400-3 REV B`, tre TO-220 su dissipatore/case, connettori e condensatori vicini.

Crea:

doc/prophet_vs_service_context/diagnostic_notes/technician_briefing_volume_zero_bleed.md

Struttura:

# Briefing tecnico: Prophet VS audio/modulazione che passa con volume a zero

## 1. Sintomo noto
Descrivi il sintomo senza sovradiagnosticare.
Includi anche il sintomo termico separato:
- case posteriore molto caldo in corrispondenza dei tre TO-220/regolatori
- uno dei regolatori scalda troppo
- e' gia stato sostituito con uno piu capiente, quindi il sospetto principale deve spostarsi sul circuito alimentato o sulle condizioni di dissipazione, non sul solo regolatore

## 2. Documenti/pagine sorgente più rilevanti
Elenca le note Markdown pagina per pagina e le immagini originali generate da ispezionare.
Includi esplicitamente:
- `IMG_5543.jpg`
- `doc/prophet_vs_service_context/page_notes/pvs_service/page_004.md`
- `doc/prophet_vs_service_context/page_images/pvs_service/page_004.png`
- `doc/prophet_vs_service_context/page_notes/pvs_service/page_005.md`
- `doc/prophet_vs_service_context/page_images/pvs_service/page_005.png`
- `doc/prophet_vs_service_context/page_notes/sci_prophet_vs_ecr739/page_004.md`
- `doc/prophet_vs_service_context/circuit_maps/power_reset.md`
- `doc/prophet_vs_service_context/component_index/ics.md`
- `doc/prophet_vs_service_context/component_index/power_rails.md`

## 3. Albero ipotesi ad alto livello
Separa in:

A. Percorso audio dopo il controllo volume
B. Problema VCA / control voltage
C. Leakage/droop/uscita errata dal sample & hold
D. Leakage sezione chorus/output o op amp guasto
E. Problema rail alimentazione / ground / reset
F. Problema CV keyboard/pressure/aftertouch
G. Riparazione precedente fatta male: solder bridge, pista sollevata, resistenza errata, pista tagliata, jumper errato
H. Problema normalizzazione connettori/jack
I. Surriscaldamento dei regolatori `U301/U302/U303` sul dissipatore/case

Per ogni ipotesi includi:
- Perché potrebbe essere compatibile con il sintomo
- Quale area dello schema ispezionare
- Quale misura o osservazione la supporterebbe
- Cosa la escluderebbe
- Componenti/net/pagine rilevanti dai documenti

## 4. Controlli sicuri e non invasivi da fare prima
Includi:
- ispezione visiva
- reinserimento/reseating connettori
- controllo corrosione/ruggine evidente intorno a MIDI/footswitch/aux/output
- controllo revisione board / modifiche ECR alle resistenze
- controllo rail alimentazione con la dovuta cautela
- test di ascolto: uscita dry vs chorus/output se applicabile
- inizializzazione patch / confronto tra patch inizializzata e factory patch
- comportamento del pot volume e capire se il segnale è prima o dopo il volume control
- identificazione visiva dei tre regolatori su `IMG_5543.jpg`: `U301 7805`, `U302 7812`, `U303 7912`; la designator map indica sinistra->destra `U301/U302/U303`, da confermare sulla PCB reale se la serigrafia e visibile
- controllo segni di stress termico intorno a `U301/U302/U303`, condensatori elettrolitici/tantalio vicini, ponte rettificatore/diodi e connettori
- controllo che vite, isolamento, rondella, pasta termica e contatto con dissipatore/case siano corretti

## 5. Misure per tecnico qualificato
Includi misure concettuali:
- rail +5, -5, +12, -12 e ripple
- per `U301 7805`, `U302 7812`, `U303 7912`: tensione ingresso, tensione uscita, ripple, caduta Vin-Vout, temperatura, corrente/carico se misurabile in sicurezza
- confronto temperatura tra i tre regolatori, senza concludere che quello piu caldo sia guasto
- controllo assorbimento a valle dei rail `+5VD`, `+12V`, `-12V`
- controllo di condensatori in perdita/corto o IC a valle che caricano il rail
- comportamento CV VCA quando volume è a zero
- uscite sample & hold per droop/rumore/livelli DC errati
- uscite op amp bloccate/saturate
- tensione circuito pressure sensor / valori resistenze
- continuità piste tagliate/jumper ECR
- continuità ground

Non dare istruzioni pericolose lato mains.

## 6. Rilevanza ECR738/ECR739
Spiega come le modifiche ECR su pressure sensor, resistenze e piste potrebbero o non potrebbero essere collegate al sintomo.
Dichiara chiaramente che questi ECR non sono automaticamente la causa, ma modifiche mancanti, sbagliate o fatte male potrebbero creare comportamenti strani nelle control voltage.

## 7. Componenti/aree da attenzionare
Crea una tabella:

| Area | Componenti/net | Perché rilevante | Pagina sorgente |

Usa solo componenti realmente trovati nell’indice generato.
La tabella deve includere una riga dedicata ai tre regolatori:
- `U301 7805`, `U302 7812`, `U303 7912`, rail `+5VD`, `+12V`, `-12V`, ordine fisico sinistra->destra dalla designator map `pvs_service pagina 5`, sorgenti `pvs_service pagina 4`, `sci_prophet_vs_ecr739 pagina 4`, foto `IMG_5543.jpg`.

## 8. Domande da fare al riparatore
Crea una checklist che l’utente può mandare a un tecnico:

- Puoi verificare se le modifiche ECR738/ECR739 sono presenti e fatte correttamente?
- Puoi controllare rail e ripple prima di sostituire IC a caso?
- Puoi verificare se il bleed è prima o dopo il potenziometro volume/output stage?
- Puoi controllare con oscilloscopio le linee CV rilevanti e il controllo VCA?
- Puoi ispezionare solder bridge, piste sollevate o riparazioni precedenti?
- Puoi identificare fisicamente i tre regolatori sul dissipatore/case (`U301/U302/U303`) e dirmi quale dei tre scalda?
- Puoi misurare Vin/Vout/ripple e caduta termica sui regolatori, e verificare se c'e' carico eccessivo a valle?
- Puoi controllare condensatori/diodi/ponte rettificatore e IC alimentati dal rail del regolatore caldo?
- Puoi verificare isolamento, vite, rondelle e pasta termica del regolatore sul dissipatore/case?
- Puoi confrontare il comportamento su patch inizializzata e factory patch?
- Puoi evitare recap generalizzato se le misure non indicano problemi ai condensatori?

## 9. Conclusione
Dai un ordine diagnostico più probabile, non una diagnosi singola fissa.
La conclusione deve trattare i due sintomi insieme ma senza forzarli:
- il bleed/distorsione puo essere audio/CV/S&H/output
- il regolatore caldo puo essere una causa comune se il rail e' rumoroso/basso o se un carico a valle disturba la macchina
- oppure possono essere due problemi separati
