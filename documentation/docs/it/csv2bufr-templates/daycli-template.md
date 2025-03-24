---
title: Modello DAYCLI
---

# Modello csv2bufr per dati climatici giornalieri (DAYCLI)

Il modello **DAYCLI** fornisce un formato CSV standardizzato per convertire i dati climatici giornalieri nella sequenza BUFR 307075.

Il formato è destinato all'uso con i Sistemi di Gestione dei Dati Climatici per pubblicare dati su WIS2, a supporto dei requisiti di segnalazione per le osservazioni climatiche giornaliere.

Questo modello mappa le osservazioni giornaliere di:

 - Temperatura minima, massima e media su un periodo di 24 ore
 - Precipitazione totale accumulata su un periodo di 24 ore
 - Profondità totale della neve al momento dell'osservazione
 - Profondità della neve fresca su un periodo di 24 ore

Questo modello richiede metadati aggiuntivi rispetto al modello semplificato AWS: metodo di calcolo della temperatura media; altezze del sensore e della stazione; esposizione e classificazione della qualità della misurazione.

!!! Nota "Informazioni sul modello DAYCLI"
    Si prega di notare che la sequenza BUFR DAYCLI sarà aggiornata nel 2025 per includere informazioni aggiuntive e bandiere di controllo della qualità (QC) riviste. Il modello DAYCLI incluso nel wis2box sarà aggiornato per riflettere questi cambiamenti. L'OMM comunicherà quando il software wis2box sarà aggiornato per includere il nuovo modello DAYCLI, permettendo agli utenti di aggiornare i loro sistemi di conseguenza.

## Colonne CSV e descrizione

{{ read_csv("docs/assets/tables/daycli-table.csv") }}

## Metodo di mediazione

{{ read_csv("docs/assets/tables/averaging-method-table.csv") }}

## Bandiera di qualità

{{ read_csv("docs/assets/tables/quality_flag.csv") }}

## Riferimenti per la classificazione del sito

[Riferimento per "classificazione del sito della temperatura"](https://library.wmo.int/idviewer/35625/839).

[Riferimento per "classificazione del sito delle precipitazioni"](https://library.wmo.int/idviewer/35625/840).

## Esempio

File CSV di esempio che si conforma al modello DAYCLI: [daycli-example.csv](/sample-data/daycli-example.csv).