# Power rails

| Riferimento / Net | Visto in pagina sorgente | Funzione / contesto | Note / incertezza |
| --- | --- | --- | --- |
| +5VD | pvs_service pagine 3-4, 6 | Logica digitale | Rail digitale, possibile causa di reset o refresh CV se basso/ripple. |
| +12V / -12V | pvs_service pagine 4, 6, 12 | Rail analogici/op amp e alimentazione | Rilevanti per headroom op amp e S&H; misurare con cautela. |
| +8V / +5.6V / -5V | pvs_service pagina 6 | Rail locali main analog/S&H | Visibili vicino a regolatori 78M08/78M05/7905. |
| AGND / DGND | pvs_service pagine 4, 6 | Ground analogico/digitale | Contaminazione o connessioni difettose possono causare bleed/rumore. |
| +12V | pvs_service pagina 4; pvs_service pagina 6; pvs_service pagina 9; pvs_service pagina 12; sci_prophet_vs_ecr738 pagina 2; sci_prophet_vs_ecr739 pagina 4 | OCR/immagine: contesto da verificare nella page note | Estratto automaticamente; possibili falsi OCR. |
| +5.6V | pvs_service pagina 6 | OCR/immagine: contesto da verificare nella page note | Estratto automaticamente; possibili falsi OCR. |
| +5V | 5508 pagina 1; 5508 pagina 2; 5530 pagina 1; 5530 pagina 3; pvs_service pagina 1; pvs_service pagina 2; pvs_service pagina 3; pvs_service pagina 4; ... 13 occorrenze | OCR/immagine: contesto da verificare nella page note | Estratto automaticamente; possibili falsi OCR. |
| +8V | 5508 pagina 2; 5530 pagina 3; pvs_service pagina 1; pvs_service pagina 6; pvs_service pagina 11; pvs_service pagina 12; sci_prophet_vs_ecr738 pagina 2 | OCR/immagine: contesto da verificare nella page note | Estratto automaticamente; possibili falsi OCR. |
| -12V | 5530 pagina 3; pvs_service pagina 4; pvs_service pagina 6; pvs_service pagina 12; sci_prophet_vs_ecr738 pagina 2; sci_prophet_vs_ecr739 pagina 4 | OCR/immagine: contesto da verificare nella page note | Estratto automaticamente; possibili falsi OCR. |
| -5V | 5508 pagina 2; 5508 pagina 4; 5530 pagina 3; pvs_service pagina 6 | OCR/immagine: contesto da verificare nella page note | Estratto automaticamente; possibili falsi OCR. |
| AGND | pvs_service pagina 4; pvs_service pagina 6; sci_prophet_vs_ecr739 pagina 4 | OCR/immagine: contesto da verificare nella page note | Estratto automaticamente; possibili falsi OCR. |
| DGND | pvs_service pagina 4; pvs_service pagina 6; sci_prophet_vs_ecr739 pagina 4 | OCR/immagine: contesto da verificare nella page note | Estratto automaticamente; possibili falsi OCR. |
| GND | pvs_service pagina 1; pvs_service pagina 2; pvs_service pagina 3; pvs_service pagina 4; pvs_service pagina 6; pvs_service pagina 7; pvs_service pagina 9; pvs_service pagina 10; ... 10 occorrenze | OCR/immagine: contesto da verificare nella page note | Estratto automaticamente; possibili falsi OCR. |
| VDD | 5530 pagina 3 | OCR/immagine: contesto da verificare nella page note | Estratto automaticamente; possibili falsi OCR. |
| VREF | pvs_service pagina 6 | OCR/immagine: contesto da verificare nella page note | Estratto automaticamente; possibili falsi OCR. |
| VSS | 5508 pagina 1; 5508 pagina 2; 5508 pagina 4; 5530 pagina 3; pvs_service pagina 6; pvs_service pagina 7; pvs_service pagina 8; pvs_service pagina 11; ... 10 occorrenze | OCR/immagine: contesto da verificare nella page note | Estratto automaticamente; possibili falsi OCR. |
