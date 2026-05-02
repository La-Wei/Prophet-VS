# KiCad CAD - Rev A MAX5167 prototype

## Stato

Questa cartella contiene un progetto KiCad iniziale per il modulo `MAX5167 Rev A`.

E' **CAD di partenza**, non CAD finale:

- schema e PCB sono marcati come prototipo non validato;
- il PCB e' un placeholder meccanico/elettrico da completare in KiCad;
- non generare Gerber senza revisione del tecnico;
- usare la netlist CSV e lo schema testuale come sorgenti vincolanti.

## File

- `max5167_rev_a_prototype.kicad_pro`: progetto KiCad.
- `max5167_rev_a_prototype.kicad_sch`: foglio schematico di overview con vincoli Rev A.
- `max5167_rev_a_prototype.kicad_pcb`: board placeholder 4 layer con aree funzionali e serigrafia prototipo.
- [exports/max5167_rev_a_schematic.pdf](exports/max5167_rev_a_schematic.pdf): PDF esportato dallo schematico con `kicad-cli`.

Nota: lo schematico e' stato esportato con `kicad-cli 10.0.1` dal DMG KiCad montato localmente. Il PCB e' volutamente un placeholder di layout e va completato in KiCad prima di generare Gerber.

## Come usarlo

1. Aprire `max5167_rev_a_prototype.kicad_pro` in KiCad.
2. Creare/verificare i simboli reali:
   - `J1` socket/header `CEM5530` 40 pin;
   - `U1` `MAX5167` 48-TQFP;
   - `U2/U3/U4` alimentazioni;
   - `U5` DNP opzionale per stretching.
3. Importare il mapping da `../02_netlist_pinmap_rev_a.csv`.
4. Completare lo schema elettrico.
5. Completare il layout PCB.
6. Eseguire ERC/DRC.
7. Fare revisione indipendente prima di qualsiasi Gerber.

## Avvertenza

Il CAD non rende il progetto automaticamente sicuro. Il punto critico resta il collaudo fuori macchina: rail, startup, ripple, timing `INH`, address e carichi CV.
