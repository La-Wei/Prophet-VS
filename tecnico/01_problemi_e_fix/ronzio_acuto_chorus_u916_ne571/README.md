# Ronzio acuto nel chorus, bypass U916 e NE571

## Scopo
Nota pratica per diagnosticare il chorus del Prophet VS quando, con chorus
inserito, si sente un ronzio acuto tipo "mosca".

Questo sintomo non va liquidato come normale rumore BBD: un BBD puo' essere
rumoroso, ma di solito produce fruscio/grana morbida, non un ronzio acuto e
insistente. Il bypass dell'ultimo integrato della catena puo' essere stato utile
come prova per far ripassare segnale, ma il chorus in questa condizione non e'
ripristinato come da progetto.

Il service manual mostra che il Prophet VS usa due `NE571` fisici nel chorus:
non sono due soppressori ridondanti, ma due parti del sistema compander.

Il `NE571` comprime/condiziona il segnale prima del BBD e lo riespande dopo il
BBD. Serve a tenere corretti livello e dinamica e a limitare quanto rumore o
clock residue della linea delay arriva all'uscita.

## Riferimenti service manual
- `../../05_pagine_rilevanti/immagini/pvs_service/page_006.png`: S&H/CV,
  `LEFT CHORUS CV`, `RIGHT CHORUS CV`, `LEFT CHORUS ON`, `RIGHT CHORUS ON`
- `../../05_pagine_rilevanti/immagini/pvs_service/page_011.png`: `LEFT CHORUS`
- `../../05_pagine_rilevanti/immagini/pvs_service/page_012.png`: `RIGHT CHORUS`
- `../../05_pagine_rilevanti/note/pvs_service/page_006.md`
- `../../05_pagine_rilevanti/note/pvs_service/page_011.md`
- `../../05_pagine_rilevanti/note/pvs_service/page_012.md`
- `../../06_pdf_originali/pvs_service.pdf`: pagine 6, 11 e 12

## Flusso chorus
- `U903 NE571`: primo stadio compander, prima della linea BBD.
- `U916 NE571`: secondo stadio compander, dopo BBD e filtri, prima dello switch
  chorus ON e dell'uscita audio.

```text
LEFT/RIGHT VOICES
-> U903 NE571
-> filtri 7 kHz
-> BBD 3209
-> filtri 7 kHz
-> U916 NE571
-> U918 4007 / chorus ON
-> uscita audio
```

## Lettura del bypass
Il bypass riferito e' sull'ultimo integrato della catena chorus, quindi va
interpretato come bypass di `U916`, il secondo `NE571`.

Dato osservato:
- prima del bypass il chorus era muto;
- sono stati provati piu' `NE571` sostitutivi, circa 5, senza risolvere;
- bypassando l'ultimo integrato della catena il chorus torna a passare, ma con
  ronzio acuto.

Questa combinazione sposta il sospetto dal singolo chip alla zona che lo fa
lavorare:
- zoccolo di `U916`, contatti lenti/ossidati, pin piegati, saldature crepate;
- alimentazione, decoupling e bias di `U916`;
- resistenze/condensatori della rete esterna del compander;
- pista o piazzola interrotta;
- uscita di `U916` caricata o bloccata da un guasto successivo;
- ricambi `NE571` non affidabili, fake o non realmente equivalenti.

Se il bypass salta solo `U916` e lascia ancora nel percorso `U918 4007`, il test
indica che il wet signal esiste a monte e che BBD/filtri generano almeno un
segnale udibile. Se invece il bypass salta anche `U918` o parte del routing,
vanno controllati anche consenso chorus ON e switch.

## Tre aree da separare
- Audio wet: `U903 -> filtri -> 3209 -> filtri -> U916 -> U918 -> uscita`.
- Clock/modulazione BBD: `7555`, `4013`, `3209`, clock trim,
  `LEFT/RIGHT CHORUS CV`.
- Consenso chorus ON: `LEFT CHORUS ON`, `RIGHT CHORUS ON`, `U918 4007`.

Un guasto al compander puo' zittire il wet signal. Un guasto al clock puo'
lasciare il wet muto o produrre ronzio acuto. Un guasto al consenso ON puo'
impedire l'inserimento del chorus anche se il wet signal esiste.

## Ronzio acuto
Nel service:
- left clock: `U912 7555` + `U913 4013` -> `U911 3209`
- right clock: `U906 7555` + `U907 4013` -> `U909 3209`
- annotazione schema: `400 kHz - 40 kHz`
- filtri audio indicati come `7 kHz LOWPASS`

Se dopo il bypass compare il ronzio acuto, le ipotesi principali sono:
- il bypass ha tolto `U916`, cioe' lo stadio che doveva ripristinare
  livello/rumore dopo il BBD;
- il ronzio era gia' generato a monte da clock/filtro/BBD, ma prima non era
  udibile perche' il ramo wet veniva bloccato;
- un filtro post-BBD o una rete attorno a `U916` non sta tagliando/gestendo
  correttamente il clock residue.

## Misure consigliate
Usare sonda x10, massa corta e attenzione a non cortocircuitare pin vicini.
Annotare se il difetto e' left, right o entrambi.

1. Documentare esattamente il bypass: quali pin/componenti sono stati uniti e
   se `U918 4007` e' ancora nel percorso.
2. Verificare rail nell'area chorus: `+12V`, `-12V`, `+8V LEFT/RT`, `+5V`.
3. Con `U916` montato, misurare alimentazione, decoupling e bias. Lo schema
   indica riferimenti intorno a circa `1.8V` sugli ingressi del compander.
4. Controllare zoccolo, saldature, piste e continuita' da ogni pin di `U916`
   ai componenti esterni vicini.
5. Cercare segnale all'ingresso di `U916`:
   - left: lato `C957 .22`;
   - right: lato `C954 .22`.
6. Cercare segnale all'uscita di `U916`, con bypass rimosso:
   - left: `U916` pin 7, poi `C911`;
   - right: `U916` pin 10, poi `C966`.
7. Misurare clock BBD:
   - left: `U912` pin 3, `U913` Q/Qbar, `U911` `CP1/CP2`;
   - right: `U906` pin 3, `U907` Q/Qbar, `U909` `CP1/CP2`.
8. Cercare il ronzio prima e dopo i filtri 7 kHz post-BBD.
9. Verificare lo switch chorus:
   - `U918 4007`, controlli `LEFT CHORUS ON` e `RIGHT CHORUS ON`.
10. Verificare le CV chorus da pagina 6:
   - `LEFT CHORUS CV`;
   - `RIGHT CHORUS CV`.

## Interpretazione rapida
| Misura | Interpretazione probabile |
| --- | --- |
| Segnale presente a ingresso `U916` ma assente a pin 7/10 | `U916`, alimentazione, bias, zoccolo o rete esterna |
| Piu' `NE571` sostituiti senza cambiamento | Sospetto su zoccolo, alimentazione, bias, rete esterna o ricambi fake |
| Ronzio gia' prima di `U916` | BBD, clock, filtro post-BBD o rail |
| Ronzio assente prima ma presente dopo `U916` | `U916` o rete esterna/bias |
| Segnale assente gia' a ingresso `U916` | Cercare prima: BBD, clock, filtri, `U903` |
| Ronzio solo dopo `U918 4007` | Switch/controllo chorus ON/routing |
| Ronzio su entrambi i canali | Rail, clock control comune o disturbo comune |
| Ronzio su un solo canale | Ramo left/right specifico: BBD, filtro, `U916` half, switch |

## Componenti da controllare attorno a U916
Left:
- ingresso: `C957 .22`, rete `R979/R980/R997`
- uscita: `U916` pin 7 -> `C911 1.0`
- rete timing/bias: `C989 220pF`, `C979 1.0`, `R981 2.2M`

Right:
- ingresso: `C954 .22`, rete `R978/R973/R995`
- uscita: `U916` pin 10 -> `C966 1.0`
- rete timing/bias: `C974 220pF`, `C975 1.0`, `R972 2.2M`

Da verificare sullo schema/board reale prima di sostituire: l'OCR del manuale e'
imperfetto, l'immagine dello schema e la serigrafia vanno considerate fonte
primaria.

## Conclusione operativa
Il bypass di `U916` e' una prova diagnostica utile per far passare il wet signal
e restringere il guasto, ma non e' una riparazione definitiva: senza `U916` il
chorus non lavora come previsto dal service manual.

Con piu' `NE571` gia' provati senza risultato, non conviene continuare a
cambiare integrati. La priorita' e' misurare `U916` pin-per-pin con integrato
montato e verificare zoccolo, alimentazione, bias, componenti esterni, piste e
carico in uscita. Solo dopo va inseguito il ronzio acuto residuo come possibile
problema separato di clock/filtro/BBD.
