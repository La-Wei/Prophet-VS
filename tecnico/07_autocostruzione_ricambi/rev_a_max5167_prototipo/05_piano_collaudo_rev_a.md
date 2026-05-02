# Piano collaudo Rev A

## Regola

Non montare il modulo nel Prophet VS finche non supera questo piano fuori macchina.

## Strumenti

- alimentatore da banco con limitazione corrente;
- oscilloscopio;
- multimetro;
- generatore o DAC di prova per `VIN`;
- generatore logico o microcontrollore per `A0..A4` e `INH`;
- carichi resistivi `5k`, `10k`, `47k`;
- opzionale: logic analyzer;
- opzionale: termocamera o termometro IR.

## Test 0 - ispezione

1. Controllare orientamento U1.
2. Controllare ponti di stagno sul 48-TQFP.
3. Controllare continuita' J1 pin per pin.
4. Verificare che `OUT30/OUT31` siano solo su test pad.
5. Verificare che `VDD_IN` non sia in corto con `+10V_A`.
6. Verificare che non ci siano corti tra `+10V_A`, `+5V_L`, `-5V_A`, `GND`.

## Test 1 - alimentazioni senza U1

Se possibile, prima alimentare il PCB senza `U1` montato o con `U1` non alimentato.

1. Applicare `+8V_IN`, `-5V_IN`, `GND_IN` con corrente limitata.
2. Misurare `+5V_L`.
3. Misurare `+11V_PRE`.
4. Misurare `+10V_A`.
5. Misurare ripple su `+10V_A`.
6. Spegnere/accendere piu volte guardando overshoot.

Fail immediato:

- `+10V_A` supera target in modo incontrollato;
- `+10V_A - (-5V_A)` si avvicina/supera il limite assoluto del `MAX5167`;
- il boost oscilla o scalda senza carico.

## Test 2 - alimentazioni con U1

1. Alimentare con corrente limitata bassa.
2. Salire gradualmente al valore nominale.
3. Misurare assorbimento su `+8V_IN` e `-5V_IN`.
4. Misurare `+10V_A`, `+5V_L`, `-5V_A`.
5. Lasciare acceso 30 minuti.
6. Ripetere per 60 minuti se stabile.

Annotare temperatura di U1, U2, U3, U4.

## Test 3 - logica base

1. Tenere `CONFIG` low e `SELECT` high.
2. Applicare address statico.
3. Applicare `INH` high: tutte le uscite devono restare in hold.
4. Portare `INH` low: solo il canale indirizzato deve campionare.
5. Tornare `INH` high: il canale deve mantenere il valore.

## Test 4 - sequenza canali

Per ogni canale 0-29:

1. Impostare address.
2. Mettere `VIN` a un valore noto.
3. Impulsare `INH` low.
4. Tornare `INH` high.
5. Misurare uscita corrispondente.
6. Verificare che i canali vicini non cambino.

Pattern consigliato:

- canali pari: `+2.0V`;
- canali dispari: `-2.0V`;
- poi ripetere con rampa o valori casuali.

## Test 5 - droop e hold

1. Campionare `+3V` su un canale.
2. Tenere `INH` high.
3. Misurare uscita dopo 1 s, 10 s, 60 s.
4. Ripetere su `CV0`, `CV15`, `CV29`.
5. Ripetere con carichi `47k`, `10k`, `5k`.

## Test 6 - carico e stabilita'

Per `CV0`, `CV15`, `CV29`:

1. Test a vuoto.
2. Test con `47k`.
3. Test con `10k`.
4. Test con `5k`.
5. Osservare ringing/oscillazioni al passaggio sample/hold.
6. Provare resistenza serie uscita `100R` solo se serve.

## Test 7 - timing Prophet simulato

Simulare, per quanto possibile, il timing osservato sul Prophet:

- address update;
- stabilizzazione `VIN`;
- `INH low`;
- `INH high`;
- passaggio al canale successivo.

Se il modulo acquisisce male solo con timing veloce, non installarlo nel synth. Valutare U5 solo dopo aver misurato il timing reale.

## Test 8 - installazione controllata

Solo dopo i test fuori macchina:

1. Sostituire eventuale socket doppia lira con tulip se fragile.
2. Installare un solo modulo, preferibilmente nel socket meno critico dopo diagnosi.
3. Alimentare e controllare corrente/temperatura.
4. Misurare rail locali sul modulo installato.
5. Verificare audio e CV.
6. Spegnere e ispezionare temperatura.
7. Solo dopo ripetere per il secondo modulo.

## Log collaudo

| Test | Esito | Note |
| --- | --- | --- |
| 0 ispezione | da fare | |
| 1 alimentazioni senza U1 | da fare | |
| 2 alimentazioni con U1 | da fare | |
| 3 logica base | da fare | |
| 4 sequenza canali | da fare | |
| 5 droop | da fare | |
| 6 carico | da fare | |
| 7 timing simulato | da fare | |
| 8 installazione | da fare | |
