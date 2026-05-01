# Cause possibili e fix consigliati

Questa e' la pagina da leggere per prima. Non e' una diagnosi certa: e' una lista ordinata di ipotesi, prove e interventi ragionevoli da far fare a un tecnico.

## Problema 1: audio/modulazione passa con volume a zero

| Priorita | Possibile causa | Come verificarla | Fix possibile |
| --- | --- | --- | --- |
| Alta | Segnale che rientra dopo il controllo volume | Seguire il segnale prima/dopo volume e confrontare left/right, dry/chorus/output | Riparare punto di accoppiamento, jack/connettore, saldatura o componente nello stadio output |
| Alta | VCA che non chiude per CV errata | Misurare CV `VCA` a volume zero e durante il bleed | Correggere la causa della CV errata: S&H, riferimento, rail, saldatura, componente nel percorso VCA |
| Alta | S&H/CEM5530 con droop, ripple o timing errato | Osservare uscite `VCA/VCF/PAN/LEV`, `INH`, DAC/riferimenti e rail locali | Riparare rail locali, timing/logica o componente S&H solo dopo prova strumentale |
| Media | Chorus/output/op amp che lascia passare o distorce | Confrontare uscita dry/chorus, canali left/right, DC offset e saturazione op amp | Riparare op amp, condensatori o reti R/C dello stadio output/chorus se misurati difettosi |
| Media | Rail analogici/digitali rumorosi o bassi | Misurare `+5VD`, `+12V`, `-12V`, `+8V`, `+5.6V`, `-5V` e ripple | Riparare alimentazione, condensatori, diodi/rectifier, ground o carico a valle |
| Media | Pressure/aftertouch che contamina CV | Misurare `PRESSURE/SENSOR`, `TP301/TP302`, valori ECR e risposta aftertouch | Correggere rete pressure, saldature, connettori o modifiche ECR fatte male |
| Media | Riparazione precedente / ECR sbagliata | Ispezione di jumper, tagli piste, pad sollevati, valori resistenze | Rifare la riparazione in modo pulito seguendo schema e board reale |

Prima prova pratica: capire se il bleed e' gia' presente prima del volume oppure nasce dopo. Questo decide se partire da VCA/S&H o da output/chorus.

## Problema 2: case caldo / regolatore che scalda troppo

I tre TO-220 nella foto `../foto/IMG_5543.jpg` sono regolatori:

- sinistra: `U301 7805`, rail `+5VD`
- centro: `U302 7812`, rail `+12V`
- destra: `U303 7912`, rail `-12V`

| Priorita | Possibile causa | Come verificarla | Fix possibile |
| --- | --- | --- | --- |
| Alta | Carico eccessivo a valle del rail caldo | Identificare quale regolatore scalda, misurare corrente/carico e cercare IC o condensatore caldo | Riparare o sostituire il componente a valle che assorbe troppo |
| Alta | Condensatore in perdita/corto sul rail | Misurare ripple, resistenza a freddo, temperatura dei condensatori vicini | Sostituire solo i condensatori difettosi o sospetti con evidenza |
| Alta | Caduta Vin-Vout troppo alta sul regolatore | Misurare ingresso, uscita e temperatura del regolatore | Correggere causa a monte o dissipazione; non basta montare un regolatore piu grosso |
| Media | Rectifier/filtro a monte difettoso | Misurare ripple ingresso regolatore e controllare diodi/ponte/filtro | Riparare rettifica/filtro se fuori norma |
| Media | Montaggio termico errato | Controllare vite, isolamento, mica/rondella, pasta termica e contatto col case | Rimontare correttamente il regolatore sul dissipatore/case |
| Media | Parte sostituita non equivalente o montata male | Verificare pinout, isolamento tab, saldature e riferimento esatto | Correggere componente/montaggio, poi rimisurare rail e temperatura |
| Media | Ground o riparazione precedente difettosa | Controllare continuita' `AGND/DGND`, pad e jumper nell'area alimentazione | Rifare saldature, piste o jumper solo dove misurato difettoso |

Nota importante: il regolatore caldo e' gia' stato sostituito con uno piu capiente. Quindi il fix non e' "metterne uno ancora piu grande" finche non si misura cosa lo sta facendo dissipare.

## Ordine di lavoro consigliato

1. Ispezione visiva a strumento spento: regolatori, condensatori, connettori, zone ECR e output.
2. Identificare quale regolatore scalda: `U301`, `U302` o `U303`.
3. Misurare rail, ripple, Vin/Vout e temperatura prima di toccare IC audio o S&H.
4. Se i rail sono sani, seguire il bleed: volume -> VCA -> S&H/CV -> output/chorus.
5. Se un rail e' rumoroso o caricato, risolvere prima alimentazione/carico a valle.
6. Evitare recap o sostituzione IC a tappeto senza misura.

## File da aprire subito

- `technician_briefing_volume_zero_bleed.md`
- `quick_navigation_map.md`
- `../02_checklist_misure/visual_inspection_checklist.md`
- `../02_checklist_misure/safe_measurement_plan.md`
