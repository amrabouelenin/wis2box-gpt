---
title: Hinzufügen von GTS-Headern zu WIS2-Benachrichtigungen
---

# Hinzufügen von GTS-Headern zu WIS2-Benachrichtigungen

!!! abstract "Lernergebnisse"

    Am Ende dieser praktischen Einheit werden Sie in der Lage sein:
    
    - eine Zuordnung zwischen Dateiname und GTS-Headern zu konfigurieren
    - Daten mit einem Dateinamen, der den GTS-Headern entspricht, einzuspeisen
    - die GTS-Header in den WIS2-Benachrichtigungen anzusehen

## Einführung

WMO-Mitglieder, die während der Übergangsphase zu WIS2 ihre Datentransmission über GTS einstellen möchten, müssen GTS-Header zu ihren WIS2-Benachrichtigungen hinzufügen. Diese Header ermöglichen es dem WIS2-zu-GTS-Gateway, die Daten an das GTS-Netzwerk weiterzuleiten.

Dies ermöglicht es den Mitgliedern, die auf einen WIS2-Knoten für die Datenpublikation umgestiegen sind, ihr MSS-System zu deaktivieren und sicherzustellen, dass ihre Daten weiterhin für Mitglieder verfügbar sind, die noch nicht zu WIS2 migriert sind.

Die GTS-Eigenschaft in der WIS2-Benachrichtigungsnachricht muss als zusätzliche Eigenschaft zur WIS2-Benachrichtigungsnachricht hinzugefügt werden. Die GTS-Eigenschaft ist ein JSON-Objekt, das die für die Weiterleitung an das GTS-Netzwerk erforderlichen GTS-Header enthält.

```json
{
  "gts": {
    "ttaaii": "FTAE31",
    "cccc": "VTBB"
  }
}
```

Innerhalb von wis2box können Sie dies automatisch zu WIS2-Benachrichtigungen hinzufügen, indem Sie eine zusätzliche Datei namens `gts_headers_mapping.csv` bereitstellen, die die erforderlichen Informationen enthält, um die GTS-Header den eingehenden Dateinamen zuzuordnen.

Diese Datei sollte im Verzeichnis abgelegt werden, das durch `WIS2BOX_HOST_DATADIR` in Ihrer `wis2box.env` definiert ist und sollte folgende Spalten haben:

- `string_in_filepath`: ein String, der Teil des Dateinamens ist, der verwendet wird, um die GTS-Header zuzuordnen
- `TTAAii`: der TTAAii-Header, der zur WIS2-Benachrichtigung hinzugefügt werden soll
- `CCCC`: der CCCC-Header, der zur WIS2-Benachrichtigung hinzugefügt werden soll

## Vorbereitung

Stellen Sie sicher, dass Sie SSH-Zugang zu Ihrer Studenten-VM haben und dass Ihre wis2box-Instanz läuft.

Stellen Sie sicher, dass Sie mit dem MQTT-Broker Ihrer wis2box-Instanz mit MQTT Explorer verbunden sind. Sie können die öffentlichen Anmeldeinformationen `everyone/everyone` verwenden, um sich mit dem Broker zu verbinden.

Stellen Sie sicher, dass Sie einen Webbrowser geöffnet haben mit dem Grafana-Dashboard Ihrer Instanz, indem Sie zu `http://<your-host>:3000` gehen.

## Erstellung von `gts_headers_mapping.csv`

Um GTS-Header zu Ihren WIS2-Benachrichtigungen hinzuzufügen, wird eine CSV-Datei benötigt, die GTS-Header den eingehenden Dateinamen zuordnet.

Die CSV-Datei sollte genau `gts_headers_mapping.csv` benannt sein und im Verzeichnis abgelegt werden, das durch `WIS2BOX_HOST_DATADIR` in Ihrer `wis2box.env` definiert ist.

## Übung 1: Bereitstellung einer `gts_headers_mapping.csv`-Datei
    
Kopieren Sie die Datei `exercise-materials/gts-headers-exercises/gts_headers_mapping.csv` zu Ihrer wis2box-Instanz und legen Sie sie im Verzeichnis ab, das durch `WIS2BOX_HOST_DATADIR` in Ihrer `wis2box.env` definiert ist.

```bash
cp ~/exercise-materials/gts-headers-exercises/gts_headers_mapping.csv ~/wis2box-data
```

Starten Sie dann den wis2box-management-Container neu, um die Änderungen anzuwenden:

```bash
docker restart wis2box-management
```

## Übung 2: Einspeisen von Daten mit GTS-Headern

Kopieren Sie die Datei `exercise-materials/gts-headers-exercises/A_SMRO01YRBK171200_C_EDZW_20240717120502.txt` in das Verzeichnis, das durch `WIS2BOX_HOST_DATADIR` in Ihrer `wis2box.env` definiert ist:

```bash
cp ~/exercise-materials/gts-headers-exercises/A_SMRO01YRBK171200_C_EDZW_20240717120502.txt ~/wis2box-data
```

Loggen Sie sich dann in den **wis2box-management**-Container ein:

```bash
cd ~/wis2box-1.0.0rc1
python3 wis2box-ctl.py login
```

Von der wis2box-Kommandozeile aus können wir die Beispieldatei `A_SMRO01YRBK171200_C_EDZW_20240717120502.txt` in ein spezifisches Dataset wie folgt einspeisen:

```bash
wis2box data ingest -p /data/wis2box/A_SMRO01YRBK171200_C_EDZW_20240717120502.txt --metadata-id urn:wmo:md:not-my-centre:core.surface-based-observations.synop
```

Stellen Sie sicher, dass Sie die Option `metadata-id` durch den korrekten Bezeichner für Ihr Dataset ersetzen.

Überprüfen Sie das Grafana-Dashboard, um zu sehen, ob die Daten korrekt eingespeist wurden. Wenn Sie WARNUNGEN oder FEHLER sehen, versuchen Sie, diese zu beheben und wiederholen Sie den Befehl `wis2box data ingest`.

## Übung 3: Ansehen der GTS-Header in der WIS2-Benachrichtigung

Gehen Sie zum MQTT Explorer und überprüfen Sie die WIS2-Benachrichtigungsnachricht für die Daten, die Sie gerade eingespeist haben.

Die WIS2-Benachrichtigungsnachricht sollte die GTS-Header enthalten, die Sie in der Datei `gts_headers_mapping.csv` angegeben haben.

## Schlussfolgerung

!!! success "Herzlichen Glückwunsch!"
    In dieser praktischen Sitzung haben Sie gelernt, wie Sie:
      - GTS-Header zu Ihren WIS2-Benachrichtigungen hinzufügen
      - überprüfen, ob GTS-Header über Ihre wis2box-Installation verfügbar gemacht werden