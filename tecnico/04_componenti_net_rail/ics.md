# IC e regolatori utili

| Riferimento | Area | Perche interessa | Sorgenti |
| --- | --- | --- | --- |
| `U301 7805` | Alimentazione digital/keyboard | Regolatore `+5VD`; uno dei tre TO-220 sul dissipatore/case | pvs_service pagina 4/5, ECR739 pagina 4 |
| `U302 7812` | Alimentazione digital/keyboard | Regolatore `+12V`; uno dei tre TO-220 sul dissipatore/case | pvs_service pagina 4/5, ECR739 pagina 4 |
| `U303 7912` | Alimentazione digital/keyboard | Regolatore `-12V`; uno dei tre TO-220 sul dissipatore/case | pvs_service pagina 4/5, ECR739 pagina 4 |
| `U304 78L05` | Alimentazione/reset | Regolatore locale nella sezione keyboard/power | pvs_service pagina 4, ECR739 pagina 4 |
| `U305 HC132` | Reset/logica | Reset gate; rail instabili possono creare comportamenti digitali strani | pvs_service pagina 4, ECR739 pagina 4 |
| `U310` | Pressure circuit | Op amp/IC nel circuito pressure lato keyboard/power | pvs_service pagina 4, ECR739 pagina 4 |
| `U459` | Pressure sensor | Op amp pressure lato main analog/S&H; vicino a R458/ECR738 | pvs_service pagina 6, ECR738 pagina 2 |
| `U449/U425 CEM5530` | Sample & hold / CV | Generano CV `VCA/VCF/PAN/LEV` e chorus/final CV; candidati per droop/modulation leak | pvs_service pagina 6, 5530 pagine 1/3/4 |
| `5508.pdf` | Riferimento S&H | Datasheet S&H supplementare utile per concetti di hold/droop/timing; non prova che PD508/5508 sia montato nello strumento | PDF in `06_pdf_originali/` |
| `U451` | DAC/riferimento S&H | Parte del percorso DAC verso CEM5530 | pvs_service pagina 6 |
| `U453/U454` | Timing/logica S&H | Logica associata a controllo/timing CV | pvs_service pagina 6 |
| `U401 7905`, `U402 78M05`, `U450 78M08` | Rail analogici locali | Generano rail locali per S&H/CV; ripple qui puo' causare CV errate | pvs_service pagina 6 |
| `U455-U458` | VCF/VCA/PAN audio path | Area diretta per bleed, VCA che non chiude o audio distorto | pvs_service pagina 9 |
| `U903/U904/U920` | Chorus/output | Output/chorus left-right; possibile bleed dopo volume | pvs_service pagina 11 |
| `TL082` | Output/lowpass | Op amp nel percorso output/right/lowpass | pvs_service pagina 12 |
