# Dati da misurare sul Prophet prima della Rev A finale

## Scopo

Questi dati servono per passare da prototipo Rev A a progetto realmente validabile.

Misurare sia su `U449` sia su `U425`, perche' i due socket possono avere carichi e routing diversi.

## Rail

| Punto | U449 | U425 | Note |
| --- | --- | --- | --- |
| pin 40 `VDD` | da misurare | da misurare | atteso circa `+8V` |
| pin 20 `VSS` | da misurare | da misurare | atteso circa `-5V` |
| pin 21 `GND` | riferimento | riferimento | verificare massa |
| ripple `VDD` | da misurare | da misurare | oscilloscopio |
| ripple `VSS` | da misurare | da misurare | oscilloscopio |

## Timing digitale

| Segnale | U449 | U425 | Note |
| --- | --- | --- | --- |
| `INH` high time | da misurare | da misurare | |
| `INH` low time | da misurare | da misurare | dato critico |
| address setup prima di `INH low` | da misurare | da misurare | |
| address hold dopo `INH high` | da misurare | da misurare | |
| tempo tra canali | da misurare | da misurare | |

## Ingresso analogico

| Punto | U449 | U425 | Note |
| --- | --- | --- | --- |
| range `VIN` minimo/massimo | da misurare | da misurare | durante patch diverse |
| rumore/ripple su `VIN` | da misurare | da misurare | |
| stabilizzazione `VIN` prima del sample | da misurare | da misurare | |

## Uscite CV

Misurare almeno alcune uscite rappresentative:

| Uscita | Socket | Tensione/range | Carico stimato | Note |
| --- | --- | --- | --- | --- |
| `CV0` | U449 | da misurare | da stimare | |
| `CV15` | U449 | da misurare | da stimare | |
| `CV29` | U449 | da misurare | da stimare | |
| `CV0` | U425 | da misurare | da stimare | |
| `CV15` | U425 | da misurare | da stimare | |
| `CV29` | U425 | da misurare | da stimare | |

## Meccanica

| Misura | Valore |
| --- | --- |
| altezza libera sopra U449 | da misurare |
| altezza libera sopra U425 | da misurare |
| larghezza socket | da misurare |
| distanza componenti vicini | da misurare |
| orientamento pin 1 reale | da confermare |

## Decisioni che dipendono da queste misure

- valore finale di `+10V_A`;
- necessita' di stretching `S/H`;
- scelta `MAX5167L/M/N`;
- resistenze serie uscite;
- necessita' di buffer extra;
- altezza componenti;
- possibilita' di usare boost + LDO o boost diretto.
