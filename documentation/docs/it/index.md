---
title: Home
---

<img alt="Logo WMO" src="assets/img/wmo-logo.png" width="200">
# Formazione WIS2 in a box

WIS2 in a box ([wis2box](https://docs.wis2box.wis.wmo.int)) è un'implementazione di riferimento libera e open source (FOSS) di un nodo WMO WIS2. Il progetto fornisce un set di strumenti plug and play per l'ingestione, l'elaborazione e la pubblicazione di dati meteorologici/climatici/idrici utilizzando approcci basati su standard in linea con i principi WIS2. wis2box offre anche accesso a tutti i dati nella rete WIS2. wis2box è progettato per avere una bassa barriera all'ingresso per i fornitori di dati, fornendo infrastrutture e servizi abilitanti per la scoperta, l'accesso e la visualizzazione dei dati.

Questa formazione fornisce spiegazioni passo passo su vari aspetti del progetto wis2box, nonché una serie di esercizi per aiutarti a pubblicare e scaricare dati da WIS2. La formazione è fornita sotto forma di presentazioni panoramiche e di esercitazioni pratiche.

I partecipanti potranno lavorare con dati di test e metadati di esempio, oltre a integrare i propri dati e metadati.

Questa formazione copre un'ampia gamma di argomenti (installazione/configurazione/pubblicazione, scaricamento dati, ecc.).

## Obiettivi e risultati di apprendimento

Gli obiettivi di questa formazione sono di familiarizzare con i seguenti:

- Concetti e componenti fondamentali dell'architettura WIS2
- Formati di dati e metadati utilizzati in WIS2 per la scoperta e l'accesso
- Architettura e ambiente wis2box
- Funzioni principali di wis2box:
    - gestione dei metadati
    - ingestione dati e trasformazione in formato BUFR
    - broker MQTT per la pubblicazione di messaggi WIS2
    - endpoint HTTP per il download dei dati
    - endpoint API per l'accesso programmatico ai dati

## Navigazione

La navigazione a sinistra fornisce un indice per l'intera formazione.

La navigazione a destra fornisce un indice per una pagina specifica.

## Prerequisiti

### Conoscenze

- Comandi Linux di base (vedi il [cheatsheet](cheatsheets/linux.md))
- Conoscenze di base di networking e protocolli Internet

### Software

Questa formazione richiede i seguenti strumenti:

- Un'istanza con sistema operativo Ubuntu (fornita dai formatori WMO durante le sessioni di formazione locali) vedi [Accesso al tuo VM studente](practical-sessions/accessing-your-student-vm.md#introduction)
- Client SSH per accedere alla tua istanza
- MQTT Explorer sul tuo computer locale
- Client SCP e FTP per copiare file dal tuo computer locale

## Convenzioni

!!! domanda

    Una sezione contrassegnata in questo modo ti invita a rispondere a una domanda.

Noterai anche sezioni di suggerimenti e note all'interno del testo:

!!! suggerimento

    I suggerimenti condividono aiuti su come eseguire al meglio le attività.

!!! nota

    Le note forniscono informazioni aggiuntive sull'argomento trattato dalla sessione pratica, oltre a come eseguire al meglio le attività.

Gli esempi sono indicati come segue:

Configurazione
``` {.yaml linenums="1"}
my-collection-defined-in-yaml:
    type: collection
    title: il mio titolo definito come attributo yaml denominato title
    description: la mia descrizione come attributo yaml denominato description
```

I frammenti che devono essere digitati in un terminale/console sono indicati come:

```bash
echo 'Ciao mondo'
```

I nomi dei container (immagini in esecuzione) sono denotati in **grassetto**.

## Luogo e materiali della formazione

I contenuti della formazione, il wiki e il tracker di problemi sono gestiti su GitHub a [https://github.com/wmo-im/wis2box-training](https://github.com/wmo-im/wis2box-training).

## Stampa del materiale

Questa formazione può essere esportata in PDF. Per salvare o stampare questo materiale didattico, vai alla [pagina di stampa](print_page), e seleziona
File > Stampa > Salva come PDF.

## Materiali per gli esercizi

I materiali per gli esercizi possono essere scaricati dal file zip [exercise-materials.zip](/exercise-materials.zip).

## Supporto

Per problemi/bug/suggerimenti o miglioramenti/contributi a questa formazione, utilizza il [GitHub issue tracker](https://github.com/wmo-im/wis2box-training/issues).

Tutti i bug, i miglioramenti e i problemi di wis2box possono essere segnalati su [GitHub](https://github.com/wmo-im/wis2box/issues).

Per ulteriore supporto o domande, contatta wis2-support@wmo.int.

Come sempre, la documentazione principale di wis2box può sempre essere trovata su [https://docs.wis2box.wis.wmo.int](https://docs.wis2box.wis.wmo.int).

I contributi sono sempre incoraggiati e benvenuti!