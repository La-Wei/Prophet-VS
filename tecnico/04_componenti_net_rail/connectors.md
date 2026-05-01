# Connettori e test point utili

| Riferimento | Area | Perche interessa | Sorgenti |
| --- | --- | --- | --- |
| `P402/P403` | Main analog S&H / pressure | Interconnessione tra sensor, CV e rail; utile per tracciamento non invasivo | pvs_service pagina 6 |
| `P302/P305` | Digital/analog interconnect | Collegano aree keyboard/power e analog/S&H; ossidazione o falso contatto puo' creare sintomi strani | pvs_service pagine 4/6 |
| `P303` | Keyboard/power | Visibile nella sezione pressure/power | pvs_service pagina 4, ECR739 pagina 4 |
| `P901`, `P3908`, `P4093` | Output/chorus/audio | Utili se il difetto cambia tra uscite o canali | pvs_service pagine 9/11 |
| `TP301/TP302` | Pressure circuit | Test point legati a pressure/sensor; utili per verificare ECR e comportamento aftertouch | pvs_service pagina 4, ECR739 pagina 4 |
| 4 jack 1/4" posteriori | Output audio e footswitch | Ossido o normalizzazione difettosa puo' introdurre rumore, bleed o falsi contatti; non sono tutti equivalenti elettricamente | Vedi `../01_problemi_e_fix/jack_sostituzione.md` |
| 3 porte MIDI DIN | `MIDI IN`, `MIDI OUT`, `MIDI OUT/THRU` | Corrosione o contatti laschi possono bloccare MIDI; `MIDI OUT/THRU` e' l'area rugginosa indicata dall'utente | pvs_service pagina 3; vedi `../01_problemi_e_fix/pannello_posteriore_ricambi.md` |
| Eventuale slide switch `MIDI OUT/THRU` | Selettore OUT/THRU vicino alla porta MIDI | Se presente fisicamente sulla macchina, cercare un SP3T/right-angle low-current con stesso footprint; non dedurre dal solo schema | Verifica fisica; vedi `../01_problemi_e_fix/pannello_posteriore_ricambi.md` |
| `S1/S2/F1` posteriori | Power switch, selettore tensione, fuse | Nota separata: se anche questi fossero rugginosi sono mains e vanno trattati con cautela | pvs_service pagina 4 |
