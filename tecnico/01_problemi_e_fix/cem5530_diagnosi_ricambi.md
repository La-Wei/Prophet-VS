# CEM5530: diagnosi, ricambi e dissipazione

## Ruolo nel Prophet VS

Il Prophet VS usa due `CEM5530` nel blocco sample & hold/CV:

- `U449`: CV legate a `VCA`, `VCF`, `PAN` e altre uscite chorus/final CV;
- `U425`: area `LEV` e altre CV di controllo.

La pagina `pvs_service` 6 e il datasheet `5530.pdf` sono le sorgenti principali. Il `CEM5530` e' un sample & hold multiplexato a 30 canali: quando un'uscita droopa, resta bloccata, e' rumorosa o viene aggiornata male, il problema puo' sembrare audio ma nascere da una CV errata.

## Sintomi compatibili

Possibili sintomi di `CEM5530`, rail o circuito S&H:

- VCA che non chiude e lascia passare audio/bleed;
- pan o livello instabile;
- modulazione percepita anche quando non dovrebbe esserci;
- filtro/VCA con comportamento diverso tra patch o voci;
- chorus/output anomalo se la CV relativa non arriva corretta;
- difetto che compare o peggiora a caldo.

Nota: i forum riportano che i `CEM5530` possono morire in modo parziale/graduale, non sempre "tutto o niente". Quindi un solo gruppo di funzioni puo' essere guasto mentre altro sembra normale.

## Cosa verificare prima di sostituire

Prima di condannare il chip:

1. misurare rail locali `+8V`, `+5.6V`, `-5V`, `+12V`, `-12V` e ripple;
2. controllare `DAC`, `INH`, address/timing e riferimenti;
3. osservare uscite `VCA/VCF/PAN/LEV` con strumento adeguato;
4. ispezionare saldature, socket, piste e jumper intorno a `U449/U425`;
5. controllare connettori tra board: i forum segnalano anche interconnect/pin e piste rotte come fonte di falsi guasti.

Se il tecnico decide di estrarre i chip, evitare molte inserzioni/rimozioni. I socket originali possono essere fragili; se si interviene, valutare socket torniti/tulip di qualita'.

## Ricambi e cloni

Opzioni da considerare, in ordine pratico. Il Prophet VS usa due moduli/chip: uno per `U449` e uno per `U425`.

### Link operativi

1. Straylight Engineering `CEM5530 replacement modules`: questa e' la pista piu chiara per comprare oggi un ricambio moderno. Nel post "What a year." Straylight scriveva che il clone `CEM5530` era ancora disponibile a `75 USD` ciascuno piu spedizione; nel post "Update Jan 2023" riportava ancora `CEM5530 replacement modules` disponibili. Prima di ordinare va comunque confermata disponibilita' attuale:
   - contact form Straylight: `https://www.straylightengineering.com/contact/`
   - disponibilita'/prezzo storico 2020: `https://www.straylightengineering.com/what-a-year/`
   - disponibilita' citata nel 2023: `https://www.straylightengineering.com/update-jan-2023/`
   - vecchia pagina progetto/design 5530: `https://www.straylightengineering.com/5530-clone-boards-available-new-design/`
   - nota sui due moduli gia trovati: `../07_autocostruzione_ricambi/straylight_x5530_moduli_trovati.md`
2. `ELD5530` di Eric Penot / Synthelectro: clone storico specifico per Prophet VS e Studio 440. Non ho trovato una pagina carrello o "buy now" attiva; questi sono quindi link di informazione/contatto col produttore originale, non un negozio automatico:
   - permalink del post Synthelectro 2014: `https://synthelectro-fr.blogspot.com/2014/06/cem5530-pour-prophet-vs-studio-440.html`
   - pagina archivio Synthelectro con il post "Remplacement du CEM5530 pour Prophet VS & Studio 440.", lunedi' 2 giugno 2014: `https://synthelectro-fr.blogspot.com/2014/06/`
   - post 2015 con Prophet VS aggiornato e due `ELD5530`: `https://synthelectro-fr.blogspot.com/2015/07/how-to-upgrade-programm-memory-of.html`
   - email pubblicata da Synthelectro nei commenti del post 2015 per richieste: `synthelectro@netcourrier.com`
3. `CEM5530` originale NOS o pull: comprare solo da fonte affidabile, testato, evitando componenti recuperati non garantiti. Non e' un clone moderno e non risolve il problema affidabilita' di base del componente vecchio.
4. Vecchie board Wine Country / NMC / Cantos / SSM2300: esistono come storia di riparazione, ma non vanno considerate disponibili senza contatto diretto.
5. Vecchie board basate su `PD508/CEM5508`: funzionano come concetto, ma anche quei chip sono rari e vecchi.

Nota importante: non ho trovato un prodotto `CEM5530` su Electric Druid. La sigla corretta da chiedere/cercare e' `ELD5530`, legata a Synthelectro/Eric Penot.

Nota batteria: i due `ELD5530` citati nel post Synthelectro 2015 non eliminano la batteria memoria. La batteria sparisce solo con la modifica separata alle SRAM non volatili; vedere `batteria_memoria_nvram.md`.

### Cosa sono davvero gli `ELD5530`

Gli `ELD5530` non sono `CEM5530` originali modificati. Sono moduli/adattatori sostitutivi che usano almeno un IC sample & hold commerciale moderno al posto del Curtis originale.

La fonte primaria Synthelectro 2014 corregge il quadro:

- la versione 2 del ricambio e' basata su un IC Maxim Integrated, ma la sigla dell'IC non viene pubblicata nella pagina;
- la prima versione era gia' una scheda che si inseriva al posto del `CEM5530`, ma non gestiva tutte le alimentazioni e richiedeva due piccole modifiche sulla board del Prophet VS o dello Studio 440;
- la versione 2 integra la generazione/gestione delle tensioni necessarie, quindi viene presentata come sostituzione plug-in del `CEM5530` guasto;
- nel Prophet VS i due `CEM5530` sono `U449` e `U425`; nello Studio 440 ce n'e' uno;
- Synthelectro segnala anche che i socket originali Prophet VS sono double-lyre, non tulip, e possono rompersi a livello saldature.

La fonte forum cita esplicitamente una clonazione del `CEM5530` con un Maxim `MAX5167`; questo resta quindi una deduzione/indizio esterno, non una sigla confermata da Synthelectro. Il datasheet Maxim/Analog Devices descrive il `MAX5167` come sample & hold a `32` canali con ingresso multiplexato, quindi e' molto vicino al ruolo del `CEM5530` nel Prophet VS, che usa `30` canali per chip.

Tradotto per il tecnico:

- non si prende un `MAX5167` e lo si infila direttamente al posto del `CEM5530`;
- serve una schedina che adatti pinout, alimentazioni, segnali di controllo, output usati/non usati e orientamento;
- se si trova un vero `ELD5530 V2`, l'idea e' rimuovere il `CEM5530` difettoso e inserire il modulo, confermando pin 1 e altezza prima di accendere;
- se il tecnico ha schema, PCB/Gerber, BOM e IC corretti puo' teoricamente costruirli;
- senza file di progetto conviene comprare moduli gia' fatti o chiedere a Synthelectro/Straylight, perche' rifarli diventa un lavoro di progettazione e test, non una normale riparazione.

Per la ricostruzione da zero, vedere anche il dossier dedicato: `../07_autocostruzione_ricambi/cem5530_clone_build_dossier.md`.

Aggiornamento: sono stati trovati due moduli `Straylight Engineering X5530` con quattro `SMP18` per scheda. Sembrano due cloni/ricambi `CEM5530` gia pronti; prima di comprare altro farli verificare al tecnico. Vedere `../07_autocostruzione_ricambi/straylight_x5530_moduli_trovati.md`.

Per contatti, priorita' e email pronte da mandare, vedere `../07_autocostruzione_ricambi/contatti_acquisto_eld5530_cem5530.md`.

Messaggio pratico da mandare a Straylight:

```text
Hello,
I need two CEM5530 replacement modules for a Sequential Circuits Prophet VS,
positions U449 and U425. Can you confirm current availability, price,
shipping to Italy, installation notes, pin-1 orientation, height clearance,
and whether replacing the original sockets with quality turned-pin/tulip
sockets is recommended?

Thank you.
```

Messaggio pratico da mandare a Synthelectro per `ELD5530`:

```text
Hello,
I own a Sequential Circuits Prophet VS and I am looking for two ELD5530
replacement modules for the original CEM5530 chips, positions U449 and U425.
Are ELD5530 modules still available? If yes, can you confirm price, shipping
to Italy, installation notes, pin-1 orientation, height clearance, and whether
socket replacement is recommended?

Thank you.
```

## Dissipatori e temperatura

Nei forum sul Prophet VS ricorre lo stesso consiglio: i `CEM5530` scaldano e conviene aggiungere un piccolo dissipatore sui chip originali.

Nota importante: questa sezione riguarda i `CEM5530` originali in package lungo `40` pin. Non applicare automaticamente gli stessi dissipatori ai moduli clone `Straylight X5530`: quei moduli usano quattro `SMP18` SOIC distribuiti sulla scheda e vanno prima misurati/verificati. Vedere `../07_autocostruzione_ricambi/straylight_x5530_moduli_trovati.md`.

Il datasheet/pinout mostra un package a `40` pin. Nel Prophet VS servono due dissipatori identici, uno per `U449` e uno per `U425`.

Misura target consigliata:

- base circa `50-51 mm` lunga, `13-14 mm` larga, altezza circa `5 mm`;
- non superare `15 mm` di larghezza senza prova a secco sul chip reale;
- evitare dissipatori alti oltre `5 mm` se non si e' verificata la chiusura del case;
- se il dissipatore e' leggermente piu corto del corpo del `CEM5530`, va bene: deve scaricare calore dal corpo centrale senza arrivare ai pin.

Ricambi sensati:

- Aavid/Boyd `508700B00000G`: `50.8 x 13.46 x 4.83 mm`, alluminio nero, per `40-DIP`, adhesive/tape non incluso. E' il formato piu sicuro come larghezza per non avvicinarsi ai pin: `https://www.digikey.com/en/products/detail/boyd-laconia-llc/508700B00000G/373763`
- Mouser per lo stesso `508700B00000G`: `https://www.mouser.com/ProductDetail/Aavid/508700B00000G?qs=2v7q0MSBcBOClotXj3TAvQ%3D%3D`
- Fischer Elektronik `ICK 40 B`: `51 x 19 x 4.8 mm`, per DIP, disponibile tramite Farnell/element14; usarlo solo se una prova a secco conferma che i `19 mm` di larghezza non toccano pin, socket o componenti vicini: `https://es.farnell.com/fischer-elektronik/ick-40-b/disipador-de-calor-dip-pegado/dp/4620926`

Adesivo/pad termico se non integrato:

- 3M `8810-0.5-5`: tape termico biadesivo `12.7 mm` largo, `0.25 mm` spesso, da tagliare a circa `50 mm` per il dissipatore Aavid/Boyd: `https://www.digikey.com/en/products/detail/3m-tc/8810-0-5-5/2649860`
- 3M `8810-0.75-5`: stessa serie, `19.05 mm` larga, adatta come misura al Fischer `ICK 40 B` se viene usato quel dissipatore: `https://www.digikey.com/en/products/detail/3m-tc/8810-0-75-5/2649863`
- 3M `8810SQ-35(100)`: pad `35 x 35 mm`, comodo se si vuole tagliare materiale in piccoli pezzi; per coprire un dissipatore lungo servono piu pezzi tagliati puliti: `https://www.digikey.com/en/products/detail/3m-tc/8810SQ-35-100/3529589`

Nota Amazon, ricerca del 2026-05-02: non sono stati aggiunti link Amazon perche non sono emersi risultati affidabili per `508700B00000G`, `ICK 40 B`, `3M 8810-0.5-5` o `3M 8810-0.75-5`. I risultati generici tipo dissipatori BGA/Raspberry o nastri VHB/montaggio non vanno considerati equivalenti se non riportano chiaramente dimensioni, uso termico, biadesivo termico ed eventuale isolamento elettrico.

Accorgimenti sensati:

- usare un dissipatore adesivo per IC/DIP, o piccolo dissipatore alettato a basso profilo;
- preferire adesivo/pad termico elettricamente isolante;
- non far toccare dissipatore e pin;
- verificare altezza e chiusura del case;
- misurare temperatura prima/dopo, non andare a sensazione;
- evitare ventole o masse pesanti appese al chip.
- se il dissipatore ha gia' pad adesivo termico integrato, non aggiungere un secondo strato;
- non usare pasta termica semplice senza fissaggio meccanico: il dissipatore potrebbe staccarsi;
- evitare adesivi caricati argento o conduttivi; se si usa epoxy termico permanente, preferire un prodotto elettricamente isolante e accettare che la rimozione sara' difficile.

Forum e vecchie note parlano anche di dissipatori neri con alette tipo vecchi Pentium-I senza ventola. Trattarlo come suggerimento di epoca/forum, non come parte obbligatoria: l'importante e' ridurre calore senza stress meccanico o corto.

## Separazione dal case caldo

Questa e' una nota termica diversa dal problema del case caldo.

- I tre TO-220 fissati al case/dissipatore sono regolatori lineari: `U301 7805`, `U302 7812`, `U303 7912`.
- I `CEM5530` sono IC sample & hold `U449/U425`; possono scaldare localmente, ma non sono "uno dei tre transistor" sul retro.
- Il dissipatore sui `CEM5530` serve a ridurre lo stress termico del chip, non a risolvere il case rovente.

Il collegamento possibile tra i due problemi e' elettrico, non meccanico/termico diretto: se un regolatore scalda perche il rail ha carico anomalo, ripple o tensione sbagliata, quel rail puo' anche disturbare l'area S&H/CV. Viceversa, un `CEM5530` guasto in modo pesante potrebbe caricare un rail, ma non e' l'ipotesi da assumere senza misure.

La pagina `5530` 3 indica che la tensione tra `VDD` e `VSS` non deve superare 16 V e che le alimentazioni influenzano lo swing input/output. Quindi:

- non abbassare o modificare rail "per far scaldare meno" senza progetto e misure;
- prima verificare che i rail siano nei valori previsti e con ripple basso;
- se un regolatore scalda troppo, cercare carico a valle, condensatore in perdita, ripple o dissipazione errata;
- se si aggiungono dissipatori ai `CEM5530`, farlo come misura conservativa per quei chip, non come sostituto della diagnosi sul regolatore caldo.

## Supporto meccanico

Un thread Gearspace segnala piste rotte sotto la board dei `5530` dovute a flessione. Per il modello keyboard:

- evitare stand che sostengono solo i lati se il fondo flette;
- usare supporto largo/continuo o flightcase che distribuisca il peso;
- quando la macchina e' aperta, controllare piste e saldature sul lato inferiore della zona `U449/U425`.

## Lista pratica

Da comprare o cercare:

- 2 dissipatori bassi per IC `CEM5530` originali, uno per `U449` e uno per `U425`;
- 2 pezzi di pad/tape termico tagliati a misura, solo se i dissipatori non hanno adesivo integrato;
- 2 ricambi `CEM5530` clone, se il budget lo permette e si vuole una riserva reale;
- socket torniti/tulip di qualita' se si dissaldano i chip o i socket originali sono fragili.

Da non fare:

- non sostituire `CEM5530` solo perche il sintomo e' strano;
- non comprare cloni senza confermare altezza, pin 1, compatibilita' Prophet VS e istruzioni di installazione;
- non usare dissipatori conduttivi o pesanti che possano cortocircuitare o flettere il chip;
- non modificare i rail senza schema, datasheet e misure.

## Fonti esterne consultate

- Gearspace, Prophet VS reliability: `https://gearspace.com/board/electronic-music-instruments-and-electronic-music-production/724391-prophet-vs-reliability.html`
- Gearspace, pagina 2 dello stesso thread: `https://gearspace.com/board/electronic-music-instruments-and-electronic-music-production/724391-prophet-vs-reliability-2.html`
- Gearspace, heatsink CEM5530: `https://gearspace.com/board/geekzone/1064015-where-can-i-find-heatsink-cem5530-chips.html`
- Analog Devices / Maxim `MAX5167L`: `https://www.analog.com/en/products/max5167l.html`
- Analog Devices / Maxim `MAX5167` datasheet PDF: `https://www.analog.com/media/en/technical-documentation/data-sheets/MAX5167-MAX5167N.pdf`
- DigiKey, Aavid/Boyd `508700B00000G`: `https://www.digikey.com/en/products/detail/boyd-laconia-llc/508700B00000G/373763`
- Mouser, Aavid `508700B00000G`: `https://www.mouser.com/ProductDetail/Aavid/508700B00000G?qs=2v7q0MSBcBOClotXj3TAvQ%3D%3D`
- Farnell, Fischer Elektronik `ICK 40 B`: `https://es.farnell.com/fischer-elektronik/ick-40-b/disipador-de-calor-dip-pegado/dp/4620926`
- DigiKey, 3M `8810-0.5-5`: `https://www.digikey.com/en/products/detail/3m-tc/8810-0-5-5/2649860`
- DigiKey, 3M `8810-0.75-5`: `https://www.digikey.com/en/products/detail/3m-tc/8810-0-75-5/2649863`
- Straylight Engineering, contact form: `https://www.straylightengineering.com/contact/`
- Straylight Engineering, prezzo storico `CEM5530` clone 2020: `https://www.straylightengineering.com/what-a-year/`
- Straylight Engineering, update Jan 2023: `https://www.straylightengineering.com/update-jan-2023/`
- Straylight Engineering, vecchia pagina clone 5530: `https://www.straylightengineering.com/5530-clone-boards-available-new-design/`
- Synthelectro ELD5530 / CEM5530 replacement: `https://synthelectro-fr.blogspot.com/2014/06/cem5530-pour-prophet-vs-studio-440.html`
- Synthelectro archivio giugno 2014 con lo stesso post: `https://synthelectro-fr.blogspot.com/2014/06/`
- Synthelectro Prophet VS memory upgrade con due `ELD5530`: `https://synthelectro-fr.blogspot.com/2015/07/how-to-upgrade-programm-memory-of.html`
