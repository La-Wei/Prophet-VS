# CEM5530 / ELD5530: dossier per clone o ricostruzione

## Stato della ricerca

Data ricerca: 2026-05-02.

Non ho trovato schemi, Gerber, PCB layout o BOM pubblici e verificabili per `ELD5530`, Straylight `CEM5530 replacement module`, Wine Country, NMC/Cantos o vecchie board `PD508/CEM5508`.

Quello che risulta dalle fonti:

- `ELD5530` e' un modulo sostitutivo, non un `CEM5530` originale modificato.
- La pagina Synthelectro 2014 descrive una versione 2 basata su IC Maxim Integrated, con gestione alimentazioni integrata e inserimento diretto al posto del `CEM5530`; la sigla dell'IC Maxim non viene pubblicata li.
- La stessa pagina dice che la prima versione richiedeva due modifiche minori sulla board perche' non gestiva tutte le alimentazioni, mentre la versione 2 fornisce direttamente le tensioni necessarie.
- Gearspace cita una clonazione tramite Maxim `MAX5167` e riporta che qualcuno intendeva rimettere online gli schemi, ma non ho trovato quegli schemi pubblicati. Quindi `MAX5167` e' la pista tecnica piu plausibile, non una conferma ufficiale della BOM ELD5530.
- Nello stesso thread viene chiesto a Eric Penot di rilasciare specifiche complete/open source, ma non ho trovato evidenza che siano state pubblicate.
- Straylight descrive un proprio modulo `CEM5530` a PCB 4 layer prodotto in fabbrica, ma non pubblica schema o file di produzione.
- Le vecchie alternative citate nei forum includono board basate su `SSM2300` e board basate su `PD508/CEM5508`, ma anche qui senza file di progetto pubblici.

Nota batteria: la pagina Synthelectro 2015 cita sia mod SRAM non volatile sia due `ELD5530` nello stesso Prophet VS. Solo la mod SRAM non volatile elimina la batteria; `ELD5530` non riguarda la memoria patch. Vedere `../01_problemi_e_fix/batteria_memoria_nvram.md`.

Conclusione operativa: questo non e' un progetto pronto da mandare in produzione. E' un dossier per permettere a un tecnico/progettista di ricostruire un modulo con metodo, oppure di valutare un modulo acquistato.

## Documenti locali da usare

- `../06_pdf_originali/5530.pdf`: datasheet preliminare `CEM5530`.
- `../05_pagine_rilevanti/immagini/5530/page_002.png`: pinout/diagramma `CEM5530`; OCR scarso, leggere l'immagine.
- `../05_pagine_rilevanti/note/5530/page_002.md`: nota su pinout/orientamento.
- `../05_pagine_rilevanti/note/5530/page_003.md`: limiti alimentazione e swing uscite.
- `../05_pagine_rilevanti/note/5530/page_004.md`: timing `INH`, auto-zero, acquisition e droop.
- `../06_pdf_originali/pvs_service.pdf`, pagina 6: `U449/U425`, DAC, `INH`, CV `VCA/VCF/PAN/LEV`, rail locali.
- `../05_pagine_rilevanti/immagini/pvs_service/page_006.png`: schema Prophet VS dell'area S&H/CV.
- `../06_pdf_originali/5508.pdf`: datasheet `PD508/CEM5508`, utile per capire le vecchie architetture a 4 chip.

Datasheet esterni da scaricare/verificare:

- Maxim/Analog Devices `MAX5167-MAX5167N`: `https://www.analog.com/media/en/technical-documentation/data-sheets/MAX5167-MAX5167N.pdf`
- Analog Devices `MAX5167L` product page: `https://www.analog.com/en/products/max5167l.html`
- Analog Devices `SSM2300`: `https://www.analog.com/en/products/ssm2300.html`
- Analog Devices `SSM2300` obsolete datasheet: `https://www.analog.com/media/en/technical-documentation/obsolete-data-sheets/ssm2300.pdf`

## Fatti primari dal post Synthelectro 2014

Il post Synthelectro 2014 e' la fonte migliore per descrivere `ELD5530` senza mischiarlo con la mod memoria/batteria:

- `CEM5530` e' descritto come interfaccia tra processore digitale e generazione analogica;
- ogni `CEM5530` viene paragonato a `30` potenziometri comandati dal processore;
- il Prophet VS usa due `CEM5530`, per `60` segnali di controllo totali;
- lo Studio 440 usa un solo `CEM5530`;
- sul Prophet VS le posizioni sono `U449` e `U425`;
- la prima scheda sostitutiva richiedeva due modifiche minori sulla board per le alimentazioni;
- `ELD5530 V2` integra quelle alimentazioni e viene presentato come ricambio plug-in;
- i socket originali del Prophet VS sono indicati come double-lyre, meno affidabili dei tulip, con rischio rottura delle zampe/saldature;
- nella foto Synthelectro, originale e ricambio sono mostrati nello stesso verso, con pin 1 in basso a sinistra. Usare questa informazione solo insieme alla serigrafia reale.

## Requisito funzionale

Il Prophet VS monta due `CEM5530`:

- `U449`: CV legate a `VCA`, `VCF`, `PAN`, chorus/final CV e altre uscite;
- `U425`: area `LEV` e altre CV.

Ogni ricambio deve comportarsi come un `CEM5530` a `30` canali sample & hold con ingresso multiplexato, decoder/address a 5 bit, controllo `INH`, hold capacitor integrati/equivalenti e uscite compatibili con i carichi del Prophet VS.

## Schema di principio, non PCB-ready

Questo e' solo il blocco logico da progettare; non e' uno schema elettrico completo.

```text
Prophet VS socket CEM5530
  A0..A4  -------------------->  address logic  ---------->  S&H IC address
  INH     -------------------->  polarity/timing logic ---->  S&H sample/hold enable
  DAC/SWIN input ------------->  input buffer/protection -->  S&H common input
  VDD/VSS/rail locali -------->  local regulation/filter -->  S&H analog/digital rails
  AGND/DGND/ground ---------->  grounding strategy ------->  S&H grounds
  OUT0..OUT29 <---------------  S&H outputs 0..29
  unused channels <-----------  NC/clamped/held per datasheet
```

Prima di disegnare una PCB, compilare una tabella pin-to-pin reale partendo dall'immagine `5530/page_002.png` e dallo schema `pvs_service` pagina 6. L'OCR del pinout non e' affidabile.

## Architettura A: `MAX5167`

E' l'architettura piu vicina a quanto viene attribuito a `ELD5530`, ma va trattata come ipotesi tecnica: Synthelectro conferma "Maxim Integrated", non la sigla `MAX5167`.

Il `MAX5167` e' un sample & hold a `32` canali con ingresso multiplexato, 5 linee address, controllo sample/hold, uscite `OUT0..OUT31`, alimentazione analogica positiva/negativa e alimentazione logica separata. Questo lo rende concettualmente adatto a sostituire un `CEM5530` a `30` canali, ma solo tramite una schedina adattatrice.

Per la prosecuzione concreta della pista `MAX5167`, usare il progetto preliminare dedicato `max5167_v2_like_pre_design.md` e poi la cartella Rev A prototipo `rev_a_max5167_prototipo/`.

Punti da progettare/verificare:

- mapping `CEM5530 OUT0..OUT29` verso `MAX5167 OUT0..OUT29` o altra numerazione confermata;
- trattamento dei due canali extra `MAX5167`;
- polarita' e timing tra `CEM5530 INH` e ingressi `SELECT`/`S/H` del `MAX5167`;
- rail: il `MAX5167` richiede rail propri; non collegare rail Prophet a caso;
- scelta variante `MAX5167L/M/N` per impedenza uscita e compatibilita' col carico;
- disponibilita' reale del chip e rischio componenti contraffatti/obsolete;
- altezza meccanica dentro il Prophet VS.

Nota critica: la pagina Synthelectro dice che la versione 2 include la gestione delle alimentazioni necessarie. Questo e' un indizio forte che una semplice piedinatura adattata non basta.

## Architettura B: 4 x `SSM2300`

Architettura citata per vecchie board NMC/Cantos/John Leimseider.

`SSM2300` e' un sample & hold multiplexato a 8 canali. Quattro IC danno 32 canali teorici, sufficienti per emulare 30 canali `CEM5530`.

Punti da progettare/verificare:

- decode 5-bit `CEM5530` in selezione chip + indirizzo 3-bit per i quattro `SSM2300`;
- comportamento di hold per i chip non selezionati;
- compatibilita' swing uscita, droop, hold step, carico capacitivo e output buffering;
- disponibilita' `SSM2300`: il prodotto e' obsoleto, quindi eventuali chip sono NOS/pull;
- layout piu grande e maggior numero di componenti rispetto a `MAX5167`.

Questa strada e' interessante solo se il tecnico ha accesso a `SSM2300` autentici e accetta una progettazione piu complessa.

## Architettura C: 4 x `PD508/CEM5508`

Architettura storica citata per vecchie board Wine Country / emulatori anni 90.

`PD508/CEM5508` e' un octal sample & hold. Quattro chip danno 32 canali teorici, ma anche questi componenti sono rari e vecchi.

Usare `../06_pdf_originali/5508.pdf` per confrontare timing, hold, droop e carico, ma non considerarla la scelta preferita se i chip sono difficili da trovare o non testati.

## Materiali minimi da prevedere

Per un progetto vero servono almeno:

- IC S&H scelto: `MAX5167` oppure 4 x `SSM2300` oppure 4 x `PD508/CEM5508`;
- PCB adattatore con footprint maschio compatibile `CEM5530` 40 pin;
- eventuale logica glue per polarita', decode e chip-select;
- regolatori locali o riferimenti/filtri per rail richiesti dall'IC scelto;
- decoupling ravvicinato su ogni rail analogico e logico;
- connessione massa analogica/digitale ragionata, non improvvisata;
- pin/header torniti o contatti affidabili;
- socket tornito/tulip di qualita' sulla board Prophet se quello originale e' fragile;
- test fixture per provare la scheda fuori dal synth.

## Checklist di progettazione

1. Ricavare pinout `CEM5530` manualmente dall'immagine `5530/page_002.png`.
2. Verificare sul Prophet VS reale orientamento pin 1 e spazio verticale disponibile.
3. Misurare rail reali sui socket `U449/U425` prima di progettare alimentazioni.
4. Misurare con oscilloscopio `INH`, address e DAC input durante aggiornamento CV.
5. Decidere architettura e IC disponibili da fonte affidabile.
6. Disegnare schema e fare revisione incrociata pin-to-pin.
7. Prevedere protezioni/serie resistors se necessarie per output e carichi capacitivi.
8. Produrre un primo prototipo e testarlo fuori dal Prophet VS.
9. Installare un solo modulo alla volta, con controllo corrente e temperatura.
10. Confrontare CV e comportamento audio prima/dopo con patch di test.

## Test minimi fuori dal synth

- nessun corto tra rail e massa;
- assorbimento corrente coerente a freddo e a caldo;
- ogni indirizzo aggiorna solo il canale previsto;
- `INH`/sample/hold rispettano il timing del `CEM5530`;
- droop entro limiti accettabili per il refresh rate reale del Prophet VS;
- swing uscita corretto per le CV richieste;
- stabilita' con carichi simili a quelli delle CV Prophet;
- temperatura stabile dopo almeno 30-60 minuti;
- nessuna oscillazione o glitch anomalo sulle uscite hold.

## Cosa chiedere se si contatta l'autore

Messaggio utile per Synthelectro/Eric Penot:

```text
Hello,
I am repairing a Sequential Circuits Prophet VS and want to preserve it long term.
If ELD5530 modules are no longer available, would you be willing to share or sell
the schematic, PCB/Gerber files, BOM, or enough documentation for my technician
to build two replacement modules for U449 and U425?

I understand this may be a non-public design; I am not asking to publish it,
only to make a repair possible if no finished modules are available.

Thank you.
```

Messaggio utile per Straylight/Tom Virostek:

```text
Hello,
I am repairing a Sequential Circuits Prophet VS and need two CEM5530 replacement
modules for U449 and U425. If modules are no longer available, would you be
willing to share or sell documentation, schematic, Gerbers, BOM, or recommend
a way for a technician to reproduce or service the modules?

Thank you.
```

## Fonti

- Synthelectro, post 2014 `Remplacement du CEM5530 pour Prophet VS & Studio 440`: `https://synthelectro-fr.blogspot.com/2014/06/cem5530-pour-prophet-vs-studio-440.html`
- Synthelectro, archivio giugno 2014 con lo stesso post: `https://synthelectro-fr.blogspot.com/2014/06/`
- Synthelectro, post 2015 con due `ELD5530`: `https://synthelectro-fr.blogspot.com/2015/07/how-to-upgrade-programm-memory-of.html`
- Gearspace, discussione affidabilita Prophet VS e cloni `CEM5530`: `https://gearspace.com/board/electronic-music-instruments-and-electronic-music-production/724391-prophet-vs-reliability.html`
- Gearspace, pagina 2 stessa discussione: `https://gearspace.com/board/electronic-music-instruments-and-electronic-music-production/724391-prophet-vs-reliability-2.html`
- Straylight Engineering, vecchia pagina clone 5530: `https://www.straylightengineering.com/5530-clone-boards-available-new-design/`
- Straylight Engineering, update Jan 2023: `https://www.straylightengineering.com/update-jan-2023/`
- Analog Devices / Maxim `MAX5167`: `https://www.analog.com/en/products/max5167l.html`
- Analog Devices / Maxim `MAX5167` datasheet PDF: `https://www.analog.com/media/en/technical-documentation/data-sheets/MAX5167-MAX5167N.pdf`
- Analog Devices `SSM2300`: `https://www.analog.com/en/products/ssm2300.html`
- Analog Devices `SSM2300` obsolete datasheet: `https://www.analog.com/media/en/technical-documentation/obsolete-data-sheets/ssm2300.pdf`
