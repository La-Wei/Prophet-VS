# Batteria memoria, SRAM e mod senza batteria

## Risposta breve

`ELD5530` e batteria sono due cose separate.

- `ELD5530` sostituisce i `CEM5530` dello sample & hold/CV.
- La batteria mantiene alimentate le SRAM patch quando il Prophet VS e' spento.
- Montare `ELD5530` non elimina la necessita' della batteria.
- La batteria non serve piu solo se si sostituiscono le SRAM originali con moduli non volatili compatibili.

## Cosa dice la mod Synthelectro

Nel post Synthelectro del 4 luglio 2015, la modifica "no more battery" riguarda la memoria programmi:

- rimuove le due SRAM originali alimentate a batteria;
- rimuove la batteria interna;
- installa due socket/supporti per le nuove SRAM non volatili;
- usa memorie da `32 Kbytes` al posto delle SRAM originali da `8 Kbytes`;
- permette quattro banchi, circa `400` programmi;
- nello stesso Prophet erano presenti anche due `ELD5530`, ma questa e' un'altra modifica.

Quindi il post descrive due upgrade sullo stesso strumento:

1. mod memoria non volatile: elimina la batteria;
2. mod `ELD5530`: sostituisce i `CEM5530`.

Fonte: `https://synthelectro-fr.blogspot.com/2015/07/how-to-upgrade-programm-memory-of.html`

## Cosa fare sul Prophet VS

Se la macchina ha ancora le SRAM originali:

- la batteria serve ancora;
- prima di sostituirla, salvare/dumpare le patch via SysEx se possibile;
- controllare polarita', tensione e segni di perdita/corrosione;
- sostituire la batteria solo con componente corretto e montato da tecnico.

Se si fa la mod SRAM non volatile:

- la batteria puo' essere rimossa;
- le patch vanno ricaricate dopo l'intervento;
- va verificata la protezione contro scritture spurie all'accensione/spegnimento;
- non basta mettere una qualunque SRAM piu grande: serve un adattamento elettrico/logico corretto.

## Batteria Synth-Parts

Link utile se si mantiene la memoria originale a batteria:

- Synth-Parts `Battery 2/3 Solder pins`, Varta `BAVA2-3AHB3`, `3 V`, `1200 mAh`, diametro `17 mm`: `https://www.synth-parts.com/en/products/battery/5181/battery-2/3-solder-pins`

Decisione ordine, aggiornata al 2026-05-02:

- si: ordinarne `1` se il Prophet VS ha ancora le SRAM originali alimentate a batteria;
- no/non ancora: non serve se il tecnico fa subito una vera mod SRAM non volatile/NVRAM;
- i moduli `Straylight X5530` trovati non cambiano questa decisione, perche sostituiscono i `CEM5530` e non la memoria patch;
- la pagina Synth-Parts indica `Actual stock: 4 pcs.`, prezzo `14.28 EUR`, spedizione EU circa `4-14` giorni e attenzione a polarita'/saldatura.

Nota: la pagina Synth-Parts avvisa di controllare la polarita' e che la batteria e' saldata alla scheda. Quindi non va montata "al volo": serve dissaldatura pulita, controllo danni da perdita e orientamento corretto.

## Nota per diagnosi

La batteria scarica o in perdita puo' causare perdita/corruzione patch e danni fisici alla PCB, ma non spiega direttamente il case caldo dei regolatori o il calore dei `CEM5530`.

Tenere separati questi tre piani:

- memoria patch/batteria/SRAM;
- `CEM5530` o `ELD5530` nello sample & hold/CV;
- alimentazione/regolatori `U301/U302/U303`.
