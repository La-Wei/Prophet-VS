Crea una mappa rapida di navigazione per la riparazione:

doc/prophet_vs_service_context/diagnostic_notes/quick_navigation_map.md

Usa anche il briefing gia' creato:

doc/prophet_vs_service_context/diagnostic_notes/technician_briefing_volume_zero_bleed.md

Mantieni separati due problemi che possono essere collegati ma non vanno forzati in una sola diagnosi:

- audio/modulazione/bleed che passa con volume a zero
- case/regolatore troppo caldo nella zona dei tre TO-220 fissati al dissipatore

I tre TO-220 della foto `IMG_5543.jpg` sono da trattare come regolatori lineari, non transistor generici:

- `U301` = `7805`, rail `+5VD`
- `U302` = `7812`, rail `+12V`
- `U303` = `7912`, rail `-12V`

La designator map `pvs_service` pagina 5 indica ordine fisico sinistra->destra `U301`, `U302`, `U303`; confermare comunque sulla serigrafia reale se visibile.

Deve rispondere in modo pratico a queste domande:

1. Se il problema è audio che passa con volume a zero, partire da queste pagine.
2. Se il problema è contaminazione CV/modulazione, partire da queste pagine.
3. Se il problema è pressure/aftertouch, partire da queste pagine.
4. Se il problema è instabilità alimentazione/rail, partire da queste pagine.
5. Se il problema è case caldo/regolatore che scalda troppo, partire da queste pagine.
6. Se il problema è riparazione precedente fatta male/pista sollevata/modifica ECR sbagliata, partire da queste pagine.
7. Se il problema è chorus/output, partire da queste pagine.

Per ogni punto includi:
- PDF sorgente
- numero pagina
- percorso immagine pagina generata
- percorso nota pagina generata
- perché questa pagina è importante
- cosa ispezionare per primo
- eventuale nota "non concludere automaticamente" quando il problema potrebbe avere cause multiple

Tieni il file corto, pratico e orientato a un tecnico.

Poi prepara una cartella consegnabile e pulita per il tecnico fuori da `doc/`:

tecnico/

Aggiorna anche un `README.md` nella root principale del progetto, con link ai file principali e una sintesi delle cause/fix.

Deve contenere solo materiale utile alla diagnosi:

- `01_problemi_e_fix/cause_e_fix.md` con cause possibili, verifiche e fix consigliati
- README operativo della cartella
- briefing tecnico `technician_briefing_volume_zero_bleed.md`
- mappa rapida `quick_navigation_map.md`
- checklist/ispezione/misure sicure
- mappe circuito concise
- indici componenti utili
- note pagina e immagini pagina solo delle pagine davvero rilevanti
- PDF sorgenti principali
  - includere anche `5508.pdf` come riferimento S&H, anche se non e' il primo PDF da aprire
- foto utente `IMG_5543.jpg`

Usa cartelle visualmente utili e non ripetere "Prophet VS" nel nome delle cartelle. Esempio:

- `01_problemi_e_fix/`
- `02_checklist_misure/`
- `03_mappe_circuito/`
- `04_componenti_net_rail/`
- `05_pagine_rilevanti/`
- `06_pdf_originali/`
- `foto/`

Non includere:

- cartella `prompt/`
- script di estrazione
- OCR grezzo `extracted_text/`
- manifest JSON
- cache o file di sistema
- pagine/immagini non citate dalla mappa o dal briefing
