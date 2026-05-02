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

Opzioni da considerare, in ordine pratico:

1. Straylight Engineering `CEM5530 replacement modules`: alternativa moderna piu concreta da verificare direttamente col produttore. Straylight indicava ancora moduli `CEM5530` disponibili nel post "Update Jan 2023"; disponibilita' attuale da confermare prima dell'ordine.
2. `ELD5530` di Eric Penot / Synthelectro: clone storico per Prophet VS e Studio 440. La versione 2 e' descritta come sostituzione diretta, basata su IC Maxim Integrated e con gestione alimentazioni integrata. Disponibilita' attuale da verificare.
3. Vecchie board Wine Country / NMC / Cantos / SSM2300: esistono come storia di riparazione, ma non vanno considerate disponibili senza contatto diretto.
4. Vecchie board basate su `PD508/CEM5508`: funzionano come concetto, ma anche quei chip sono rari e vecchi.
5. `CEM5530` originale NOS o pull: comprare solo da fonte affidabile, testato, evitando componenti recuperati non garantiti.

Nota: non ho trovato un prodotto `CEM5530` su Electric Druid. La sigla da cercare e' probabilmente `ELD5530`, legata a Synthelectro/Eric Penot, non "Electric Druid".

## Dissipatori e temperatura

Nei forum sul Prophet VS ricorre lo stesso consiglio: i `CEM5530` scaldano e conviene aggiungere un piccolo dissipatore sui chip originali.

Il datasheet/pinout mostra un package a `44` pin. Nel Prophet VS servono due dissipatori identici, uno per `U449` e uno per `U425`.

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
- DigiKey, Aavid/Boyd `508700B00000G`: `https://www.digikey.com/en/products/detail/boyd-laconia-llc/508700B00000G/373763`
- Mouser, Aavid `508700B00000G`: `https://www.mouser.com/ProductDetail/Aavid/508700B00000G?qs=2v7q0MSBcBOClotXj3TAvQ%3D%3D`
- Farnell, Fischer Elektronik `ICK 40 B`: `https://es.farnell.com/fischer-elektronik/ick-40-b/disipador-de-calor-dip-pegado/dp/4620926`
- DigiKey, 3M `8810-0.5-5`: `https://www.digikey.com/en/products/detail/3m-tc/8810-0-5-5/2649860`
- DigiKey, 3M `8810-0.75-5`: `https://www.digikey.com/en/products/detail/3m-tc/8810-0-75-5/2649863`
- Straylight Engineering, update Jan 2023: `https://www.straylightengineering.com/update-jan-2023/`
- Straylight Engineering, vecchia pagina clone 5530: `https://www.straylightengineering.com/5530-clone-boards-available-new-design/`
- Synthelectro ELD5530 / CEM5530 replacement: `https://synthelectro-fr.blogspot.com/2014/06/`
- Synthelectro Prophet VS memory upgrade con due `ELD5530`: `https://synthelectro-fr.blogspot.com/2015/07/how-to-upgrade-programm-memory-of.html`
