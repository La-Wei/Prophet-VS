# Rail utili

| Rail | Dove compare | Perche interessa | Cosa controllare |
| --- | --- | --- | --- |
| `+5VD` | pvs_service pagine 4/6, ECR739 pagina 4 | Rail digitale; legato a `U301 7805`, reset/logica e refresh CV | Tensione, ripple, carico a valle, temperatura `U301` |
| `+12V` | pvs_service pagine 4/6/12, ECR739 pagina 4 | Rail analogico/op amp e rail del regolatore `U302 7812` | Tensione, ripple, Vin/Vout `U302`, carico audio/CV |
| `-12V` | pvs_service pagine 4/6/12, ECR739 pagina 4 | Rail analogico/op amp e rail del regolatore `U303 7912` | Tensione, ripple, Vin/Vout `U303`, carico audio/CV |
| `+8V` | pvs_service pagina 6 | Rail locale S&H/CV/output; generato vicino a `U450 78M08` | Stabilita', ripple, effetto su CEM5530 e chorus/final CV |
| `+5.6V` | pvs_service pagina 6 | Rail/riferimento locale analogico S&H | Stabilita' e rumore sulle CV |
| `-5V` | pvs_service pagina 6 | Rail locale analogico vicino a `U401 7905` | Stabilita', ripple e carico a valle |
| `AGND/DGND` | pvs_service pagine 4/6, ECR739 pagina 4 | Ground analogico/digitale; ground difettoso puo' causare bleed/rumore | Continuita' secondo schema, senza creare ponti accidentali |
