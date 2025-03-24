---
title: Einrichten eines empfohlenen Datensatzes mit Zugriffskontrolle
---

# Einrichten eines empfohlenen Datensatzes mit Zugriffskontrolle

!!! abstract "Lernergebnisse"
    Am Ende dieser praktischen Sitzung werden Sie in der Lage sein:

    - einen neuen Datensatz mit der Datenrichtlinie 'empfohlen' zu erstellen
    - einen Zugriffstoken zum Datensatz hinzuzufügen
    - zu überprüfen, dass der Datensatz ohne den Zugriffstoken nicht zugänglich ist
    - den Zugriffstoken zu den HTTP-Headern hinzuzufügen, um auf den Datensatz zuzugreifen

## Einführung

Datensätze, die nicht als 'Kern'-Datensatz in der WMO betrachtet werden, können optional mit einer Zugriffskontrollrichtlinie konfiguriert werden. wis2box bietet einen Mechanismus, um einen Zugriffstoken zu einem Datensatz hinzuzufügen, der verhindert, dass Benutzer Daten herunterladen, es sei denn, sie geben den Zugriffstoken in den HTTP-Headern an.

## Vorbereitung

Stellen Sie sicher, dass Sie SSH-Zugriff auf Ihre Studenten-VM haben und dass Ihre wis2box-Instanz aktiv ist.

Stellen Sie sicher, dass Sie mit dem MQTT-Broker Ihrer wis2box-Instanz über MQTT Explorer verbunden sind. Sie können die öffentlichen Anmeldeinformationen `everyone/everyone` verwenden, um sich mit dem Broker zu verbinden.

Stellen Sie sicher, dass Sie einen Webbrowser geöffnet haben mit der wis2box-Webapp für Ihre Instanz, indem Sie `http://<Ihr-Host>/wis2box-webapp` besuchen.

## Übung 1: Erstellen eines neuen Datensatzes mit der Datenrichtlinie 'empfohlen'

Gehen Sie auf die Seite 'Datensatzeditor' in der wis2box-Webapp und erstellen Sie einen neuen Datensatz. Verwenden Sie dieselbe Zentrum-ID wie in den vorherigen praktischen Sitzungen und verwenden Sie die Vorlage='surface-weather-observations/synop'.

Klicken Sie auf 'OK', um fortzufahren.

Im Datensatzeditor setzen Sie die Datenrichtlinie auf 'empfohlen' (beachten Sie, dass das Ändern der Datenrichtlinie die 'Themenhierarchie' aktualisiert).
Ersetzen Sie die automatisch generierte 'Lokale ID' durch einen beschreibenden Namen für den Datensatz, z.B. 'empfohlene-daten-mit-zugriffskontrolle':

<img alt="create-dataset-recommended" src="../../assets/img/create-dataset-recommended.png" width="800">

Fahren Sie fort, die erforderlichen Felder für räumliche Eigenschaften und Kontaktinformationen auszufüllen, und 'Überprüfen Sie das Formular' auf Fehler.

Senden Sie schließlich den Datensatz ab, unter Verwendung des zuvor erstellten Authentifizierungstokens, und überprüfen Sie, dass der neue Datensatz in der wis2box-Webapp erstellt wurde.

Überprüfen Sie den MQTT-Explorer, um zu sehen, dass Sie die WIS2-Benachrichtigungsnachricht über den neuen Discovery-Metadatensatz im Thema `origin/a/wis2/<Ihr-Zentrum-ID>/metadata` erhalten.

## Übung 2: Einen Zugriffstoken zum Datensatz hinzufügen

Melden Sie sich am wis2box-Management-Container an,

```bash
cd ~/wis2box-1.0.0rc1
python3 wis2box-ctl.py login
```

Vom Befehlszeileninneren des Containers können Sie einen Datensatz sichern, indem Sie den Befehl `wis2box auth add-token` verwenden, mit der Option `--metadata-id`, um den Metadaten-Identifikator des Datensatzes und den Zugriffstoken als Argument anzugeben.

Zum Beispiel, um den Zugriffstoken `S3cr3tT0k3n` zum Datensatz mit dem Metadaten-Identifikator `urn:wmo:md:not-my-centre:core.surface-based-observations.synop` hinzuzufügen:

```bash
wis2box auth add-token --metadata-id urn:wmo:md:not-my-centre:reco.surface-based-observations.synop S3cr3tT0k3n
```

Verlassen Sie den wis2box-Management-Container:

```bash
exit
```

## Übung 3: Veröffentlichen Sie einige Daten zum Datensatz

Kopieren Sie die Datei `exercise-materials/access-control-exercises/aws-example2.csv` in das Verzeichnis, das durch `WIS2BOX_HOST_DATADIR` in Ihrer `wis2box.env` definiert ist:

```bash
cp ~/exercise-materials/access-control-exercises/aws-example2.csv ~/wis2box-data
```

Verwenden Sie dann WinSCP oder einen Befehlszeilen-Editor, um die Datei `aws-example2.csv` zu bearbeiten und die WIGOS-Station-Identifikatoren in den Eingabedaten zu aktualisieren, um den Stationen in Ihrer wis2box-Instanz zu entsprechen.

Gehen Sie anschließend zum Stations-Editor in der wis2box-Webapp. Für jede Station, die Sie in `aws-example2.csv` verwendet haben, aktualisieren Sie das 'Thema'-Feld, um es mit dem 'Thema' des Datensatzes abzugleichen, den Sie in der vorherigen Übung erstellt haben.

Diese Station wird nun mit 2 Themen verbunden sein, einem für den 'Kern'-Datensatz und einem für den 'empfohlenen' Datensatz:

<img alt="edit-stations-add-topics" src="../../assets/img/edit-stations-add-topics.png" width="600">

Sie müssen Ihren Token für `collections/stations` verwenden, um die aktualisierten Stationsdaten zu speichern.

Melden Sie sich anschließend erneut am wis2box-Management-Container an:

```bash
cd ~/wis2box-1.0.0rc1
python3 wis2box-ctl.py login
```

Von der wis2box-Befehlszeile aus können wir die Beispieldatendatei `aws-example2.csv` in einen bestimmten Datensatz wie folgt einpflegen:

```bash
wis2box data ingest -p /data/wis2box/aws-example2.csv --metadata-id urn:wmo:md:not-my-centre:reco.surface-based-observations.synop
```

Stellen Sie sicher, dass Sie den richtigen Metadaten-Identifikator für Ihren Datensatz angeben und **überprüfen Sie, dass Sie WIS2-Datenbenachrichtigungen im MQTT Explorer erhalten**, im Thema `origin/a/wis2/<Ihr-Zentrum-ID>/data/recommended/surface-based-observations/synop`.

Überprüfen Sie den kanonischen Link in der WIS2-Benachrichtigungsnachricht und kopieren/einfügen Sie den Link in den Browser, um zu versuchen, die Daten herunterzuladen.

Sie sollten einen 403 Forbidden-Fehler sehen.

## Übung 4: Den Zugriffstoken zu HTTP-Headern hinzufügen, um auf den Datensatz zuzugreifen

Um zu demonstrieren, dass der Zugriffstoken erforderlich ist, um auf den Datensatz zuzugreifen, werden wir den Fehler, den Sie im Browser gesehen haben, mit der Befehlszeilenfunktion `wget` reproduzieren.

Von der Befehlszeile in Ihrer Studenten-VM verwenden Sie den Befehl `wget` mit dem kanonischen Link, den Sie aus der WIS2-Benachrichtigungsnachricht kopiert haben.

```bash
wget <kanonischer-link>
```

Sie sollten sehen, dass die HTTP-Anfrage mit *401 Unauthorized* zurückkommt und die Daten nicht heruntergeladen werden.

Fügen Sie nun den Zugriffstoken zu den HTTP-Headern hinzu, um auf den Datensatz zuzugreifen.

```bash
wget --header="Authorization: Bearer S3cr3tT0k3n" <kanonischer-link>
```

Nun sollten die Daten erfolgreich heruntergeladen werden.

## Schlussfolgerung

!!! success "Herzlichen Glückwunsch!"
    In dieser praktischen Sitzung haben Sie gelernt, wie man:

    - einen neuen Datensatz mit der Datenrichtlinie 'empfohlen' erstellt
    - einen Zugriffstoken zum Datensatz hinzufügt
    - überprüft, dass der Datensatz ohne den Zugriffstoken nicht zugänglich ist
    - den Zugriffstoken zu den HTTP-Headern hinzufügt, um auf den Datensatz zuzugreifen