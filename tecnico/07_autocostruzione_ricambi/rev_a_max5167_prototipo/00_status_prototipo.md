# Status Rev A

## Decisione di progetto

La `Rev A` usa un singolo `MAX5167` come sostituto funzionale del `CEM5530`.

Motivo:

- `CEM5530`: 30 canali sample & hold, ingresso comune, address 5 bit, controllo `INH`.
- `MAX5167`: 32 canali sample & hold, ingresso comune, address 5 bit, controllo `S/H`, rail analogici/logici separati.
- Le due uscite extra `OUT30/OUT31` del `MAX5167` restano non collegate al socket.

## Avvertenza grande

Questo progetto e' marcato **PROTOTIPO NON VALIDATO**. Non deve essere presentato come ricambio pronto o equivalente garantito all'`ELD5530 V2`.

La parte piu rischiosa non e' il mapping statico dei pin; sono:

- alimentazione `MAX5167` con `VDD` circa `+10V` e `VSS` circa `-5V`, vicino al limite `VDD-VSS`;
- startup/shutdown, dove un rail puo' salire prima dell'altro;
- ripple del boost `+10V`;
- larghezza reale del sample `INH low`;
- carichi reali sulle CV del Prophet VS;
- spazio meccanico e orientamento pin 1.

## Criterio di successo Rev A

La `Rev A` e' riuscita solo se, fuori dal synth:

- si accende con corrente stabile;
- genera rail locali corretti senza overshoot pericoloso;
- ogni address 0-29 aggiorna solo l'uscita prevista;
- `OUT30/OUT31` non arrivano al socket;
- droop, hold step e rumore restano compatibili con CV Prophet;
- dopo 60 minuti la temperatura e' stabile;
- il modulo supera una revisione pin-to-pin indipendente.

Solo dopo si installa nel Prophet, un modulo alla volta.

## Versione documento

- Nome: `rev_a_max5167_prototipo`
- Data: 2026-05-02
- Stato: progettazione testuale completa per prototipo, non CAD, non Gerber
