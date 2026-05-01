# Jack posteriori: sostituzione

## Quanti sono

Sul Prophet VS i jack 1/4" posteriori da considerare sono 4:

- 2 jack audio output: left/right o left/phones/right-mono secondo cablaggio e pannello reale
- 2 jack footswitch: `Second Release Footswitch` e `Auxiliary Footswitch`

La pagina `pvs_service` 4 mostra chiaramente i due footswitch (`J301` e `J302`). Le pagine `pvs_service` 11/12 mostrano la sezione output/chorus con i connettori dell'area audio (`J901/J902/P901` nello schema/board).

## Sono tutti uguali?

Meccanicamente potrebbero essere della stessa famiglia di jack PCB, ma elettricamente non vanno trattati come identici:

- gli output audio portano segnale audio e possono usare contatti normalizzati/switch;
- i footswitch leggono contatti di comando e possono usare tip/sleeve o contatti switch in modo diverso;
- un jack stereo/switch puo' essere usato su circuiti mono se la PCB e' progettata cosi', ma non bisogna dedurlo dal solo fatto che il segnale e' mono.

Quindi: confrontare sempre pin, footprint, altezza, ghiera, contatti switch e continuita' del jack originale prima di dissaldare.

## Il pezzo Synth-Parts linkato

Il pezzo linkato e' un buon candidato, non una garanzia assoluta senza confronto fisico:

- Jalco `YKB21-5078`
- 1/4" / 6.3 mm PCB
- stereo con switch
- filetto `M12x1`
- equivalenti dichiarati: `YKB21-5078`, `HLJ-2305`, `HTJ-064-16D`
- venduto nella categoria Prophet VS da Synth-Parts

Link: `https://www.synth-parts.com/en/products/connectors-and-cable/14-phone-jack/5460/ykb21-5078-phone-jack-1/4-6.3-mm-for-printed-circuits-stereo`

## Stato attuale

Aggiornamento: la plastica dei jack posteriori e' rotta. In questo caso non ha piu senso considerarli solo "da testare": vanno sostituiti tutti e 4, sempre verificando footprint, altezza, contatti e orientamento prima di ordinare o saldare.

## Prima di sostituirli

1. Ispezione: jack crepato, ghiera lenta, saldature rotte, piste sollevate, ossido.
2. Foto lato componenti e lato saldature prima di dissaldare.
3. Test continuita' di un jack originale con plug inserito e non inserito: tip, ring, sleeve e contatti switch.
4. Confronto con il ricambio: pin, passo, altezza, filetto, dado, contatti switch.
5. Sostituzione dei 4 jack rotti, evitando di stressare piste e fori metallizzati.

Se il problema principale e' bleed a volume zero, i jack sono una possibile causa solo se il segnale cambia toccando/muovendo cavi o se le normalizzazioni risultano ossidate. Se il difetto resta identico su tutte le uscite, prima controllare VCA/S&H/output/rail.

## Alternative

Alternative sensate:

- stesso Jalco `YKB21-5078`;
- equivalenti indicati dal venditore: `HLJ-2305`, `HTJ-064-16D`;
- altra fonte dello stesso identico footprint e stesso schema contatti.

Alternative da evitare salvo necessita':

- jack mono tipo `YKB21-5012` o `YKB21-5076` senza verificare pinout e switch;
- jack panel-mount Switchcraft/Neutrik con fili volanti, se la PCB originale e' sana;
- jack "simile" ma con altezza o foratura diversa, perche puo' stressare pannello e piste.

## Acquisto pratico

Se il tecnico conferma che il footprint originale corrisponde al Jalco `YKB21-5078`, comprare 4 pezzi piu eventuali dadi `M12x1` di ricambio.

Nota collegata: per MIDI, power switch e selettore tensione vedere `pannello_posteriore_ricambi.md`.
