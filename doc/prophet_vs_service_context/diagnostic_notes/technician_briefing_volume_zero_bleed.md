# Briefing tecnico: Prophet VS audio/modulazione che passa con volume a zero

## 1. Sintomo noto

Il Prophet VS lascia passare qualcosa anche con il volume a zero: puo' essere suono residuo, patch distorta, bleed audio o una modulazione percepibile tipo LFO in alcune patch. Il sintomo non va interpretato subito come "VCA guasto": puo' stare nel percorso audio, nel controllo CV del VCA, nello sample & hold, nell'output/chorus, nei rail o in una riparazione precedente.

Sintomo termico separato:

- Il retro del case diventa molto caldo in corrispondenza dei tre dispositivi TO-220 fissati al dissipatore/case.
- Dalla documentazione questi tre dispositivi non risultano transistor generici ma regolatori lineari della sezione alimentazione digital/keyboard: `U301 7805`, `U302 7812`, `U303 7912`.
- La designator map di `pvs_service` pagina 5 indica l'ordine fisico sinistra->destra come `U301`, `U302`, `U303`; confermare sulla serigrafia reale se visibile.
- Uno di questi regolatori scalda troppo. E' gia' stato sostituito con un componente piu' capiente, quindi il sospetto principale deve spostarsi sul circuito alimentato, sul carico a valle o sulle condizioni di dissipazione, non sul solo regolatore.

## 2. Documenti/pagine sorgente piu rilevanti

- `IMG_5543.jpg`: foto locale della board `PC2400-3 REV B`, area alimentazione, tre TO-220 su dissipatore/case, connettori e condensatori vicini.
- `doc/prophet_vs_service_context/page_notes/pvs_service/page_004.md` ([nota](../page_notes/pvs_service/page_004.md)) e `doc/prophet_vs_service_context/page_images/pvs_service/page_004.png` ([immagine](../page_images/pvs_service/page_004.png)): keyboard/power supply, pressure circuit, `U301/U302/U303`, `U304`, `U305`, `U310`, rail `+5VD`, `+12V`, `-12V`, `AGND`, `DGND`.
- `doc/prophet_vs_service_context/page_notes/pvs_service/page_005.md` ([nota](../page_notes/pvs_service/page_005.md)) e `doc/prophet_vs_service_context/page_images/pvs_service/page_005.png` ([immagine](../page_images/pvs_service/page_005.png)): layout/artwork fisico della board, utile per localizzare i riferimenti e confrontarli con la foto.
- `doc/prophet_vs_service_context/page_notes/sci_prophet_vs_ecr739/page_004.md` ([nota](../page_notes/sci_prophet_vs_ecr739/page_004.md)) e `doc/prophet_vs_service_context/page_images/sci_prophet_vs_ecr739/page_004.png` ([immagine](../page_images/sci_prophet_vs_ecr739/page_004.png)): ECR739, pressure circuit e power supply; conferma `U301 7805`, `U302 7812`, `U303 7912`, `U304 78L05`, `U305 HC132`, `U310`, `TP301/TP302`.
- `doc/prophet_vs_service_context/circuit_maps/power_reset.md` ([mappa](../circuit_maps/power_reset.md)): mappa rail/reset e failure mode associati a rail bassi, ripple e ground.
- `doc/prophet_vs_service_context/component_index/ics.md` ([indice](../component_index/ics.md)): indice IC/regolatori, inclusi `U301/U302/U303`, CEM5530 `U449/U425`, `U459`, `U310`, `U401/U402/U450`.
- `doc/prophet_vs_service_context/component_index/power_rails.md` ([indice](../component_index/power_rails.md)): indice rail `+5VD`, `+12V`, `-12V`, `+8V`, `+5.6V`, `-5V`, `AGND/DGND`.
- `doc/prophet_vs_service_context/circuit_maps/audio_path.md` ([mappa](../circuit_maps/audio_path.md)): percorso VCF/VCA/PAN/output e possibili cause di bleed.
- `doc/prophet_vs_service_context/circuit_maps/sample_hold_cv.md` ([mappa](../circuit_maps/sample_hold_cv.md)): CEM5530, DAC, timing `INH`, uscite CV `VCA/VCF/PAN/LEV`.
- `doc/prophet_vs_service_context/circuit_maps/pressure_aftertouch.md` ([mappa](../circuit_maps/pressure_aftertouch.md)): `PRESSURE/SENSOR`, `U310`, `U459`, reti ECR.
- `doc/prophet_vs_service_context/circuit_maps/board_revisions_ecr.md` ([mappa](../circuit_maps/board_revisions_ecr.md)): confronto ECR738/ECR739 e checklist di modifica fisica.

## 3. Albero ipotesi ad alto livello

### A. Percorso audio dopo il controllo volume

Perche compatibile: se il bleed e' udibile anche con il potenziometro volume a zero, il segnale potrebbe accoppiarsi o rientrare dopo il punto in cui il volume dovrebbe attenuarlo. Un difetto in uscita, un accoppiamento tra piste, un condensatore in perdita o un jack/connettore possono lasciare passare audio residuo.

Area da ispezionare: pagine `pvs_service` 9, 11, 12; nets `LEFT`, `RIGHT`, `CHORUS`; componenti audio/output `U455/U456/U457/U458`, `U903/U904/U920`, `TL082`, reti R/C C9xx/R9xx.

Supporterebbe: segnale presente dopo il controllo volume anche quando il segnale prima del volume e' correttamente attenuato; differenza tra uscite left/right, cuffie/line, dry/chorus.

Escluderebbe: audio nullo in tutti i punti dopo il volume quando il volume e' a zero, con bleed presente solo come CV/modulazione su stadi precedenti.

Componenti/net/pagine: `LEFT/RIGHT/CHORUS`, `pvs_service` pagine 9, 11, 12, `audio_path.md`, `named_nets.md`.

### B. Problema VCA / control voltage

Perche compatibile: un VCA che non chiude completamente, o una CV VCA fuori livello, puo' lasciare passare voce anche se il controllo utente e' a zero. Se il difetto cambia tra patch, inviluppi o modulazioni, la pista CV diventa piu' sospetta.

Area da ispezionare: CV `VCA` generate dallo S&H, percorso VCF/VCA/PAN su `pvs_service` pagine 6 e 9.

Supporterebbe: CV VCA non raggiunge il livello di chiusura, e il bleed segue envelope/LFO/patch; il segnale audio prima del VCA e' normale ma l'uscita VCA non si chiude.

Escluderebbe: CV VCA corretta e stabile con VCA effettivamente chiuso, ma segnale che appare solo in uno stadio output successivo.

Componenti/net/pagine: `VCA`, `VCF`, `PAN`, `LEV`, CEM5530 `U449/U425`, `pvs_service` pagine 6 e 9.

### C. Leakage/droop/uscita errata dal sample & hold

Perche compatibile: lo S&H genera molte CV, incluse `VCA/VCF/PAN/LEV`, chorus/final CV e altre linee di controllo. Droop, hold step, timing `INH` errato, riferimento/DAC instabile o rail disturbati possono produrre modulazione residua o livelli errati.

Area da ispezionare: main analog sample & hold su `pvs_service` pagina 6; datasheet CEM5530 pagine 1, 3, 4; linee `DAC`, `INH`, `VREF`, rail locali `+8V`, `+5.6V`, `-5V`.

Supporterebbe: CV che deriva, ripple o modulazione sulle uscite hold, livello VCA/LEV non fermo, sintomo che cambia con patch o con modulazioni.

Escluderebbe: tutte le CV interessate sono stabili, prive di ripple e coerenti quando il sintomo e' presente.

Componenti/net/pagine: `U449`, `U425`, `U451`, `U453/U454`, `DAC`, `INH`, `VCA/VCF/PAN/LEV`, `pvs_service` pagina 6, `5530` pagine 1/3/4.

### D. Leakage sezione chorus/output o op amp guasto

Perche compatibile: se il bleed resta in una uscita finale o cambia con chorus/output, puo' derivare da op amp, filtri, condensatori di accoppiamento o routing left/right/chorus.

Area da ispezionare: output/chorus e filtro lowpass su `pvs_service` pagine 11 e 12.

Supporterebbe: differenza netta tra uscita dry e chorus/output, DC offset o saturazione su un op amp, un canale piu' difettoso dell'altro.

Escluderebbe: output/chorus puliti e silenziosi quando viene iniettato o seguito il segnale con volume a zero, mentre il bleed e' gia' presente a monte.

Componenti/net/pagine: `LEFT`, `RIGHT`, `CHORUS`, `LEFT CHORUS`, `RIGHT CHORUS`, `U903/U904/U920`, `TL082`, `pvs_service` pagine 11 e 12.

### E. Problema rail alimentazione / ground / reset

Perche compatibile: rail bassi o con ripple possono creare distorsione, CV sbagliate, refresh digitale instabile, reset incerto, rumore o bleed. Il regolatore caldo rende questa ipotesi importante, soprattutto se il rail alimentato ha carico eccessivo o ripple anomalo.

Area da ispezionare: power supply digital/keyboard su `pvs_service` pagina 4 e `sci_prophet_vs_ecr739` pagina 4; local analog rails su `pvs_service` pagina 6; ground `AGND/DGND`.

Supporterebbe: `+5VD`, `+12V` o `-12V` fuori valore, ripple eccessivo, caduta Vin-Vout anomala sui regolatori, reset instabile, temperatura correlata al carico.

Escluderebbe: rail stabili, ripple basso, assorbimento normale e ground continui mentre il difetto si localizza chiaramente in un solo blocco audio/CV.

Componenti/net/pagine: `U301 7805`, `U302 7812`, `U303 7912`, `U304 78L05`, `U305 HC132`, `U401 7905`, `U402 78M05`, `U450 78M08`, `+5VD`, `+12V`, `-12V`, `+8V`, `+5.6V`, `-5V`, `AGND/DGND`.

### F. Problema CV keyboard/pressure/aftertouch

Perche compatibile: il pressure/aftertouch entra nelle CV e puo' produrre comportamento percepito come modulazione o livello anomalo, specialmente se la taratura o le ECR sono state applicate male.

Area da ispezionare: `PRESSURE/SENSOR`, `U310`, `U459`, `R321`, `R307/R308/R309/R320/R304`, `R458`, `TP301/TP302`.

Supporterebbe: valore `PRESSURE/SENSOR` bloccato, rumoroso, saturato o dipendente dal tocco anche quando non dovrebbe; modifiche ECR incoerenti.

Escluderebbe: pressure sensor stabile e coerente, nessuna correlazione con aftertouch/pressure, CV audio principali corrette.

Componenti/net/pagine: `pvs_service` pagine 4 e 6, `sci_prophet_vs_ecr738` pagina 2, `sci_prophet_vs_ecr739` pagina 4, `pressure_aftertouch.md`.

### G. Riparazione precedente fatta male

Perche compatibile: piste tagliate, jumper, resistenze errate, saldature fredde o ponti di stagno possono creare sia bleed/CV instabili sia carico eccessivo su un rail. Lo strumento e' vecchio e potrebbe essere stato modificato secondo ECR o riparato in modo parziale.

Area da ispezionare: zone ECR738/ECR739, regolatori, connettori, pressure sensor, S&H, output/chorus.

Supporterebbe: flussante scuro, pad sollevati, filo/jumper non documentato, taglio pista non isolato, valore resistenza diverso da schema/ECR, saldatura crepata.

Escluderebbe: board pulita, revision e modifiche coerenti con documenti, continuita' verificata e nessun segno di riparazione nelle aree sospette.

Componenti/net/pagine: `board_revisions_ecr.md`, `pvs_service` pagine 4/5/6, ECR738 pagina 2, ECR739 pagina 4.

### H. Problema normalizzazione connettori/jack

Perche compatibile: connettori e jack ossidati o normalizzazioni difettose possono lasciare passare segnale, introdurre rumore, cambiare canale o alterare riferimenti. L'ossidazione e' plausibile dopo anni di inutilizzo.

Area da ispezionare: connettori tra digital/analog e S&H/output, jack output/aux/footswitch/MIDI, `P402/P403`, `P302/P305`, `P901`, `P3908`, `P4093`.

Supporterebbe: sintomo che cambia muovendo o reinserendo cavi/connettori, differenze tra uscite, contatti ossidati o meccanicamente lenti.

Escluderebbe: contatti puliti, continuita' affidabile, nessun cambiamento muovendo cablaggi e localizzazione elettrica del difetto altrove.

Componenti/net/pagine: `connectors.md`, `pvs_service` pagine 4, 6, 9, 11.

### I. Surriscaldamento dei regolatori `U301/U302/U303` sul dissipatore/case

Perche compatibile: un regolatore caldo puo' essere effetto di carico eccessivo, condensatore in perdita/corto, rail disturbato, tensione di ingresso troppo alta o cattivo accoppiamento termico. Se il rail disturbato alimenta CV/audio/reset, puo' contribuire al bleed; se invece il rail e' elettricamente sano, puo' essere un secondo problema separato.

Area da ispezionare: `U301 7805` su `+5VD`, `U302 7812` su `+12V`, `U303 7912` su `-12V`, condensatori e diodi/rectifier/filtro vicini, cablaggio, vite, isolamento, rondella, mica/pasta termica e contatto col case.

Supporterebbe: temperatura anomala solo su un regolatore, Vin/Vout/ripple fuori norma, corrente assorbita alta sul rail, condensatore caldo o in perdita, caduta Vin-Vout elevata, isolamento termico montato male.

Escluderebbe: temperatura coerente con carico previsto, rail puliti e assorbimento normale, problema audio/CV localizzato altrove.

Componenti/net/pagine: `U301/U302/U303`, `+5VD`, `+12V`, `-12V`, `C301/C304/C305/C307/C308/C309`, `pvs_service` pagine 4/5, `sci_prophet_vs_ecr739` pagina 4, `IMG_5543.jpg`.

## 4. Controlli sicuri e non invasivi da fare prima

- Ispezione visiva a strumento spento: componenti anneriti, crepati, montati al contrario, condensatori gonfi/in perdita, saldature opache, pad sollevati, piste tagliate, jumper e flussante.
- Reinserimento/reseating prudente dei connettori, senza forzare plastica o pad vecchi.
- Controllo corrosione/ruggine evidente intorno a MIDI, footswitch, aux, jack output, connettori tra board.
- Controllo revisione board e confronto con ECR738/ECR739: resistenze annotate, tagli piste, jumper, qualita' delle saldature.
- Controllo rail alimentazione con la dovuta cautela e solo su punti accessibili, evitando l'area mains/trasformatore se non si e' qualificati.
- Test di ascolto: confronto tra uscita dry e chorus/output, canale left/right, cuffie/line se applicabile.
- Inizializzazione patch e confronto tra patch inizializzata e factory patch: annotare se il bleed segue envelope/LFO/modulation matrix o se resta fisso.
- Verifica comportamento del pot volume: capire se il segnale residuo e' prima o dopo il volume control, senza sostituire il potenziometro a priori.
- Identificazione visiva dei tre regolatori su `IMG_5543.jpg`: `U301 7805`, `U302 7812`, `U303 7912`; la designator map indica sinistra->destra `U301/U302/U303`, da confermare sulla PCB reale se la serigrafia e' visibile.
- Controllo segni di stress termico intorno a `U301/U302/U303`, condensatori elettrolitici/tantalio vicini, diodi/rectifier/filtro e connettori.
- Controllo che vite, isolamento, rondella, pasta termica e contatto con dissipatore/case siano corretti per il package e per il tipo di regolatore installato.

## 5. Misure per tecnico qualificato

- Misurare rail `+5VD`, `+12V`, `-12V`, `+8V`, `+5.6V`, `-5V` e ripple, con massa corretta e puntali sicuri.
- Per `U301 7805`, `U302 7812`, `U303 7912`: misurare tensione ingresso, tensione uscita, ripple, caduta Vin-Vout, temperatura e corrente/carico se misurabile in sicurezza.
- Confrontare la temperatura tra i tre regolatori, senza concludere automaticamente che quello piu' caldo sia guasto.
- Controllare assorbimento a valle dei rail `+5VD`, `+12V`, `-12V`, cercando eventuale carico anomalo o IC/condensatore che scalda.
- Controllare condensatori in perdita/corto e diodi/rectifier/filtro nella sezione del rail interessato.
- Osservare il comportamento della CV VCA quando il volume e' a zero e quando il sintomo e' presente.
- Osservare le uscite sample & hold, soprattutto `VCA/VCF/PAN/LEV`, per droop, rumore, ripple, livelli DC errati o modulazione non prevista.
- Verificare DAC/riferimenti e timing `INH` solo dopo aver confermato rail stabili.
- Controllare op amp/output per uscite bloccate, saturate, con DC offset o rumore anomalo.
- Misurare concettualmente `PRESSURE/SENSOR`, `TP301/TP302` e i valori delle reti `R321`, `R307/R308/R309/R320/R304`, `R458` quando pertinenti.
- Verificare continuita' di piste tagliate/jumper ECR e continuita' ground `AGND/DGND` secondo schema, senza creare ponti accidentali.

Non dare per scontato lato mains: trasformatore, primario, cablaggi AC e zone esposte vanno trattati solo da tecnico qualificato con strumenti e isolamento appropriati.

## 6. Rilevanza ECR738/ECR739

ECR738 e ECR739 sono rilevanti perche toccano aree pressure/aftertouch e, nel caso di ECR739, anche keyboard/power/reset. Non sono automaticamente la causa del bleed o del regolatore caldo: indicano pero' zone dove una modifica mancata, parziale o fatta male puo' introdurre offset, CV fuori scala, rumore, instabilita' o saldature fragili.

ECR738 mostra l'area pressure sensor sul lato main analog/sample & hold, con `U459`, `R458`, rail `+12V/-12V` e vicinanza alle uscite CEM5530. ECR739 mostra la pressure circuit su digital/keyboard con `U310`, rete `R321/R307/R308/R309/R320/R304`, `TP301/TP302`, e la sezione alimentazione `U301/U302/U303/U304`.

La verifica corretta e':

- controllare se le modifiche sono presenti sulla board reale;
- controllare se i valori fisici corrispondono a schema/ECR;
- ispezionare tagli piste e jumper;
- misurare rail e CV prima di attribuire il sintomo a un componente raro.

## 7. Componenti/aree da attenzionare

| Area | Componenti/net | Perche rilevante | Pagina sorgente |
| --- | --- | --- | --- |
| Regolatori principali su dissipatore/case | `U301 7805`, `U302 7812`, `U303 7912`; rail `+5VD`, `+12V`, `-12V`; ordine fisico sinistra->destra dalla designator map `pvs_service` pagina 5 | Uno dei tre scalda troppo; se il rail ha ripple, carico eccessivo o caduta Vin-Vout anomala puo' disturbare audio/CV/reset o essere un guasto separato | `pvs_service` pagine 4/5, `sci_prophet_vs_ecr739` pagina 4, `IMG_5543.jpg` |
| Reset e power digital/keyboard | `U304 78L05`, `U305 HC132`, `RESET`, `+5VD`, `DGND` | Reset o logica instabili possono alterare refresh CV, inizializzazione e comportamento digitale | `pvs_service` pagina 4, `sci_prophet_vs_ecr739` pagina 4, `power_reset.md` |
| Rail analogici locali S&H | `U401 7905`, `U402 78M05`, `U450 78M08`; rail `-5V`, `+5.6V`, `+8V`, `+12V`, `-12V` | Alimentano e polarizzano S&H/CV; ripple o rail bassi possono causare CV errate e bleed | `pvs_service` pagina 6, `power_rails.md` |
| Sample & hold / CV generation | CEM5530 `U449/U425`, `U451`, `U453/U454`, net `DAC`, `INH`, `VCA/VCF/PAN/LEV`, `RIGHT FINAL CV` | Droop, hold step o timing/riferimenti errati possono lasciare VCA aperto o introdurre modulazione | `pvs_service` pagina 6, `5530` pagine 1/3/4, `sample_hold_cv.md` |
| VCA/VCF/PAN audio path | `U455/U456/U457/U458`, net `VCA`, `VCF`, `PAN`, `LEFT`, `RIGHT`, R/C pagina 9 | Area diretta per audio distorto, VCA che non chiude o pan/level anomali | `pvs_service` pagina 9, `audio_path.md`, `named_nets.md` |
| Output/chorus/lowpass | `U903/U904/U920`, `TL082`, net `LEFT`, `RIGHT`, `CHORUS`, `LEFT CHORUS`, `RIGHT CHORUS`, `LEV` | Se il bleed appare dopo il controllo volume, output/chorus/op amp/filtro possono essere il punto di rientro | `pvs_service` pagine 11/12, `audio_path.md` |
| Pressure/aftertouch | `U310`, `U459`, `R321`, `R307/R308/R309/R320/R304`, `R458`, `PRESSURE`, `SENSOR`, `TP301/TP302` | Pressure o ECR errate possono contaminare CV o produrre modulazioni indesiderate | `pvs_service` pagine 4/6, `sci_prophet_vs_ecr738` pagina 2, `sci_prophet_vs_ecr739` pagina 4 |
| Interconnessioni e test point | `P402/P403`, `P302/P305`, `P303`, `P901`, `P3908`, `P4093`, `TP301/TP302` | Connettori ossidati o lenti possono creare intermittenti, ground incerti, audio/CV che cambia muovendo cavi | `connectors.md`, `pvs_service` pagine 4/6/9/11 |
| Condensatori e reti vicine ai rail | `C301`, `C304`, `C305`, `C307`, `C308`, `C309`, `C401/C402`, C9xx/R9xx output | Condensatori in perdita/corto o ESR elevata possono aumentare carico, ripple, distorsione o bleed | `resistors_caps.md`, `pvs_service` pagine 4/6/11/12, `sci_prophet_vs_ecr739` pagina 4 |

## 8. Domande da fare al riparatore

- Puoi verificare se le modifiche ECR738/ECR739 sono presenti e fatte correttamente?
- Puoi controllare rail e ripple prima di sostituire IC a caso?
- Puoi verificare se il bleed e' prima o dopo il potenziometro volume/output stage?
- Puoi controllare con oscilloscopio le linee CV rilevanti e il controllo VCA?
- Puoi ispezionare solder bridge, piste sollevate o riparazioni precedenti?
- Puoi identificare fisicamente i tre regolatori sul dissipatore/case (`U301/U302/U303`) e dirmi quale dei tre scalda?
- Puoi misurare Vin/Vout/ripple e caduta termica sui regolatori, e verificare se c'e' carico eccessivo a valle?
- Puoi controllare condensatori/diodi/ponte rettificatore e IC alimentati dal rail del regolatore caldo?
- Puoi verificare isolamento, vite, rondelle e pasta termica del regolatore sul dissipatore/case?
- Puoi confrontare il comportamento su patch inizializzata e factory patch?
- Puoi evitare recap generalizzato se le misure non indicano problemi ai condensatori?

## 9. Conclusione

Ordine diagnostico consigliato:

1. Separare elettricamente il sintomo audio/CV dal sintomo termico: identificare quale regolatore scalda e quale rail alimenta.
2. Misurare rail e ripple, perche un rail disturbato puo' spiegare sia riscaldamento sia comportamento audio/CV anomalo.
3. Se i rail sono corretti, seguire il bleed: prima/dopo volume, VCA, S&H/CV, output/chorus.
4. Controllare ECR738/ECR739 e riparazioni precedenti solo come aree sospette, non come diagnosi gia' decisa.

Il bleed/distorsione puo' venire da audio path, CV VCA, S&H o output/chorus. Il regolatore caldo puo' essere una causa comune se il rail e' basso/rumoroso o se un carico a valle disturba la macchina. Puo' pero' anche essere un secondo problema separato: la cosa importante e' non sostituire componenti a catena prima di avere rail, ripple, temperature e punto di ingresso del bleed misurati.
