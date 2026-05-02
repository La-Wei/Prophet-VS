# Moduli Straylight X5530 trovati

Data nota: 2026-05-02.

## Identificazione dalla foto

La foto utente mostra due schede verdi marchiate:

- `X5530`;
- `Straylight Engineering`;
- data/lotto visibile `2018`;
- quattro IC Analog Devices `SMP18` per scheda.

Conclusione pratica: questi sembrano **due moduli Straylight Engineering X5530**, cioe' moduli sostitutivi/cloni per `CEM5530`.

Non sono `ELD5530` Synthelectro e non sono il prototipo `MAX5167` della repo. Sono una terza pista concreta, probabilmente gia' pronta all'uso se integra e correttamente compatibile.

## Perche sono compatibili come architettura

Il `CEM5530` originale e' un sample & hold multiplexato a `30` canali.

Ogni `SMP18` e' un sample & hold ottale, quindi:

```text
4 x SMP18 = 4 x 8 canali = 32 canali
```

Questo combacia con l'idea di sostituire un `CEM5530` a `30` canali usando quattro IC ottali e lasciando due canali non usati o gestiti dalla logica della scheda.

Fonte IC: Analog Devices descrive `SMP18` come `Fast Acquisition Octal Sample-and-Hold with Multiplexed Input`: `https://www.analog.com/en/products/smp18.html`

Fonte modulo: Straylight Engineering documenta una nuova board clone `5530` prodotta come PCB a 4 layer/factory assembled: `https://www.straylightengineering.com/5530-clone-boards-available-new-design/`

## Cosa cambia per il piano

Se questi due moduli sono fisicamente integri, la priorita' cambia:

1. non comprare subito `ELD5530` o altri cloni;
2. far verificare questi due moduli al tecnico;
3. contattare Straylight solo per confermare istruzioni, orientamento e note installazione se necessario;
4. usare il progetto `MAX5167` solo come backup/documentazione, non come prima strada.

Il Prophet VS usa due `CEM5530`, in posizioni `U449` e `U425`. Quindi una coppia di moduli `X5530` e' potenzialmente il set completo richiesto dalla macchina.

## Controlli prima di montarli

Non montarli direttamente solo perche sembrano corretti.

Chiedere al tecnico di verificare:

- foto fronte/retro e laterale di entrambi i moduli;
- presenza e rettilineita' dei pin maschio;
- nessun pin piegato, ossidato o spezzato;
- nessun corto visibile tra pin o saldature;
- nessun componente staccato o scheda flessa;
- verso pin 1 del modulo e verso pin 1 del socket `CEM5530`;
- compatibilita' meccanica con lo spazio disponibile sopra `U449/U425`;
- stato dei socket originali Prophet VS: se double-lyre fragili, valutare socket tulip di qualita';
- continuita' di base su alimentazioni e GND prima dell'inserimento;
- eventuale assorbimento anomalo con test fuori macchina, se il tecnico ha fixture adatta.

## Dissipatori sui cloni X5530

Non aggiungere automaticamente i dissipatori pensati per i `CEM5530` originali.

Il consiglio dei dissipatori riguarda soprattutto il chip originale in package lungo `40` pin, che concentra calore su un solo corpo DIP. Il modulo `X5530` e' diverso:

- usa quattro `SMP18` SOIC distribuiti sulla scheda;
- la dissipazione e' divisa su piu IC e sulla PCB;
- un dissipatore `40-DIP` non si applica meccanicamente al modulo;
- piccoli dissipatori incollati sui singoli SOIC possono toccare pin, aumentare altezza o stressare le saldature.

Quindi, salvo istruzioni Straylight o misura termica reale:

1. montare il modulo senza dissipatori aggiunti;
2. verificare temperatura dopo accensione controllata;
3. confrontare i due moduli tra loro;
4. se un `SMP18` o una zona della scheda scalda molto piu dell'altra, spegnere e diagnosticare rail/orientamento/modulo;
5. non incollare dissipatori permanenti prima di avere misure.

Una leggera temperatura sui `SMP18` puo' essere normale. Un modulo troppo caldo al tatto, con assorbimento anomalo o rail che crollano, non va "curato" col dissipatore: va spento e diagnosticato.

## Installazione raccomandata

Sequenza prudente:

1. diagnosticare se il problema riguarda `U449`, `U425` o entrambi;
2. salvare foto dei `CEM5530` originali montati, con orientamento pin 1;
3. spegnere e scollegare completamente il Prophet VS;
4. rimuovere un solo `CEM5530` alla volta;
5. se il socket e' fragile, sostituirlo prima di provare il modulo;
6. inserire un solo `X5530`, rispettando pin 1;
7. accendere con controllo corrente/temperatura;
8. verificare rail, CV e comportamento audio;
9. solo dopo ripetere sul secondo socket.

## Nota acquisti

Con questi due moduli in mano, le email di acquisto diventano secondarie.

Usare `contatti_acquisto_eld5530_cem5530.md` solo per:

- chiedere conferma installazione a Straylight;
- comprare ricambi solo se questi moduli risultano danneggiati;
- cercare un secondo set di backup.

## Da comunicare al tecnico

Messaggio breve:

```text
I found two Straylight Engineering X5530 modules dated 2018.
They appear to be CEM5530 replacement modules based on four Analog Devices SMP18
octal sample-and-hold ICs per board. Please verify pin-1 orientation, socket
condition, mechanical clearance, shorts, and basic power/GND continuity before
installing them in U449/U425.
```
