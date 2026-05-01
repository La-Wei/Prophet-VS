# Net utili

| Net | Area | Perche interessa | Sorgenti |
| --- | --- | --- | --- |
| `VCA` | S&H -> VCA | Se non raggiunge il livello di chiusura, puo' lasciare passare audio a volume zero | pvs_service pagine 6/9 |
| `VCF` | S&H -> filtro | CV errata puo' alterare timbro o creare comportamento patch/modulazione strano | pvs_service pagine 6/9 |
| `PAN` | S&H -> pan/audio | Drift o errore puo' cambiare bilanciamento left/right | pvs_service pagine 6/9 |
| `LEV` | S&H/output | Livelli/final CV; utile per bleed o output anomalo | pvs_service pagine 6/12 |
| `LEFT/RIGHT` | Audio path | Percorso canali; utile per capire se il difetto e' mono, stereo o output-specifico | pvs_service pagine 9/11/12 |
| `CHORUS`, `LEFT CHORUS`, `RIGHT CHORUS` | Chorus/output | Se il difetto cambia con chorus/output, partire da qui | pvs_service pagine 6/11/12 |
| `PRESSURE/SENSOR` | Pressure/aftertouch | CV pressure fuori scala puo' contaminare controlli o modulazioni | pvs_service pagine 4/6, ECR738 pagina 2, ECR739 pagina 4 |
| `INH` | S&H timing | Timing errato puo' creare droop/hold error o CV non stabili | pvs_service pagina 6, 5530 pagina 4 |
| `DAC` | S&H input | DAC/riferimento rumoroso o errato si riflette su molte CV | pvs_service pagina 6, 5530 pagine 1/3 |
| `RESET` | Logica/reset | Rail/reset instabili possono alterare inizializzazione e controllo CV | pvs_service pagina 4, ECR739 pagina 4 |
