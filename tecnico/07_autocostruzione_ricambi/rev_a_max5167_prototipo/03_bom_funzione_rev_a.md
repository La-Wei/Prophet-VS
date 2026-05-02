# BOM funzionale Rev A

## Stato

Questa non e' una BOM di acquisto definitiva. E' una BOM funzionale per trasformare lo schema testuale in CAD.

Il tecnico deve scegliere part number reali in base a:

- disponibilita' autentica;
- package e altezza;
- rumore;
- startup/enable;
- corrente e temperatura;
- compatibilita' con layout piccolo.

## IC principali

| Ref | Funzione | Specifica minima | Popolamento |
| --- | --- | --- | --- |
| `U1` | Sample & hold 32 canali | `MAX5167L/M/N`, 48-TQFP | obbligatorio |
| `U2` | Boost `+8V_FILT` -> `+11V_PRE` | regolabile, soft-start/enable, low-noise | obbligatorio salvo soluzione alternativa validata |
| `U3` | Regolazione/filtraggio `+11V_PRE` -> `+10V_A` | LDO low-noise o regolatore equivalente | consigliato |
| `U4` | LDO `+8V_FILT` -> `+5V_L` | low-noise, stabile con cap scelti | obbligatorio |
| `U5` | Stretching opzionale `S/H` | logica/monostabile compatibile 5V | DNP Rev A iniziale |

## Passivi e protezioni

| Ref | Valore iniziale | Funzione | Popolamento |
| --- | --- | --- | --- |
| `RIN1` | `0R`, opzione `100R` | serie su `VIN` | obbligatorio |
| `RN_LOGIC` | `0R` o `47R` | serie su `A0..A4`, `INH` | obbligatorio |
| `RSEL` | `10k` | pull-up `SELECT` a `+5V_L` | obbligatorio |
| `RCFG` | `10k` | pull-down `CONFIG` a `DGND_LOCAL` | obbligatorio |
| `R_OUT0..R_OUT29` | `0R`, opzioni `100R/470R` | serie uscite CV | obbligatorio |
| `R_OUT30/R_OUT31` | DNP | solo test pad, non socket | DNP |
| `FB1` | ferrite o `0R` | filtro `+8V_IN` | obbligatorio |
| `FB2` | ferrite o `0R` | filtro `-5V_IN` | obbligatorio |
| `F1` | `0R` o polyfuse piccolo | isolamento/debug su `+8V_IN` | consigliato |
| `D_RAIL*` | DNP | clamp/TVS rail locali | DNP finche non scelti |

## Decoupling minimo

| Ref | Valore iniziale | Posizione |
| --- | --- | --- |
| `C1` | `10uF` | `+8V_FILT` verso `GND_IN` |
| `C2` | `100nF` | `+8V_FILT` vicino ingresso |
| `C3` | `10uF` | `+11V_PRE` uscita boost |
| `C4` | `100nF` | `+11V_PRE` vicino U3 |
| `C5` | `10uF` | `+10V_A` verso `AGND_LOCAL` |
| `C6` | `100nF` | vicino U1 pin 30 |
| `C7` | `4.7uF/10uF` | `+5V_L` verso `DGND_LOCAL` |
| `C8` | `100nF` | vicino U1 pin 7 |
| `C9` | `10uF` | `-5V_A` verso `AGND_LOCAL` |
| `C10` | `100nF` | vicino U1 pin 9 |
| `C_AGND` | DNP | eventuale filtro locale massa/rail |
| `C_OUT*` | DNP | uscite CV verso massa, solo se test lo richiede |

## Connettori e meccanica

| Ref | Parte | Nota |
| --- | --- | --- |
| `J1` | header maschio 40 pin compatibile socket `CEM5530` | pin torniti consigliati |
| `TP_*` | test pad | rail, address, `VIN`, `INH`, CV campione |
| label PCB | serigrafia | `MAX5167 Rev A PROTOTYPE - NOT VALIDATED` |

## Note di scelta componenti

- `MAX5167L`: preferenza iniziale se autentico, per uscita a bassa impedenza.
- `MAX5167M/N`: valutabili se il tecnico vuole piu resistenza d'uscita interna o se il carico capacitivo lo richiede.
- U2 deve essere scelto guardando ripple e startup, non solo corrente massima.
- U3 deve evitare overshoot su `+10V_A`.
- U4 deve dare `+5V_L` pulito e stabile prima della logica.
- I componenti DNP non sono decorativi: servono a correggere Rev A senza rifare subito il PCB.
