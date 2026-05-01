# Pannello posteriore: jack, MIDI e switch

## Decisione sui jack 1/4"

I 4 jack 1/4" posteriori hanno plastica rotta: sostituirli tutti.

Ricambio candidato:

- Jalco `YKB21-5078`
- 1/4" / 6.3 mm PCB
- stereo con switch
- filetto `M12x1`
- equivalenti dichiarati: `HLJ-2305`, `HTJ-064-16D`

Link sorgente: `https://www.synth-parts.com/en/products/connectors-and-cable/14-phone-jack/5460/ykb21-5078-phone-jack-1/4-6.3-mm-for-printed-circuits-stereo`

Compra: 4 pezzi, piu eventuali dadi `M12x1`.

## Porta/selettore MIDI OUT/THRU

Chiarimento utente: il componente rugginoso e' quello dell'area `MIDI OUT/THRU`, non il selettore tensione.

Il Prophet VS ha tre connessioni MIDI 5 poli DIN:

- `MIDI IN`
- `MIDI OUT`
- `MIDI OUT/THRU`

Il service mostra il circuito MIDI sulla pagina `pvs_service` 3:

- `U333 68B50`: UART MIDI;
- `U312 PC900`: optoisolatore MIDI IN;
- `Q302`: driver `MIDI OUT`;
- `Q301`: driver `MIDI OUT/THRU`.

Quindi la zona da controllare e' pagina `pvs_service` 3, non la pagina alimentazione.

## Se e' la presa DIN `MIDI OUT/THRU`

Se e' arrugginita la presa DIN femmina:

1. testare MIDI OUT e MIDI THRU con cavi buoni;
2. ispezionare pin, schermatura metallica, saldature e piazzole;
3. se la ruggine e' estesa o i contatti sono instabili, sostituire la presa.

Il service non basta per garantire il footprint meccanico dei DIN. Prima di ordinare bisogna guardare la board reale e capire se i MIDI sono:

1. un blocco triplo integrato, tre DIN in un solo corpo;
2. tre prese DIN singole separate;
3. una variante ruotata o con pinout diverso.

Ricambi candidati, da confermare fisicamente:

- se e' un blocco triplo: Jalco `YKF51-5046`, triple female MIDI DIN socket for PCB;
- se sono singoli: Jalco `YKF51-5050` o altra presa DIN femmina 5 poli PCB con stesso footprint, stessa altezza e stessa distanza pannello.

Fonti ricambio:

- `https://www.synth-parts.com/en/products/connectors-and-cable/din-sockest-and-plugs/6651/e-mu-triple-female-midi-socket-for-pcb-jalco-ykf51-5046`
- `https://www.synth-parts.com/en/products/connectors-and-cable/din-sockest-and-plugs/6721/din-female-5-pin-midi-for-pcb-ykf51-5050`
- `https://www.synth-parts.com/en/products/connectors-and-cable/din-sockest-and-plugs/`

Nota importante: `YKF51-5046` e' venduto per E-Mu/Korg/Roland/Yamaha, non come ricambio Prophet VS specifico. Il venditore avvisa che esistono versioni ruotate di 180 gradi. Non comprarlo come "sicuro" senza foto e misura della board reale.

## Se e' il piccolo switch `MIDI OUT/THRU`

Se il componente rugginoso e' proprio un piccolo slide switch vicino alla porta `MIDI OUT/THRU`, cercare come:

- slide switch right-angle PCB;
- `SP3T` / `1P3T`;
- funzione `ON-ON-ON`;
- low-current signal switch, non mains;
- stesso footprint, stessa altezza leva, stesso passo pin, stessi eventuali pin di ancoraggio.

Candidati da confrontare, non da comprare alla cieca:

- C&K `OS103011MA7QP1C`: SP3T, through-hole, right angle, PC pin;
- C&K `AYZ0103AGRLC`: SP3T, SMD/gull wing, right angle;
- Same Sky/CUI `SLW-1516255-6A-RA-D`: SP3T, through-hole, right angle;
- generici `SS-13F16` / `SS-13F24`: SP3T, through-hole, right angle.

Fonte utile ma non Prophet VS: una discussione Gearspace su Prophet 2000 descrive il selettore MIDI Thru/Out come slide switch right-angle `SP3T`. Questo aiuta la ricerca della famiglia componente, ma non prova il footprint del Prophet VS.

Fonte: `https://gearspace.com/board/geekzone/1421716-prophet-2000-need-help-finding-replacement-part.html`

## Test funzionale

Prima di dissaldare:

1. con MIDI monitor, verificare `MIDI OUT` separato;
2. verificare `MIDI OUT/THRU` nelle posizioni disponibili;
3. muovere leggermente plug/switch: se il segnale cade o diventa intermittente, il componente e' da sostituire;
4. se la ruggine e' sullo switch, misurare continuita' tra comune e contatti in ogni posizione.

## Nota separata: power e selettore tensione

Sul retro esistono anche componenti mains:

- `S1`: power switch;
- `S2`: selettore tensione `110/220`;
- `F1`: fuse.

Questi non sono l'oggetto indicato dall'utente, ma se risultano rugginosi vanno controllati come parti di rete AC.

## Lista acquisto pratica

Da comprare subito se il footprint jack e' confermato:

- 4 x Jalco `YKB21-5078`
- dadi `M12x1` di scorta, se non inclusi o se quelli originali sono ossidati

Da comprare solo dopo foto/misura:

- MIDI DIN triplo `YKF51-5046` oppure tre DIN singoli 5 poli equivalenti;
- eventuale slide switch `MIDI OUT/THRU` SP3T/right-angle con footprint identico.

Da non fare:

- non montare jack MIDI generici se non entrano perfettamente nel pannello;
- non ordinare un blocco triplo MIDI se sulla board ci sono tre DIN separati;
- non ordinare uno switch SP3T solo perche ha la stessa funzione: deve combaciare fisicamente;
- non lasciare la presa/switch `MIDI OUT/THRU` rugginosa se il contatto e' intermittente.
