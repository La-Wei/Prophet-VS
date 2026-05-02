# Handoff CAD Rev A

## Pacchetto da consegnare al progettista PCB

Consegnare questi file insieme:

- [README.md](README.md)
- [00_status_prototipo.md](00_status_prototipo.md)
- [01_schema_testuale_rev_a.md](01_schema_testuale_rev_a.md)
- [02_netlist_pinmap_rev_a.csv](02_netlist_pinmap_rev_a.csv)
- [03_bom_funzione_rev_a.md](03_bom_funzione_rev_a.md)
- [04_vincoli_pcb_rev_a.md](04_vincoli_pcb_rev_a.md)
- [05_piano_collaudo_rev_a.md](05_piano_collaudo_rev_a.md)
- [06_dati_da_misurare_sul_prophet.md](06_dati_da_misurare_sul_prophet.md)
- [cad_kicad/README.md](cad_kicad/README.md)

## Output CAD richiesto

Per considerare completato il passaggio in CAD servono:

- progetto KiCad iniziale: `cad_kicad/max5167_rev_a_prototype.kicad_pro`;
- schema elettrico PDF;
- file sorgente KiCad/Altium/Eagle;
- ERC senza errori critici;
- footprint `CEM5530` 40 pin verificato;
- footprint `MAX5167` 48-TQFP verificato;
- layout PCB;
- DRC senza errori critici;
- Gerber solo dopo revisione;
- pick/place o assembly drawing se si produce esternamente;
- BOM con part number reali.

## Revisione prima dei Gerber

Controllo indipendente obbligatorio:

1. J1 pin 1-40 contro pinout CEM5530.
2. U1 pin 1-48 contro datasheet MAX5167.
3. Rail: `VDD_IN` non diretto a U1 `VDD`.
4. Rail: `+10V_A` non supera limiti con `-5V_A`.
5. `SELECT`/`CONFIG` coerenti.
6. `INH` arriva a `S/H` in direct mode.
7. `OUT30/OUT31` non arrivano al socket.
8. `VIN` non filtrato in modo da alterare il sample.
9. U5 DNP non modifica il comportamento se non popolato.
10. Label prototipo presente.

## Serigrafia obbligatoria

Mettere sul PCB:

```text
MAX5167 CEM5530 REPLACEMENT
REV A PROTOTYPE - NOT VALIDATED
PIN 1
```

## Nota per il tecnico

Se il progettista CAD chiede "posso produrre direttamente?", la risposta e' no: prima serve revisione dello schema e verifica meccanica sul Prophet reale.
