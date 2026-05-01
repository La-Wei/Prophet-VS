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

Accorgimenti sensati:

- usare un dissipatore adesivo per IC/DIP, o piccolo dissipatore alettato a basso profilo;
- preferire adesivo/pad termico elettricamente isolante;
- non far toccare dissipatore e pin;
- verificare altezza e chiusura del case;
- misurare temperatura prima/dopo, non andare a sensazione;
- evitare ventole o masse pesanti appese al chip.

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

- 2 dissipatori adesivi bassi per IC `CEM5530` originali, se restano montati;
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
- Straylight Engineering, update Jan 2023: `https://www.straylightengineering.com/update-jan-2023/`
- Straylight Engineering, vecchia pagina clone 5530: `https://www.straylightengineering.com/5530-clone-boards-available-new-design/`
- Synthelectro ELD5530 / CEM5530 replacement: `https://synthelectro-fr.blogspot.com/2014/06/`
- Synthelectro Prophet VS memory upgrade con due `ELD5530`: `https://synthelectro-fr.blogspot.com/2015/07/how-to-upgrade-programm-memory-of.html`
