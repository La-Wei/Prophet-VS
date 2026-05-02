# Vincoli PCB Rev A

## Stato

Questi vincoli servono per il layout del prototipo. Non sono quote meccaniche definitive: vanno completate misurando il Prophet VS reale.

## Stackup consigliato

PCB 4 layer consigliata:

1. Top: componenti, segnali corti, fanout U1.
2. Inner 1: ground plane continuo.
3. Inner 2: power/local rails.
4. Bottom: routing verso header 40 pin e test pad.

PCB 2 layer sconsigliata per Rev A perche' boost, rail analogici, CV e footprint adattatore sono troppo densi.

## Zone fisiche

Separare il modulo in tre aree:

- area `U1 MAX5167`: centro, decoupling ravvicinato;
- area alimentazioni: boost/induttore lontano da `VIN` e uscite CV;
- area header `J1`: pin 40 CEM, tracce ordinate verso socket.

## Regole layout critiche

- Tenere induttore boost e nodo switching lontani da `VIN_IN`, `CV0..CV29`, `AGND_LOCAL`.
- Traccia `VIN_IN` corta, schermata da ground, senza passare sotto il boost.
- Decoupling `100nF` attaccato ai pin U1, non "nelle vicinanze generiche".
- `AGND_LOCAL` e `DGND_LOCAL` collegati in un solo punto vicino a U1.
- Routing address e `INH` con ritorno ground vicino.
- Nessun collegamento di `OUT30/OUT31` al footprint CEM.
- Pin 1 marcato con serigrafia grande, visibile anche dopo montaggio.
- Serigrafia obbligatoria: `PROTOTYPE NOT VALIDATED`.

## Distanze e altezza

Prima del CAD finale il tecnico deve misurare:

- larghezza del socket `CEM5530`;
- passo e diametro pin accettati dal socket o dal nuovo tulip;
- altezza massima disponibile sopra `U449`;
- altezza massima disponibile sopra `U425`;
- distanza da componenti vicini, cavi, coperchio e dissipatori.

## Test pad

I test pad devono essere accessibili con il modulo installato su fixture fuori synth.

Minimo:

- `GND_IN`;
- `+8V_FILT`;
- `+11V_PRE`;
- `+10V_A`;
- `+5V_L`;
- `-5V_A`;
- `VIN_IN`;
- `INH_IN`;
- `A0..A4`;
- `CV0`, `CV15`, `CV29`;
- `OUT30`, `OUT31`.

## Footprint DNP da tenere

- U5 logica/stretching;
- TVS/clamp rail;
- condensatori uscite CV;
- filtro RC `VIN`;
- resistenze serie alternative sulle uscite;
- jumper `DIRECT/STRETCH` per `S/H`.

## Checklist layout

| Check | Stato |
| --- | --- |
| `OUT30/OUT31` non vanno a J1 | da fare |
| `VDD_IN` non va diretto a U1 pin 30 | da fare |
| `VSS_IN` passa da filtro prima di U1 pin 9 | da fare |
| `SELECT` pull-up e `CONFIG` pull-down presenti | da fare |
| `S/H` default direct da `INH` | da fare |
| rail `+10V_A` misurabile da test pad | da fare |
| rail `+5V_L` misurabile da test pad | da fare |
| `VIN_IN` non passa vicino al boost | da fare |
| pin 1 chiarissimo su top e bottom | da fare |
| label prototipo presente | da fare |
