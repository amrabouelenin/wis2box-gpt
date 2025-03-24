---
title: Aggiunta degli header GTS alle notifiche WIS2
---

# Aggiunta degli header GTS alle notifiche WIS2

!!! abstract "Risultati dell'apprendimento"

    Al termine di questa sessione pratica, sarai in grado di:
    
    - configurare una mappatura tra nome del file e header GTS
    - inserire dati con un nome di file che corrisponde agli header GTS
    - visualizzare gli header GTS nelle notifiche WIS2

## Introduzione

I membri dell'OMM che desiderano interrompere la trasmissione dei loro dati su GTS durante la fase di transizione a WIS2 dovranno aggiungere gli header GTS alle loro notifiche WIS2. Questi header permettono al gateway WIS2 a GTS di inoltrare i dati alla rete GTS.

Questo consente ai membri che sono passati all'uso di un nodo WIS2 per la pubblicazione dei dati di disabilitare il loro sistema MSS e garantire che i loro dati siano ancora disponibili per i membri che non sono ancora migrati a WIS2.

La proprietà GTS nel Messaggio di Notifica WIS2 deve essere aggiunta come proprietà aggiuntiva al Messaggio di Notifica WIS2. La proprietà GTS è un oggetto JSON che contiene gli header GTS necessari affinché i dati vengano inoltrati alla rete GTS.

```json
{
  "gts": {
    "ttaaii": "FTAE31",
    "cccc": "VTBB"
  }
}
```

All'interno di wis2box puoi aggiungere automaticamente questo alle Notifiche WIS2 fornendo un file aggiuntivo chiamato `gts_headers_mapping.csv` che contiene le informazioni necessarie per mappare gli header GTS ai nomi dei file in arrivo.

Questo file dovrebbe essere collocato nella directory definita da `WIS2BOX_HOST_DATADIR` nel tuo `wis2box.env` e dovrebbe avere le seguenti colonne:

- `string_in_filepath`: una stringa che fa parte del nome del file che verrà utilizzata per abbinare gli header GTS
- `TTAAii`: l'header TTAAii da aggiungere alla notifica WIS2
- `CCCC`: l'header CCCC da aggiungere alla notifica WIS2

## Preparazione

Assicurati di avere accesso SSH alla tua VM studente e che la tua istanza di wis2box sia attiva e funzionante.

Assicurati di essere connesso al broker MQTT della tua istanza wis2box usando MQTT Explorer. Puoi usare le credenziali pubbliche `everyone/everyone` per connetterti al broker.

Assicurati di avere un browser web aperto con la dashboard di Grafana per la tua istanza andando su `http://<tuo-host>:3000`

## Creazione di `gts_headers_mapping.csv`

Per aggiungere gli header GTS alle tue notifiche WIS2, è necessario un file CSV che mappi gli header GTS ai nomi dei file in arrivo.

Il file CSV dovrebbe essere nominato (esattamente) `gts_headers_mapping.csv` e dovrebbe essere collocato nella directory definita da `WIS2BOX_HOST_DATADIR` nel tuo `wis2box.env`. 

## Esercizio 1: fornire un file `gts_headers_mapping.csv`
    
Copia il file `exercise-materials/gts-headers-exercises/gts_headers_mapping.csv` nella tua istanza di wis2box e collocalo nella directory definita da `WIS2BOX_HOST_DATADIR` nel tuo `wis2box.env`.

```bash
cp ~/exercise-materials/gts-headers-exercises/gts_headers_mapping.csv ~/wis2box-data
```

Quindi riavvia il container di gestione wis2box per applicare le modifiche:

```bash
docker restart wis2box-management
```

## Esercizio 2: Inserimento dati con header GTS

Copia il file `exercise-materials/gts-headers-exercises/A_SMRO01YRBK171200_C_EDZW_20240717120502.txt` nella directory definita da `WIS2BOX_HOST_DATADIR` nel tuo `wis2box.env`:

```bash
cp ~/exercise-materials/gts-headers-exercises/A_SMRO01YRBK171200_C_EDZW_20240717120502.txt ~/wis2box-data
```

Quindi accedi al container **wis2box-management**:

```bash
cd ~/wis2box-1.0.0rc1
python3 wis2box-ctl.py login
```

Dalla linea di comando di wis2box possiamo inserire il file di dati di esempio `A_SMRO01YRBK171200_C_EDZW_20240717120502.txt` in un dataset specifico come segue:

```bash
wis2box data ingest -p /data/wis2box/A_SMRO01YRBK171200_C_EDZW_20240717120502.txt --metadata-id urn:wmo:md:not-my-centre:core.surface-based-observations.synop
```

Assicurati di sostituire l'opzione `metadata-id` con l'identificatore corretto per il tuo dataset.

Controlla la dashboard di Grafana per vedere se i dati sono stati inseriti correttamente. Se vedi degli AVVISI o ERRORI, prova a risolverli e ripeti l'esercizio del comando `wis2box data ingest`.

## Esercizio 3: Visualizzazione degli header GTS nella Notifica WIS2

Vai su MQTT Explorer e controlla il Messaggio di Notifica WIS2 per i dati che hai appena inserito.

Il Messaggio di Notifica WIS2 dovrebbe contenere gli header GTS che hai fornito nel file `gts_headers_mapping.csv`.

## Conclusione

!!! success "Congratulazioni!"
    In questa sessione pratica, hai imparato a:
      - aggiungere gli header GTS alle tue notifiche WIS2
      - verificare che gli header GTS siano resi disponibili tramite la tua installazione di wis2box