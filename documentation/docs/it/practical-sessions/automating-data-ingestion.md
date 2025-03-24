---
title: Automazione dell'ingestione dei dati
---

# Automazione dell'ingestione dei dati

!!! abstract "Risultati di apprendimento"

    Alla fine di questa sessione pratica, sarai in grado di:
    
    - comprendere come i plugin di dati del tuo dataset determinano il flusso di lavoro di ingestione dei dati
    - inserire dati in wis2box utilizzando uno script con il client Python di MinIO
    - inserire dati in wis2box accedendo a MinIO tramite SFTP

## Introduzione

Il container **wis2box-management** ascolta gli eventi dal servizio di archiviazione MinIO per attivare l'ingestione dei dati in base ai plugin di dati configurati per il tuo dataset. Questo ti permette di caricare dati nel bucket MinIO e attivare il flusso di lavoro di wis2box per pubblicare dati sul broker WIS2.

I plugin di dati definiscono i moduli Python che sono caricati dal container **wis2box-management** e determinano come i dati vengono trasformati e pubblicati.

Nell'esercizio precedente avresti dovuto creare un dataset utilizzando il template `surface-based-observations/synop` che includeva i seguenti plugin di dati:

<img alt="mappature dei dati" src="../../assets/img/wis2box-data-mappings.png" width="800">

Quando un file viene caricato su MinIO, wis2box assocerà il file a un dataset quando il percorso del file contiene l'id del dataset (`metadata_id`) e determinerà i plugin di dati da utilizzare in base all'estensione del file e al modello di file definito nelle mappature del dataset.

Nelle sessioni precedenti, abbiamo attivato il flusso di lavoro di ingestione dei dati utilizzando la funzionalità della riga di comando di wis2box, che carica i dati nello storage MinIO nel percorso corretto.

Gli stessi passaggi possono essere eseguiti programmaticamente utilizzando qualsiasi software client MinIO o S3, permettendoti di automatizzare l'ingestione dei tuoi dati come parte dei tuoi flussi di lavoro operativi.

In alternativa, puoi anche accedere a MinIO utilizzando il protocollo SFTP per caricare dati e attivare il flusso di lavoro di ingestione dei dati.

## Preparazione

Accedi alla tua VM studente utilizzando il tuo client SSH (PuTTY o altro).

Assicurati che wis2box sia attivo e funzionante:

```bash
cd ~/wis2box-1.0.0rc1/
python3 wis2box-ctl.py start
python3 wis2box-ctl.py status
```

Assicurati che MQTT Explorer sia in esecuzione e connesso alla tua istanza. Se sei ancora connesso dalla sessione precedente, cancella eventuali messaggi precedenti che potresti aver ricevuto dalla coda.
Questo può essere fatto sia disconnettendosi e riconnettendosi sia cliccando sull'icona del cestino per l'argomento dato.

Assicurati di avere un browser web aperto con la dashboard di Grafana per la tua istanza andando su `http://<il-tuo-host>:3000`

E assicurati di avere una seconda scheda aperta con l'interfaccia utente di MinIO su `http://<il-tuo-host>:9001`. Ricorda che devi accedere con `WIS2BOX_STORAGE_USER` e `WIS2BOX_STORAGE_PASSWORD` definiti nel tuo file `wis2box.env`.

## Esercizio 1: configurare uno script Python per inserire dati in MinIO

In questo esercizio utilizzeremo il client Python di MinIO per copiare dati in MinIO.

MinIO fornisce un client Python che può essere installato come segue:

```bash
pip3 install minio
```

Sulla tua VM studente il pacchetto 'minio' per Python sarà già installato.

Vai alla directory `exercise-materials/data-ingest-exercises`; questa directory contiene uno script di esempio `copy_file_to_incoming.py` che utilizza il client Python di MinIO per copiare un file in MinIO.

Prova a eseguire lo script per copiare il file di dati di esempio `csv-aws-example.csv` nel bucket `wis2box-incoming` in MinIO" come segue:

```bash
cd ~/exercise-materials/data-ingest-exercises
python3 copy_file_to_incoming.py csv-aws-example.csv
```

!!! note

    Riceverai un errore poiché lo script non è configurato per accedere all'endpoint MinIO sul tuo wis2box.

Lo script deve conoscere l'endpoint corretto per accedere a MinIO sul tuo wis2box. Se wis2box è in esecuzione sul tuo host, l'endpoint MinIO è disponibile su `http://<il-tuo-host>:9000`. Lo script deve anche essere aggiornato con la tua password di archiviazione e il percorso nel bucket MinIO per memorizzare i dati.

!!! question "Aggiorna lo script e inserisci i dati CSV"
    
    Modifica lo script `copy_file_to_incoming.py` per correggere gli errori, utilizzando uno dei seguenti metodi:
    - Dalla riga di comando: usa l'editor di testo `nano` o `vim` per modificare lo script
    - Utilizzando WinSCP: avvia una nuova connessione utilizzando il protocollo di file `SCP` e le stesse credenziali del tuo client SSH. Naviga alla directory `exercise-materials/data-ingest-exercises` e modifica `copy_file_to_incoming.py` utilizzando l'editor di testo integrato
    
    Assicurati di:

    - definire il corretto endpoint MinIO per il tuo host
    - fornire la corretta password di archiviazione per la tua istanza MinIO
    - fornire il percorso corretto nel bucket MinIO per memorizzare i dati

    Riesegui lo script per inserire il file di dati di esempio `csv-aws-example.csv` in MinIO:

    ```bash
    python3 copy_file_to_incoming.py csv-aws-example.csv
    ```

    E assicurati che gli errori siano risolti.

Puoi verificare che i dati siano stati caricati correttamente controllando l'interfaccia utente di MinIO e vedendo se i dati di esempio sono disponibili nella directory corretta nel bucket `wis2box-incoming`.

Puoi utilizzare la dashboard di Grafana per controllare lo stato del flusso di lavoro di ingestione dei dati.

Infine, puoi utilizzare MQTT Explorer per verificare se sono state pubblicate notifiche per i dati che hai inserito. Dovresti vedere che i dati CSV sono stati trasformati in formato BUFR e che è stata pubblicata una notifica di dati WIS2 con un URL "canonico" per consentire il download dei dati BUFR.

## Esercizio 2: Inserimento di dati binari

Successivamente, proviamo ad inserire dati binari in formato BUFR utilizzando il client Python di MinIO.

wis2box può inserire dati binari in formato BUFR utilizzando il plugin `wis2box.data.bufr4.ObservationDataBUFR` incluso in wis2box.

Questo plugin dividerà il file BUFR in singoli messaggi BUFR e pubblicherà ogni messaggio sul broker MQTT. Se la stazione per il messaggio BUFR corrispondente non è definita nei metadati della stazione di wis2box, il messaggio non verrà pubblicato.

Poiché hai utilizzato il template `surface-based-observations/synop` nella sessione precedente, le tue mappature dei dati includono il plugin `Dati FM-12 convertiti in BUFR` per le mappature del dataset. Questo plugin carica il modulo `wis2box.data.synop2bufr.ObservationDataSYNOP2BUFR` per inserire i dati.

!!! question "Inserimento di dati binari in formato BUFR"

    Esegui il seguente comando per copiare il file di dati binari `bufr-example.bin` nel bucket `wis2box-incoming` in MinIO:

    ```bash
    python3 copy_file_to_incoming.py bufr-example.bin
    ```

Controlla la dashboard di Grafana e MQTT Explorer per vedere se i dati di prova sono stati inseriti e pubblicati con successo e se vedi degli errori, prova a risolverli.

!!! question "Verifica l'ingestione dei dati"

    Quanti messaggi sono stati pubblicati sul broker MQTT per questo campione di dati?

??? success "Clicca per rivelare la risposta"

    Se hai inserito e pubblicato con successo l'ultimo campione di dati, dovresti aver ricevuto 10 nuove notifiche sul broker MQTT di wis2box. Ogni notifica corrisponde ai dati di una stazione per un timestamp di osservazione.

    Il plugin `wis2box.data.bufr4.ObservationDataBUFR` divide il file BUFR in singoli messaggi BUFR e pubblica un messaggio per ogni stazione e timestamp di osservazione.

## Esercizio 3: Inserimento di dati SYNOP in formato ASCII

Nella sessione precedente abbiamo utilizzato il modulo SYNOP nell'**applicazione web wis2box** per inserire dati SYNOP in formato ASCII. Puoi anche inserire dati SYNOP in formato ASCII caricando i dati in MinIO.

Nella sessione precedente avresti dovuto creare un dataset che includeva il plugin 'Dati FM-12 convertiti in BUFR' per le mappature del dataset:

<img alt="mappature del dataset" src="../../assets/img/wis2box-data-mappings.png" width="800">

Questo plugin carica il modulo `wis2box.data.synop2bufr.ObservationDataSYNOP2BUFR` per inserire i dati.

Prova a utilizzare il client Python di MinIO per inserire i dati di prova `synop-202307.txt` e `synop-202308.txt` nella tua istanza wis2box.

Nota che i 2 file contengono lo stesso contenuto, ma il nome del file è diverso. Il nome del file viene utilizzato per determinare la data del campione di dati.

Il plugin synop2bufr si basa su un modello di file per estrarre la data dal nome del file. Il primo gruppo nell'espressione regolare viene utilizzato per estrarre l'anno e il secondo gruppo viene utilizzato per estrarre il mese.

!!! question "Inserisci dati FM-12 SYNOP in formato ASCII"

    Torna all'interfaccia MinIO nel tuo browser e naviga nel bucket `wis2box-incoming` e nel percorso dove hai caricato i dati di prova nell'esercizio precedente.
    
    Carica i nuovi file nel percorso corretto nel bucket `wis2box-incoming` in MinIO per attivare il flusso di lavoro di ingestione dei dati.

    Controlla la dashboard di Grafana e MQTT Explorer per vedere se i dati di prova sono stati inseriti e pubblicati con successo.

    Qual è la differenza nel `properties.datetime` tra i due messaggi pubblicati sul broker MQTT?

??? success "Clicca per rivelare la risposta"

    Controlla le proprietà delle ultime 2 notifiche in MQTT Explorer e noterai che una notifica ha:

    ```{.copy}
    "properties": {
        "data_id": "wis2/urn:wmo:md:nl-knmi-test:surface-based-observations.synop/WIGOS_0-20000-0-60355_20230703T090000",
        "datetime": "2023-07-03T09:00:00Z",
        ...
    ```

    e l'altra notifica ha:

    ```{.copy}
    "properties": {
        "data_id": "wis2/urn:wmo:md:nl-knmi-test:surface-based-observations.synop/WIGOS_0-20000-0-60355_20230803T090000",
        "datetime": "2023-08-03T09:00:00Z",
        ...
    ```

    Il nome del file è stato utilizzato per determinare l'anno e il mese del campione di dati.

## Esercizio 4: Inserimento di dati in MinIO utilizzando SFTP

I dati possono anche essere inseriti in MinIO tramite SFTP.

Il servizio MinIO abilitato nello stack wis2box ha SFTP abilitato sulla porta 8022. Puoi accedere a MinIO tramite SFTP utilizzando le stesse credenziali dell'interfaccia utente di MinIO. In questo esercizio utilizzeremo le credenziali di amministrazione per il servizio MinIO come definito in `wis2box.env`, ma puoi anche creare utenti aggiuntivi nell'interfaccia utente di MinIO.

Per accedere a MinIO tramite SFTP puoi utilizzare qualsiasi software client SFTP. In questo esercizio utilizzeremo WinSCP, che è un client SFTP gratuito per Windows.

Utilizzando WinSCP, la tua connessione apparirà come segue:

<img alt="connessione sftp-winscp" src="../../assets/img/winscp-sftp-connection.png" width="400">

Per nome utente e password, utilizza i valori delle variabili di ambiente `WIS2BOX_STORAGE_USERNAME` e `WIS2BOX_STORAGE_PASSWORD` dal tuo file `wis2box.env`. Clicca su 'salva' per salvare la sessione e poi su 'login' per connetterti.

Quando effettui il login vedrai il bucket MinIO `wis2box-incoming` e `wis2box-public` nella directory radice. Puoi caricare dati nel bucket `wis2box-incoming` per attivare il flusso di lavoro di ingestione dei dati.

Clicca sul bucket `wis2box-incoming` per navigare in questo bucket, poi clicca con il tasto destro e seleziona *Nuovo*->*Directory* per creare una nuova directory nel bucket `wis2box-incoming`.

Crea la directory *not-a-valid-path* e carica il file *randomfile.txt* in questa directory (puoi usare qualsiasi file tu voglia).

Controlla la dashboard di Grafana alla porta 3000 per vedere se il flusso di lavoro di ingestione dei dati è stato attivato. Dovresti vedere:

*ERRORE - Errore di validazione del percorso: Impossibile abbinare http://minio:9000/wis2box-incoming/not-a-valid-path/randomfile.txt al dataset, il percorso dovrebbe includere uno dei seguenti: ...*

L'errore indica che il file è stato caricato su MinIO e il flusso di lavoro di ingestione dei dati è stato attivato, ma poiché il percorso non corrisponde a nessun dataset nell'istanza wis2box, il mapping dei dati è fallito.

Puoi anche utilizzare `sftp` dalla riga di comando:

```bash
sftp -P 8022 -oBatchMode=no -o StrictHostKeyChecking=no <il-mio-nome-host-o-ip>
```
Accedi utilizzando le credenziali definite in `wis2box.env` per le variabili di ambiente `WIS2BOX_STORAGE_USERNAME` e `WIS2BOX_STORAGE_PASSWORD`, naviga nel bucket `wis2box-incoming` e poi crea una directory e carica un file come segue:

```bash
cd wis2box-incoming
mkdir not-a-valid-path
cd not-a-valid-path
put ~/exercise-materials/data-ingest-exercises/synop.txt .
```

Questo risulterà in un "Errore di validazione del percorso" nella dashboard di Grafana indicando che il file è stato caricato su MinIO.

Per uscire dal client sftp, digita `exit`. 

!!! Question "Inserisci dati in MinIO utilizzando SFTP"

    Prova a inserire il file `synop.txt` nella tua istanza wis2box utilizzando SFTP per attivare il flusso di lavoro di ingestione dei dati.

    Controlla l'interfaccia utente di MinIO per vedere se il file è stato caricato nel percorso corretto nel bucket `wis2box-incoming`.
    
    Controlla la dashboard di Grafana per vedere se il flusso di lavoro di ingestione dei dati è stato attivato o se ci sono stati degli errori.

 Per assicurarti che i tuoi dati vengano inseriti correttamente, assicurati che il file sia caricato nel bucket `wis2box-incoming` in una directory che corrisponda all'id del dataset o all'argomento del tuo dataset.

## Conclusione

!!! success "Congratulazioni!"
    In questa sessione pratica, hai imparato a:

    - attivare il flusso di lavoro di wis2box utilizzando uno script Python e il client Python di MinIO
    - utilizzare diversi plugin di dati per inserire diversi formati di dati
    - caricare dati su MinIO utilizzando SFTP