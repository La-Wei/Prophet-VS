# Pannello posteriore: jack, MIDI e switch

## Decisione sui jack 1/4"

I 4 jack 1/4" posteriori hanno plastica rotta: sostituirli tutti.

Foto locali aggiornate:

- `../foto/jack_pcb_01.JPG`
- `../foto/jack_pcb_02.JPG`
- `../foto/midi_din_originale_01.JPG`

Ricambio candidato:

- Jalco `YKB21-5078`
- 1/4" / 6.3 mm PCB
- stereo con switch
- filetto `M12x1`
- equivalenti dichiarati: `HLJ-2305`, `HTJ-064-16D`

Link sorgente: `https://www.synth-parts.com/en/products/connectors-and-cable/14-phone-jack/5460/ykb21-5078-phone-jack-1/4-6.3-mm-for-printed-circuits-stereo`

Jack mono Synth-Parts, solo se i footswitch risultano davvero mono e con footprint diverso:

- Jalco `YKB21-5076`, mono con switch, PCB, filetto `M12x1`: `https://www.synth-parts.com/en/products/connectors-and-cable/14-phone-jack/5475/ykb21-5076-phone-jack-1/4-6.3-mm-pcb-mono`
- Jalco `YKB21-5012`, mono con switch, PCB, filetto `M12x1`: `https://www.synth-parts.com/en/products/connectors-and-cable/14-phone-jack/5461/ykb21-5012-phone-jack-1/4-6.3-mm-for-printed-circuits-mono`

Compra: se tutti e 4 i footprint sono uguali, 4 pezzi `YKB21-5078`; se i due footswitch sono footprint mono, 2 stereo `YKB21-5078` piu 2 mono da scegliere tra `YKB21-5076`/`YKB21-5012` dopo misure.

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

Aggiornamento dalle foto: `../foto/midi_din_originale_01.JPG` mostra una presa DIN 5 poli diversa dai ricambi Jalco PCB gia linkati. Si vede un corpo con inserto rosso/fenolico, contatti lunghi piegati verso la PCB e due flange/orecchie di fissaggio. Quindi `YKF51-5050` e `YKF51-5046` non vanno ordinati come ricambi sicuri.

Il service non basta per garantire il footprint meccanico dei DIN. Prima di ordinare bisogna guardare la board reale e capire se i MIDI sono:

1. un blocco triplo integrato, tre DIN in un solo corpo;
2. tre prese DIN singole separate;
3. una DIN panel/chassis mount con terminali lunghi piegati/saldati in PCB, come sembra dalla nuova foto;
4. una variante ruotata o con pinout diverso.

Ricambi candidati, da confermare fisicamente:

- se e' un blocco triplo: Jalco `YKF51-5046`, triple female MIDI DIN socket for PCB, ma le foto nuove non puntano a questa soluzione;
- se sono singoli PCB moderni: Jalco `YKF51-5050` o `BCTE5P1-5211`, ma le foto nuove non sembrano combaciare;
- se e' come in foto: cercare una DIN femmina 5 poli `180 degree`, panel/chassis mount o PCB right-angle con flange, terminali solder/PC lunghi e stessa geometria.

Fonti ricambio:

- `https://www.synth-parts.com/en/products/connectors-and-cable/din-sockest-and-plugs/6651/e-mu-triple-female-midi-socket-for-pcb-jalco-ykf51-5046`
- `https://www.synth-parts.com/en/products/connectors-and-cable/din-sockest-and-plugs/6721/din-female-5-pin-midi-for-pcb-ykf51-5050`
- `https://www.synth-parts.com/en/products/connectors-and-cable/din-sockest-and-plugs/5442/din-female-5-pin-midi-for-printed-circuits`
- `https://www.synth-parts.com/en/products/connectors-and-cable/din-sockest-and-plugs/`

Nota importante: i link Synth-Parts sopra sono ora **solo confronto**, non ricambio confermato per il Prophet VS fotografato. Dalle foto bisogna cercare un ricambio con stessa meccanica, non solo "DIN MIDI 5 pin".

### Pista MIDI piu concreta dopo le foto

La pista piu concreta non e' Synth-Parts/Jalco, ma una DIN femmina 5 poli `180 degree` di famiglia Switchcraft DIN panel/PC mount.

Candidati Switchcraft da confrontare per primi:

- `57NC5FX`: DIN panel mount, 5 contatti a 180 gradi, terminali PC/thru-hole. E' il candidato piu interessante se il tecnico vuole terminali da PCB.
- `57GB5FX`: DIN panel mount, 5 contatti a 180 gradi, terminali solder cup/flared solder. E' interessante se l'originale ha terminali lunghi/saldabili da formare verso la PCB.
- `57PC5F`: DIN femmina right-angle PC mount, 5 contatti a 180 gradi, contact arrangement F. Da confrontare se serve un corpo piu "PCB right-angle" invece del panel mount classico.

Link utili:

- `https://www.switchcraft.com/din-panel-mount-connector-5-contacts-at-180-pc-terminals/57nc5fx/`
- `https://www.switchcraft.com/din-panel-mount-connector-5-contacts-at-180-/57gb5fx/`
- `https://www.switchcraft.com/female-din-right-angle-pc-mount-5-contacts-at-180-contact-arrangement-f/57pc5f/`

Verdetto operativo: prima misurare/interfacciare con questi tre datasheet/foto. Se uno combacia per flange, altezza e pattern terminali, quello diventa il ricambio MIDI preferito. Se non combacia, si cerca ancora, ma almeno si e' nella famiglia giusta.

Candidati/famiglie da confrontare fuori Synth-Parts:

- Switchcraft `57GB5FX`: DIN femmina 5 contatti 180 gradi, panel mount, usata per MIDI, `https://www.performanceaudio.com/products/switchcraft-57gb5fx-5-pin-din-panel-mount-jack`;
- Lumberg `0105 05`: DIN 5 poli right-angle/PCB chassis socket, `https://cpc.farnell.com/lumberg/0105-05/din-connector-rcpt-5pos-chassis/dp/CN25115`;
- Hirschmann `MAB 5 SH`: DIN 5 poli PCB right-angle, `https://uk.farnell.com/hirschmann/mab-5-sh/socket-din-pcb-5pin/dp/1944987`;
- Deltron `671-0501`: DIN 5 poli female PCB right-angle, `https://no.rs-online.com/web/p/din-connectors/1806737`.

Questi sono candidati di ricerca: non comprarli senza misurare distanza fori, altezza rispetto al pannello, forma flange, orientamento pin e pattern dei terminali.

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

- 4 x Jalco `YKB21-5078`, se tutti e 4 i jack hanno stesso footprint stereo/switch
- oppure 2 x `YKB21-5078` + 2 x mono `YKB21-5076`/`YKB21-5012`, se i footswitch sono davvero footprint mono
- dadi `M12x1` di scorta, se non inclusi o se quelli originali sono ossidati

Da comprare solo dopo foto/misura:

- MIDI DIN: non comprare `YKF51-5050`/`YKF51-5046` come sicuri; dalle foto serve probabilmente DIN femmina 5 poli panel/PCB right-angle con flange e terminali lunghi. Prima confrontare Switchcraft `57NC5FX`, `57GB5FX`, `57PC5F`;
- eventuale slide switch `MIDI OUT/THRU` SP3T/right-angle con footprint identico.

Da non fare:

- non montare jack MIDI generici se non entrano perfettamente nel pannello;
- non ordinare un blocco triplo MIDI se sulla board ci sono tre DIN separati;
- non ordinare uno switch SP3T solo perche ha la stessa funzione: deve combaciare fisicamente;
- non lasciare la presa/switch `MIDI OUT/THRU` rugginosa se il contatto e' intermittente.
