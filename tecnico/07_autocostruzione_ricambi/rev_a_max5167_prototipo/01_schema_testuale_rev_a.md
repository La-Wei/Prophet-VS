# Schema testuale Rev A

## Convenzioni

Questo documento descrive lo schema elettrico che il tecnico deve riportare in CAD.

Sigle:

- `J1`: connettore/pin maschio verso socket `CEM5530` 40 pin.
- `U1`: `MAX5167L/M/N`, 48-TQFP.
- `U2`: convertitore boost da `+8V_IN` a `+11V_PRE`.
- `U3`: regolatore/filtraggio da `+11V_PRE` a `+10V_A`.
- `U4`: LDO da `+8V_FILT` a `+5V_L`.
- `U5`: logica opzionale DNP per stretching `S/H`.
- `RN_OUT`: resistenze serie opzionali sulle uscite.
- `RN_LOGIC`: resistenze serie opzionali su address e `INH`.

## J1 - socket CEM5530

J1 deve essere un adattatore maschio compatibile con package `CEM5530` 40 pin.

| J1 pin | Net Rev A |
| --- | --- |
| 1 | `VIN_IN` |
| 2-9 | `CV0..CV7` |
| 10 | `INH_IN` |
| 11 | `A4_IN` |
| 12-19 | `CV8..CV15` |
| 20 | `VSS_IN` |
| 21 | `GND_IN` |
| 22-29 | `CV16..CV23` |
| 30 | `A0_IN` |
| 31 | `A1_IN` |
| 32 | `A2_IN` |
| 33 | `A3_IN` |
| 34-39 | `CV24..CV29` |
| 40 | `VDD_IN` |

## U1 - MAX5167

### Alimentazione U1

| U1 pin | Net |
| --- | --- |
| 7 `VL` | `+5V_L` |
| 8 `DGND` | `DGND_LOCAL` |
| 9 `VSS` | `-5V_A` |
| 10 `AGND` | `AGND_LOCAL` |
| 30 `VDD` | `+10V_A` |

`AGND_LOCAL` e `DGND_LOCAL` devono unirsi in un punto locale vicino a U1 e tornare a `GND_IN`.

### Clamp U1

| U1 pin | Net | Popolamento Rev A |
| --- | --- | --- |
| 12 `CH` | `+10V_A` | `0R` o short locale |
| 13 `CL` | `-5V_A` | `0R` o short locale |

Motivo: lasciare le clamp ai rail analogici del `MAX5167`, evitando clamp intermedie prima delle misure reali delle CV.

### Ingresso analogico

```text
J1 pin 1 VIN_IN
  -> RIN1 0R/100R footprint, default 0R
  -> TP_VIN
  -> U1 pin 11 IN
```

Non aggiungere condensatori verso massa in Rev A salvo footprint DNP: il DAC Prophet e il timing sample non vanno rallentati senza misura.

### Logica address

```text
J1 pin 30 A0_IN -> RN_LOGIC 47R/0R -> U1 pin 47 ADDR0
J1 pin 31 A1_IN -> RN_LOGIC 47R/0R -> U1 pin 48 ADDR1
J1 pin 32 A2_IN -> RN_LOGIC 47R/0R -> U1 pin 1  ADDR2
J1 pin 33 A3_IN -> RN_LOGIC 47R/0R -> U1 pin 2  ADDR3
J1 pin 11 A4_IN -> RN_LOGIC 47R/0R -> U1 pin 3  ADDR4
```

Default consigliato per il primo prototipo: `0R` o `47R`, da scegliere dopo aver visto fronti e ringing.

### Logica sample/hold

Rev A default direct:

```text
J1 pin 10 INH_IN
  -> RN_LOGIC 47R/0R
  -> JP1 posizione DIRECT
  -> U1 pin 5 S/H
```

Polarita' prevista:

- `INH_IN` high -> `S/H` high -> hold;
- `INH_IN` low -> `S/H` low -> sample del canale indirizzato.

Footprint opzionale:

```text
INH_IN -> U5 DNP stretcher/logic -> JP1 posizione STRETCH -> U1 pin 5 S/H
```

`U5` non va popolato in Rev A iniziale. Serve solo se le misure mostrano che `INH low` e' troppo breve per acquisire con precisione.

### SELECT / CONFIG

```text
U1 pin 6 CONFIG -> RCFG 10k -> DGND_LOCAL
U1 pin 4 SELECT -> RSEL 10k -> +5V_L
```

Con `CONFIG` low, `SELECT` e' active-high. Tenendolo high, `S/H` resta sempre abilitato.

## Uscite CV

Ogni uscita usata passa da un footprint serie verso il pin CEM corrispondente.

```text
U1 OUTn -> R_OUTn 0R/100R/470R footprint -> J1 CVn
```

Default consigliato per Rev A:

- popolamento iniziale: `0R`;
- usare `100R` o `470R` solo se test di carico/capacita' mostrano ringing o instabilita';
- non aggiungere condensatori verso massa salvo footprint DNP.

`OUT30` e `OUT31`:

```text
U1 pin 45 OUT30 -> TP_OUT30, NC verso J1
U1 pin 46 OUT31 -> TP_OUT31, NC verso J1
```

## Alimentazioni

### Ingresso +8V

```text
J1 pin 40 VDD_IN
  -> F1/POLYFUSE opzionale o 0R
  -> FB1 ferrite/0R
  -> +8V_FILT
  -> C1 10uF verso GND_IN
  -> C2 100nF verso GND_IN
```

### Generazione +10V analogico

```text
+8V_FILT
  -> U2 boost con soft-start/enable
  -> +11V_PRE
  -> C3/C4 filtro locale
  -> U3 LDO/low-noise regulator
  -> +10V_A target 9.8V..10.0V
  -> C5 10uF verso AGND_LOCAL
  -> C6 100nF vicino a U1 pin 30
```

Note:

- target pratico `+9.8V..+10.0V`, non oltre, per rispettare margine `VDD-VSS`;
- `+11V_PRE` va scelto solo quanto basta per dropout di U3;
- se il tecnico sceglie boost diretto a `+10V_A`, deve dimostrare ripple e startup accettabili al banco.

### Generazione +5V logico

```text
+8V_FILT
  -> U4 LDO +5V
  -> +5V_L
  -> C7 4.7uF/10uF verso DGND_LOCAL
  -> C8 100nF vicino a U1 pin 7
```

### Ingresso -5V

```text
J1 pin 20 VSS_IN
  -> FB2 ferrite/0R
  -> -5V_A
  -> C9 10uF verso AGND_LOCAL
  -> C10 100nF vicino a U1 pin 9
```

### Masse

```text
J1 pin 21 GND_IN
  -> punto stella locale
  -> AGND_LOCAL
  -> DGND_LOCAL
```

Non creare loop di massa con piani separati collegati in piu punti.

## Protezione startup

Rev A deve prevedere almeno footprint per:

- soft-start/enable di U2;
- test pad `+8V_FILT`, `+11V_PRE`, `+10V_A`, `+5V_L`, `-5V_A`;
- clamp/TVS DNP sui rail se il tecnico li ritiene necessari dopo simulazione e test;
- resistenza/0R per isolare il boost durante debugging.

Regola: se `-5V_A` manca, `+10V_A` non deve superare il limite `VDD-VSS` del `MAX5167`.

## Test pad minimi

| Test pad | Net |
| --- | --- |
| `TP_GND` | `GND_IN` |
| `TP_8VIN` | `+8V_FILT` |
| `TP_11PRE` | `+11V_PRE` |
| `TP_10A` | `+10V_A` |
| `TP_5L` | `+5V_L` |
| `TP_N5A` | `-5V_A` |
| `TP_VIN` | `VIN_IN` |
| `TP_INH` | `INH_IN` |
| `TP_A0..TP_A4` | address |
| `TP_OUT0` | `CV0` |
| `TP_OUT15` | `CV15` |
| `TP_OUT29` | `CV29` |
| `TP_OUT30` | `OUT30` solo test |
| `TP_OUT31` | `OUT31` solo test |

## DNP obbligatori in Rev A

Questi footprint devono esserci, ma normalmente non vanno popolati nella prima accensione:

- U5 stretching `S/H`;
- capacitori verso massa sulle uscite CV;
- clamp/TVS rail locali;
- resistenze alternative di uscita diverse da `0R`;
- filtro RC su `VIN`.
