# Progetto preliminare ELD5530 V2-like con MAX5167

## Stato del progetto

Questo documento e' una pre-progettazione tecnica per una scheda sostitutiva del `CEM5530` in stile `ELD5530 V2`.

Non e' lo schema originale ELD5530, non e' una BOM definitiva e non e' un Gerber pronto da produrre. Serve a portare il lavoro fino al punto in cui un tecnico/progettista possa disegnare lo schema in CAD, fare una revisione pin-to-pin e preparare un prototipo senza ripartire da zero.

Per il pacchetto Rev A concreto, vedere [rev_a_max5167_prototipo/README.md](rev_a_max5167_prototipo/README.md). La Rev A e' marcata come prototipo non validato.

Risposta breve alla domanda: la fonte primaria Synthelectro 2014 conferma che `ELD5530 V2` e' basato su un IC Maxim Integrated, ma non pubblica la sigla. Il forum Gearspace cita esplicitamente il `MAX5167` e il datasheet `MAX5167` combacia molto bene con la funzione richiesta. Quindi il progetto piu realistico resta `MAX5167` su PCB adattatore 40 pin, con alimentazioni locali integrate, ma va trattato come prototipo dedotto e non come replica certificata dell'ELD5530 originale.

La stessa fonte 2014 spiega anche perche' le alimentazioni locali sono obbligatorie: la prima versione del ricambio richiedeva due piccole modifiche sulla board perche' non gestiva tutte le alimentazioni; la V2 invece fornisce direttamente le tensioni necessarie e viene presentata come plug-in replacement del `CEM5530`.

Nota batteria: questa scheda sostituisce il `CEM5530` nello sample & hold/CV e non elimina la batteria memoria. La batteria sparisce solo con una mod separata alle SRAM patch non volatili; vedere `../01_problemi_e_fix/batteria_memoria_nvram.md`.

## Cosa significa "modifica" in pratica

Non si modifica fisicamente il `MAX5167` e non si modifica il silicio del `CEM5530`.

La modifica e' una **scheda adattatrice**:

```text
socket Prophet per CEM5530
  -> schedina adattatrice 40 pin
  -> MAX5167 saldato sulla schedina
  -> regolatori/filtri locali sulla schedina
  -> pin della schedina che imitano il CEM5530 originale
```

Il `MAX5167` e' il chip commerciale che fa il lavoro sample & hold. Pero' non ha:

- lo stesso package del `CEM5530`;
- la stessa piedinatura;
- le stesse alimentazioni dirette;
- solo 30 canali, perche ne ha 32;
- la stessa meccanica plug-in.

Per questo serve il CAD: non per "programmare" o "modificare" il chip, ma per disegnare la piccola PCB che converte piedinatura, alimentazioni e segnali. In pratica il tecnico non prende un `MAX5167` e lo infila nel Prophet: salda il `MAX5167` su una schedina, testa la schedina, poi inserisce la schedina al posto del `CEM5530`.

Se si trova un modulo `ELD5530` o Straylight gia finito e collaudato, il CAD non serve all'utente: si compra il modulo e si monta. Il CAD serve solo se il modulo va ricostruito.

## Come si applica sul Prophet VS

Procedura pratica ideale, se il modulo Rev A viene davvero realizzato:

1. Diagnosticare quale `CEM5530` e' guasto o sospetto: `U449`, `U425`, oppure entrambi.
2. Misurare rail, `VIN`, `INH` e address sul socket originale.
3. Costruire la schedina adattatrice `MAX5167` fuori dal synth.
4. Collaudarla su alimentatore e fixture, non nel Prophet.
5. Spegnere il Prophet, rimuovere il `CEM5530` originale dal socket.
6. Se il socket originale e' doppia lira o fragile, sostituirlo con socket tulip di qualita'.
7. Inserire la schedina adattatrice rispettando pin 1.
8. Accendere con controllo corrente/temperatura.
9. Verificare CV e audio prima di montare il secondo modulo.

Quindi la modifica visibile sulla macchina dovrebbe essere minima: togliere il vecchio chip e inserire il modulo adattatore. La parte complessa sta tutta nella piccola scheda sostitutiva.

## Vincoli non negoziabili

- Modulo plug-in al posto del `CEM5530`, senza fili esterni se possibile.
- Compatibilita' con socket `U449` e `U425` del Prophet VS.
- Footprint maschio compatibile con il `CEM5530` a `40` pin.
- Ingresso comune dal DAC/S&H Prophet verso l'ingresso sample del nuovo IC.
- `30` uscite CV operative; i due canali extra del `MAX5167` restano non usati.
- Polarita' `INH` compatibile: high = hold, low = sample/acquire.
- Alimentazioni locali pulite: il `MAX5167` non va alimentato direttamente dal rail `+8V` originale.
- Prova fuori dal synth obbligatoria prima dell'installazione.

## Confronto CEM5530 vs MAX5167

| Punto | CEM5530 | MAX5167 | Impatto sul progetto |
| --- | --- | --- | --- |
| Canali | 30 S&H | 32 S&H | `OUT30/OUT31` restano NC/test pad |
| Address | 5 bit `A0..A4` | 5 bit `ADDR0..ADDR4` | Mapping diretto, da confermare sul timing Prophet |
| Controllo | `INH` | `S/H`, `SELECT`, `CONFIG` | `INH` puo' pilotare `S/H` se `SELECT` e' reso sempre attivo |
| Sample/hold | `INH` low aggiorna il canale indirizzato; high mette in hold/auto-zero | `S/H` low sample, high hold | Polarita' compatibile |
| Rail | Nel Prophet visibili `+8V`, `-5V`, GND/AGND | `VDD +10V`, `VSS -5V`, `VL +5V` | Serve generazione locale `+10V` e `+5V` |
| Package | 40 pin | 48 pin TQFP | Serve PCB adattatore |
| Droop | Da datasheet CEM, verificare pagina 4 | Tipico `1 mV/s` | Adeguato in teoria, ma va misurato nel refresh reale |
| Acquisition | CEM: ciclo veloce, pagina 4 | Datasheet MAX: 2.5 us tipico, fino a 4 us per acquisizione accurata | Misurare larghezza reale di sample nel Prophet |
| Output impedance | Buffer interni CEM | Varianti `L/M/N`: 50R/500R/1k | Preferire footprint che consenta piccole correzioni |

## Pinout CEM5530 ricavato dalla pagina 2

Da confermare visivamente su `../05_pagine_rilevanti/immagini/5530/page_002.png` e sulla board reale prima di disegnare il PCB.

| Pin CEM5530 | Segnale |
| --- | --- |
| 1 | `VIN` |
| 2-9 | `O0..O7` |
| 10 | `INH` |
| 11 | `A4` |
| 12-19 | `O8..O15` |
| 20 | `VSS` |
| 21 | `GND` |
| 22-29 | `O16..O23` |
| 30 | `A0` |
| 31 | `A1` |
| 32 | `A2` |
| 33 | `A3` |
| 34-39 | `O24..O29` |
| 40 | `VDD` |

## Mapping proposto CEM5530 -> MAX5167

Questo e' il mapping elettrico di partenza. Prima del CAD va verificato con continuita' sullo schema `pvs_service` pagina 6 e con una prova su breadboard/fixture.

| CEM5530 | MAX5167 | Note |
| --- | --- | --- |
| pin 1 `VIN` | pin 11 `IN` | Collegamento diretto iniziale; aggiungere footprint serie `0R/100R` e pad test |
| pin 10 `INH` | pin 5 `S/H` | Polarita' compatibile: high hold, low sample |
| pin 11 `A4` | pin 3 `ADDR4` | Address bit 4 |
| pin 30 `A0` | pin 47 `ADDR0` | Address bit 0 |
| pin 31 `A1` | pin 48 `ADDR1` | Address bit 1 |
| pin 32 `A2` | pin 1 `ADDR2` | Address bit 2 |
| pin 33 `A3` | pin 2 `ADDR3` | Address bit 3 |
| pin 2 `O0` | pin 14 `OUT0` | Uscita CV 0 |
| pin 3 `O1` | pin 15 `OUT1` | Uscita CV 1 |
| pin 4 `O2` | pin 16 `OUT2` | Uscita CV 2 |
| pin 5 `O3` | pin 17 `OUT3` | Uscita CV 3 |
| pin 6 `O4` | pin 18 `OUT4` | Uscita CV 4 |
| pin 7 `O5` | pin 19 `OUT5` | Uscita CV 5 |
| pin 8 `O6` | pin 20 `OUT6` | Uscita CV 6 |
| pin 9 `O7` | pin 21 `OUT7` | Uscita CV 7 |
| pin 12 `O8` | pin 22 `OUT8` | Uscita CV 8 |
| pin 13 `O9` | pin 23 `OUT9` | Uscita CV 9 |
| pin 14 `O10` | pin 24 `OUT10` | Uscita CV 10 |
| pin 15 `O11` | pin 25 `OUT11` | Uscita CV 11 |
| pin 16 `O12` | pin 26 `OUT12` | Uscita CV 12 |
| pin 17 `O13` | pin 27 `OUT13` | Uscita CV 13 |
| pin 18 `O14` | pin 28 `OUT14` | Uscita CV 14 |
| pin 19 `O15` | pin 29 `OUT15` | Uscita CV 15 |
| pin 22 `O16` | pin 31 `OUT16` | Uscita CV 16 |
| pin 23 `O17` | pin 32 `OUT17` | Uscita CV 17 |
| pin 24 `O18` | pin 33 `OUT18` | Uscita CV 18 |
| pin 25 `O19` | pin 34 `OUT19` | Uscita CV 19 |
| pin 26 `O20` | pin 35 `OUT20` | Uscita CV 20 |
| pin 27 `O21` | pin 36 `OUT21` | Uscita CV 21 |
| pin 28 `O22` | pin 37 `OUT22` | Uscita CV 22 |
| pin 29 `O23` | pin 38 `OUT23` | Uscita CV 23 |
| pin 34 `O24` | pin 39 `OUT24` | Uscita CV 24 |
| pin 35 `O25` | pin 40 `OUT25` | Uscita CV 25 |
| pin 36 `O26` | pin 41 `OUT26` | Uscita CV 26 |
| pin 37 `O27` | pin 42 `OUT27` | Uscita CV 27 |
| pin 38 `O28` | pin 43 `OUT28` | Uscita CV 28 |
| pin 39 `O29` | pin 44 `OUT29` | Uscita CV 29 |
| n/a | pin 45 `OUT30` | NC, pad test opzionale |
| n/a | pin 46 `OUT31` | NC, pad test opzionale |
| pin 20 `VSS` | pin 9 `VSS` | Filtrare; rail `-5V` locale |
| pin 21 `GND` | pin 8 `DGND`, pin 10 `AGND` | Unione controllata, stella locale |
| pin 40 `VDD` | non diretto a MAX `VDD` | Usare come ingresso `+8V` per alimentazioni locali |
| n/a | pin 30 `VDD` | `+10V` locale regolato |
| n/a | pin 7 `VL` | `+5V` logico locale |
| n/a | pin 4 `SELECT` | Default a `VL` |
| n/a | pin 6 `CONFIG` | Default a `DGND`; cosi `SELECT` e' active-high |
| n/a | pin 12 `CH` | Default a `VDD +10V`, verificare clamp desiderato |
| n/a | pin 13 `CL` | Default a `VSS -5V`, verificare clamp desiderato |

## Schema elettrico di principio

```text
CEM5530 socket pin 40 VDD circa +8V
  -> filtro ingresso
  -> boost low-noise +11/+12V
  -> LDO/filtraggio finale +10V
  -> MAX5167 pin 30 VDD
  -> MAX5167 pin 12 CH

CEM5530 socket pin 40 VDD circa +8V
  -> LDO low-noise +5V
  -> MAX5167 pin 7 VL
  -> pull-up SELECT

CEM5530 socket pin 20 VSS circa -5V
  -> filtro ingresso
  -> MAX5167 pin 9 VSS
  -> MAX5167 pin 13 CL

CEM5530 socket pin 21 GND/AGND
  -> punto stella locale
  -> MAX5167 pin 10 AGND
  -> MAX5167 pin 8 DGND

CEM5530 pin 10 INH
  -> 47R/100R serie opzionale
  -> MAX5167 pin 5 S/H

MAX5167 pin 6 CONFIG
  -> DGND

MAX5167 pin 4 SELECT
  -> VL
```

## Alimentazioni locali

La parte piu "V2-like" e' questa: la scheda deve generare da sola le tensioni che il `MAX5167` richiede.

Proposta base:

- ingresso dal pin `VDD` CEM: misurare sul Prophet reale, atteso circa `+8V`;
- ingresso dal pin `VSS` CEM: misurare sul Prophet reale, atteso circa `-5V`;
- `+10V` analogico per `MAX5167 VDD`: generarlo con boost da `+8V`, preferibilmente seguito da filtraggio o LDO se il margine e lo spazio lo consentono;
- `+5V` logico per `MAX5167 VL`: generarlo da `+8V` con LDO locale low-noise;
- `-5V` analogico per `MAX5167 VSS`: usare il rail `VSS` esistente solo dopo filtro e misura ripple;
- `AGND/DGND`: unione locale controllata, poi ritorno al pin `GND` CEM.

Punti da non saltare:

- misurare corrente assorbita dal modulo originale se ancora funzionante;
- dimensionare il boost con margine termico, non solo con corrente teorica del datasheet;
- rispettare il limite `VDD-VSS` del `MAX5167`: con `+10V` e `-5V` si lavora gia vicino al massimo ammesso; evitare overshoot di startup, boost mal regolato o `-5V` assente durante l'accensione;
- tenere il ripple del boost lontano dall'ingresso `VIN`, dalle uscite CV e dal ground analogico;
- prevedere test pad per `+8_IN`, `-5_IN`, `+10_A`, `+5_L`, `GND`, `INH`, `VIN`.

Protezione raccomandata in revisione 1: soft-start o enable controllato del boost, clamp/TVS adeguati sui rail locali se compatibili con il rumore richiesto, e prova di accensione/spegnimento con oscilloscopio su `VDD`, `VSS`, `VL` e `GND`.

## Timing e logica

Il `MAX5167` puo' funzionare in modo molto simile al `CEM5530` se:

- `CONFIG` e' tenuto low;
- `SELECT` e' tenuto high;
- `S/H` riceve il segnale `INH`.

Con questa configurazione:

- `INH`/`S/H` high: tutti i canali in hold;
- `INH`/`S/H` low: il canale indirizzato da `ADDR0..ADDR4` campiona `IN`.

Il rischio vero non e' la polarita', ma la larghezza temporale. Nel `MAX5167` il minimo impulso digitale `S/H` e' molto breve, ma quello non basta a garantire che l'uscita abbia gia acquisito il valore analogico con precisione. Il datasheet indica acquisizione tipica `2.5 us` e fino a `4 us` per accuratezza piena: il datasheet `CEM5530` e la logica Prophet vanno quindi misurati con oscilloscopio:

- larghezza del tratto `INH` low;
- setup/hold degli address rispetto a `INH`;
- stabilizzazione del DAC prima del sample;
- tempo tra due canali successivi.

Decisione progettuale consigliata:

- primo prototipo senza stretching di `INH`, per non alterare la macchina;
- se la finestra low e' troppo breve, aggiungere solo in seconda revisione una piccola logica opzionale, abilitabile con jumper, che estenda `S/H` low senza invadere il cambio address/DAC successivo;
- non aggiungere monostabili "a sentimento": un impulso piu lungo puo' campionare il canale sbagliato.

Nota di audit: aggiungere nel CAD footprint DNP per una logica di stretching, ma popolare la revisione 1 in modalita' passiva/direct. In questo modo si lascia una via di correzione senza introdurre subito una variabile nuova.

## Uscite e carichi

Scelta iniziale consigliata: partire dal `MAX5167L` se reperibile autentico, per l'impedenza d'uscita piu bassa (`50R`). Le varianti `M` e `N` hanno impedenze piu alte e possono essere utili con carichi capacitivi, ma possono introdurre piu errore se il carico della CV e' basso.

Layout consigliato:

- footprint per resistenza serie opzionale su ogni uscita, default `0R` o DNP secondo test;
- test pad almeno su `OUT0`, `OUT15`, `OUT29`;
- `OUT30` e `OUT31` solo su test pad, non collegati al socket;
- niente condensatori verso massa sulle uscite in revisione 1, salvo footprint DNP, per non rallentare CV o caricare il chip;
- se una linea Prophet mostra carico troppo basso, prevedere buffer op amp esterno solo su revisione dedicata.

## BOM preliminare

Questa BOM e' volutamente per funzione, non per marca definitiva.

| Q.ta | Parte | Nota |
| --- | --- | --- |
| 1 | `MAX5167L` / `MAX5167M` / `MAX5167N`, 48-TQFP | Preferenza iniziale `L`; comprare solo da fonte affidabile |
| 1 | PCB adattatore 40 pin -> 48-TQFP | 4 layer consigliati: power/ground piu puliti |
| 1 | Boost converter regolato per `+10V` finale | Da `+8V`; scegliere modello low-noise e collaudabile |
| 1 | LDO/filtraggio `+10V` se si usa boost sopra `+10V` | Consigliato se lo spazio lo permette |
| 1 | LDO `+5V` logico | Da `+8V` a `VL` |
| 1 | Filtro/ferrite rail `-5V` | Prima di `MAX5167 VSS` |
| varie | Protezione startup/overshoot rail | Soft-start, enable o clamp da definire in CAD |
| 1 | Footprint DNP per stretching `S/H` | Solo se le misure Prophet mostrano sample troppo breve |
| 1 | Set pin torniti 40 pin | Maschio, passo e larghezza da misurare sul socket |
| 30 | Resistenze serie uscita opzionali | Footprint `0R/100R/470R`, default dopo test |
| 6 | Resistenze serie logica opzionali | `INH`, `A0..A4`, tipicamente `47R/100R` se servono |
| varie | Decoupling | `100nF` vicino ai pin, piu bulk `1uF/10uF` per rail |
| varie | Test pad | Rail, `VIN`, `INH`, address, uscite campione |

## Vincoli PCB

- Tenere boost converter e induttore lontani da `VIN` e dalle uscite CV.
- Ground plane continuo, con ritorno analogico pulito.
- `MAX5167` il piu vicino possibile al centro del modulo per fanout equilibrato.
- Decoupling direttamente ai pin `VDD`, `VSS`, `VL`.
- Pin header meccanicamente robusto; evitare pin economici che stressano il socket.
- Altezza massima da misurare nel Prophet reale prima di scegliere componenti.
- Orientamento pin 1 marcato in modo molto evidente sul silkscreen.
- Prevedere spazio per una label `MAX5167 V2-like, not original ELD5530`.

## Piano test prima del Prophet

1. Ispezione ottica del PCB e continuita' tra tutti i pin del finto `CEM5530`.
2. Alimentazione da banco con limitazione corrente su `+8V`, `-5V`, GND simulati.
3. Verifica rail locali: `+10V`, `+5V`, ripple e startup.
4. Verifica termica 30-60 minuti senza segnali.
5. Generatore DAC simulato su `VIN`, address manuali/logic analyzer su `A0..A4`.
6. Per ogni address 0-29: portare `S/H` low, campionare, tornare high, verificare solo il canale atteso.
7. Verificare che `OUT30/OUT31` non tocchino il socket.
8. Misurare droop su 1 minuto e su intervallo pari al refresh Prophet.
9. Misurare hold step e glitch quando si cambia address.
10. Test con carichi equivalenti alle CV Prophet: almeno `5k`, `10k`, `47k` e capacita' parassita ragionevole.
11. Solo dopo: installare un modulo alla volta nel Prophet, con alimentatore limitato o lamp/current monitor se disponibile.

## Gate prima di mandare in produzione

Non produrre piu di un prototipo finche questi punti non sono chiusi:

- rail reali misurati sui socket `U449` e `U425`;
- larghezza `INH` low/high misurata in condizioni operative;
- range reale del segnale `VIN` misurato;
- carico minimo delle linee CV piu critiche stimato o misurato;
- spazio verticale e orientamento pin 1 verificati fisicamente;
- disponibilita' reale e autenticita' del `MAX5167` verificata;
- revisione indipendente del mapping pin-to-pin.

## Esito audit

| Area | Stato | Nota |
| --- | --- | --- |
| Architettura | verde | `MAX5167` e' funzionalmente molto vicino al `CEM5530` |
| Pin mapping | giallo | Tabella pronta, ma da verificare su immagine e board reale |
| Alimentazioni | giallo | Concetto V2-like definito; part number da scegliere dopo misure |
| Timing | giallo/rosso | Polarita' ok; larghezza sample da misurare prima del PCB definitivo |
| Output/carichi | giallo | Serve misura o stima carichi CV Prophet |
| Meccanica | giallo | Serve misura altezza e socket |
| Produzione | rosso | Nessun Gerber definitivo; serve prototipo e test |

## Fonti e rimandi

- Dossier generale: [cem5530_clone_build_dossier.md](cem5530_clone_build_dossier.md)
- Rev A prototipo: [rev_a_max5167_prototipo/README.md](rev_a_max5167_prototipo/README.md)
- Datasheet CEM5530 locale: `../06_pdf_originali/5530.pdf`
- Pinout CEM5530 locale: [5530 pagina 2](../05_pagine_rilevanti/note/5530/page_002.md)
- Timing CEM5530 locale: [5530 pagina 4](../05_pagine_rilevanti/note/5530/page_004.md)
- Schema Prophet S&H/CV: [pvs_service pagina 6](../05_pagine_rilevanti/note/pvs_service/page_006.md)
- Synthelectro ELD5530 V2: `https://synthelectro-fr.blogspot.com/2014/06/cem5530-pour-prophet-vs-studio-440.html`
- Synthelectro archivio giugno 2014 con lo stesso post: `https://synthelectro-fr.blogspot.com/2014/06/`
- Analog Devices / Maxim MAX5167 product page: `https://www.analog.com/en/products/max5167l.html`
- Analog Devices / Maxim MAX5167 datasheet: `https://www.analog.com/media/en/technical-documentation/data-sheets/MAX5167-MAX5167N.pdf`
