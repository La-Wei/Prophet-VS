# Resistenze e condensatori utili

| Riferimento | Area | Perche interessa | Sorgenti |
| --- | --- | --- | --- |
| `R458` | Pressure sensor lato main analog | ECR738 la mostra vicino a `U459`; valore da verificare fisicamente | pvs_service pagina 6, ECR738 pagina 2 |
| `R321` | Pressure circuit | Offset pressure; visibile come riferimento chiave nella rete `U310` | pvs_service pagina 4, ECR739 pagina 4 |
| `R307/R308/R309/R320/R304` | Pressure circuit | Rete resistenze pressure; valori errati o ECR fatta male possono alterare `PRESSURE/SENSOR` | pvs_service pagina 4, ECR739 pagina 4 |
| `C301/C304/C305/C307/C308/C309` | Power supply digital/keyboard | Condensatori vicini alla sezione `U301/U302/U303`; un corto/perdita puo' caricare il regolatore caldo | pvs_service pagine 4/5, ECR739 pagina 4 |
| `C401/C402` | Rail analogici locali | Condensatori vicino a regolatori locali S&H; controllare polarita', ripple e perdita | pvs_service pagina 6 |
| `C9xx/R9xx` | Chorus/output | Reti output/chorus; possibili cause di bleed, distorsione o differenza canali | pvs_service pagine 11/12 |
| `R462/R463/R476`, `C4124/C4162` | VCA/VCF/PAN audio | Reti nel percorso voce; ispezionare per saldature o componenti alterati | pvs_service pagina 9 |
