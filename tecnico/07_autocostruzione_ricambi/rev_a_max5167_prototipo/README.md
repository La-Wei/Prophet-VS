# Rev A MAX5167 - prototipo non validato

## Stato

Questa cartella contiene una proposta di progetto `Rev A` per un modulo sostitutivo `CEM5530` basato su `MAX5167`.

E' un **prototipo non validato**:

- non e' uno schema originale `ELD5530`;
- non e' una BOM ufficiale Synthelectro: la fonte 2014 conferma solo IC Maxim Integrated, non la sigla `MAX5167`;
- non e' un progetto collaudato nel Prophet VS;
- non contiene Gerber pronti per produzione;
- non va montato nel synth senza test fuori macchina;
- va trasformato in CAD, revisionato e provato da un tecnico.

Obiettivo della `Rev A`: dare al tecnico una base concreta con schema testuale, pin map, BOM funzionale, vincoli PCB e test plan.

Nota batteria: questo prototipo sostituisce solo il `CEM5530`. Non e' la mod memoria non volatile e non elimina la batteria del Prophet VS; vedere `../../01_problemi_e_fix/batteria_memoria_nvram.md`.

## Applicazione pratica

La `Rev A` non e' una modifica interna a un chip. E' una schedina sostitutiva:

```text
CEM5530 originale fuori dallo socket
modulo Rev A inserito nello stesso socket
MAX5167 e alimentazioni locali montati sul modulo Rev A
```

Il CAD serve per realizzare fisicamente quella schedina: il `MAX5167` e' un 48-TQFP, mentre il `CEM5530` originale e' un modulo/IC a 40 pin con piedinatura diversa. La PCB fa da traduttore tra il Prophet e il `MAX5167`.

Se un modulo finito `ELD5530`/Straylight e' reperibile e collaudato, questa cartella non serve per montarlo. Serve solo se il tecnico deve costruire un sostituto.

## Aprire in ordine

1. [00_status_prototipo.md](00_status_prototipo.md)
2. [01_schema_testuale_rev_a.md](01_schema_testuale_rev_a.md)
3. [02_netlist_pinmap_rev_a.csv](02_netlist_pinmap_rev_a.csv)
4. [03_bom_funzione_rev_a.md](03_bom_funzione_rev_a.md)
5. [04_vincoli_pcb_rev_a.md](04_vincoli_pcb_rev_a.md)
6. [05_piano_collaudo_rev_a.md](05_piano_collaudo_rev_a.md)
7. [06_dati_da_misurare_sul_prophet.md](06_dati_da_misurare_sul_prophet.md)
8. [07_handoff_cad.md](07_handoff_cad.md)
9. [cad_kicad/README.md](cad_kicad/README.md)

## Cosa puo' fare il tecnico con questa cartella

- Disegnare lo schema in KiCad/Altium/Eagle senza dover ricavare da zero il mapping.
- Aprire un progetto KiCad iniziale in `cad_kicad/`.
- Creare il footprint adattatore `CEM5530` 40 pin -> `MAX5167` 48-TQFP.
- Selezionare componenti reali per boost, LDO, filtri e protezioni.
- Preparare un primo prototipo.
- Testare il modulo fuori dal Prophet VS.

## Cosa manca prima di dichiararlo funzionante

- Misure reali su `U449/U425`: rail, `VIN`, `INH`, address, carichi.
- Scelta part number finali per alimentazioni e protezioni.
- Layout PCB e revisione indipendente.
- Prototipo fisico.
- Collaudo strumentale.
- Installazione controllata in un solo socket alla volta.

## Rimandi

- Progetto preliminare: [../max5167_v2_like_pre_design.md](../max5167_v2_like_pre_design.md)
- Dossier generale: [../cem5530_clone_build_dossier.md](../cem5530_clone_build_dossier.md)
- Pinout CEM5530: [../../05_pagine_rilevanti/note/5530/page_002.md](../../05_pagine_rilevanti/note/5530/page_002.md)
- Schema Prophet S&H/CV: [../../05_pagine_rilevanti/note/pvs_service/page_006.md](../../05_pagine_rilevanti/note/pvs_service/page_006.md)
