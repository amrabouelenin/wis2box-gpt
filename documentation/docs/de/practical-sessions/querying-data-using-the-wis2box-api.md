---
title: Datenabfrage mit der wis2box API
---

# Datenabfrage mit der wis2box API

!!! abstract "Lernergebnisse"
    Am Ende dieser praktischen Sitzung werden Sie in der Lage sein:

    - die wis2box API zu nutzen, um Ihre Stationen abzufragen und zu filtern
    - die wis2box API zu nutzen, um Ihre Daten abzufragen und zu filtern

## Einführung

Die wis2box API bietet Zugriff auf Entdeckung und Abfrage in maschinenlesbarer Form für die Daten, die in wis2box aufgenommen wurden. Die API basiert auf dem OGC API - Features Standard und wird mit [pygeoapi](https://pygeoapi.io) implementiert.

Die wis2box API bietet Zugriff auf die folgenden Sammlungen:

- Stationen
- Entdeckungsmetadaten
- Datenbenachrichtigungen
- sowie eine Sammlung pro konfiguriertem Datensatz, die die Ausgabe von bufr2geojson speichert (das Plugin `bufr2geojson` muss in der Datenmappings-Konfiguration aktiviert sein, um die Elemente in der Datensatzsammlung zu füllen).

In dieser praktischen Sitzung lernen Sie, wie Sie die Daten-API verwenden, um Daten, die in wis2box aufgenommen wurden, zu durchsuchen und abzufragen.

## Vorbereitung

!!! note
    Navigieren Sie zur Startseite der wis2box API in Ihrem Webbrowser:

    `http://<Ihr-Host>/oapi`

<img alt="wis2box-api-startseite" src="../../assets/img/wis2box-api-landing-page.png" width="600">

## Sammlungen inspizieren

Von der Startseite aus klicken Sie auf den Link 'Sammlungen'.

!!! question
    Wie viele Datensatzsammlungen sehen Sie auf der resultierenden Seite? Was denken Sie, was jede Sammlung darstellt?

??? success "Klicken Sie, um die Antwort zu enthüllen"
    Es sollten 4 Sammlungen angezeigt werden, einschließlich "Stationen", "Entdeckungsmetadaten" und "Datenbenachrichtigungen"

## Stationen inspizieren

Von der Startseite aus klicken Sie auf den Link 'Sammlungen', dann auf den Link 'Stationen'.

<img alt="wis2box-api-sammlungen-stationen" src="../../assets/img/wis2box-api-collections-stations.png" width="600">

Klicken Sie auf den Link 'Durchsuchen', dann auf den Link 'json'.

!!! question
    Wie viele Stationen werden zurückgegeben? Vergleichen Sie diese Zahl mit der Stationsliste in `http://<Ihr-Host>/wis2box-webapp/station`

??? success "Klicken Sie, um die Antwort zu enthüllen"
    Die Anzahl der Stationen aus der API sollte gleich der Anzahl der Stationen sein, die Sie in der wis2box-Webanwendung sehen.

!!! question
    Wie können wir nach einer einzelnen Station (z.B. `Balaka`) suchen?

??? success "Klicken Sie, um die Antwort zu enthüllen"
    Abfragen Sie die API mit `http://<Ihr-Host>/oapi/collections/stations/items?q=Balaka`.

!!! note
    Das obige Beispiel basiert auf den Malawi-Testdaten. Versuchen Sie, gegen die Stationen zu testen, die Sie im Rahmen der vorherigen Übungen eingegeben haben.

## Beobachtungen inspizieren

!!! note
    Das obige Beispiel basiert auf den Malawi-Testdaten. Versuchen Sie, gegen die Beobachtungen zu testen, die Sie im Rahmen der Übungen eingegeben haben.

Von der Startseite aus klicken Sie auf den Link 'Sammlungen', dann auf den Link 'Oberflächenwetterbeobachtungen aus Malawi'.

<img alt="wis2box-api-sammlungen-malawi-beob" src="../../assets/img/wis2box-api-collections-malawi-obs.png" width="600">

Klicken Sie auf den Link 'Abfragbare'.

<img alt="wis2box-api-sammlungen-malawi-beob-abfragbare" src="../../assets/img/wis2box-api-collections-malawi-obs-queryables.png" width="600">

!!! question
    Welches Abfragbare würde verwendet, um nach Stationskennung zu filtern?

??? success "Klicken Sie, um die Antwort zu enthüllen"
    Der `wigos_station_identifer` ist das richtige Abfragbare.

Navigieren Sie zur vorherigen Seite (d.h. `http://<Ihr-Host>/oapi/collections/urn:wmo:md:mwi:mwi_met_centre:surface-weather-observations`)

Klicken Sie auf den Link 'Durchsuchen'.

!!! question
    Wie können wir die JSON-Antwort visualisieren?

??? success "Klicken Sie, um die Antwort zu enthüllen"
    Indem Sie auf den Link 'JSON' oben rechts auf der Seite klicken oder `f=json` zur API-Anfrage im Webbrowser hinzufügen.

Untersuchen Sie die JSON-Antwort der Beobachtungen.

!!! question
    Wie viele Datensätze werden zurückgegeben?

!!! question
    Wie können wir die Antwort auf 3 Beobachtungen begrenzen?

??? success "Klicken Sie, um die Antwort zu enthüllen"
    Fügen Sie `limit=3` zur API-Anfrage hinzu.

!!! question
    Wie können wir die Antwort nach den neuesten Beobachtungen sortieren?

??? success "Klicken Sie, um die Antwort zu enthüllen"
    Fügen Sie `sortby=-resultTime` zur API-Anfrage hinzu (beachten Sie das `-`-Zeichen, um die absteigende Sortierreihenfolge anzugeben). Um nach den frühesten Beobachtungen zu sortieren, aktualisieren Sie die Anfrage, um `sortby=resultTime` einzuschließen.

!!! question
    Wie können wir die Beobachtungen nach einer einzelnen Station filtern?

??? success "Klicken Sie, um die Antwort zu enthüllen"
    Fügen Sie `wigos_station_identifier=<WSI>` zur API-Anfrage hinzu.

!!! question
    Wie können wir die Beobachtungen als CSV erhalten?

??? success "Klicken Sie, um die Antwort zu enthüllen"
    Fügen Sie `f=csv` zur API-Anfrage hinzu.

!!! question
    Wie können wir eine einzelne Beobachtung (id) anzeigen?

??? success "Klicken Sie, um die Antwort zu enthüllen"
    Verwenden Sie den Merkmalsidentifikator aus einer API-Anfrage gegen die Beobachtungen, um die API für `http://<Ihr-Host>/oapi/collections/{collectionId}/items/{featureId}` zu abfragen, wobei `{collectionId}` der Name Ihrer Beobachtungssammlung und `{itemId}` der Identifikator der einzelnen Beobachtung von Interesse ist.

## Schlussfolgerung

!!! success "Herzlichen Glückwunsch!"
    In dieser praktischen Sitzung haben Sie gelernt, wie Sie:

    - die wis2box API nutzen, um Ihre Stationen abzufragen und zu filtern
    - die wis2box API nutzen, um Ihre Daten abzufragen und zu filtern