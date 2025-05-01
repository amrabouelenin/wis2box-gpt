---
title: Startseite
---

<img alt="WMO-Logo" src="assets/img/wmo-logo.png" width="200">
# WIS2 in a box Schulung

WIS2 in a box ([wis2box](https://docs.wis2box.wis.wmo.int)) ist eine freie und offene Referenzimplementierung eines WMO WIS2-Knotens. Das Projekt bietet ein Plug-and-Play-Toolset zum Erfassen, Verarbeiten und Veröffentlichen von Wetter-/Klima-/Wasserdaten unter Verwendung von standardbasierten Ansätzen in Übereinstimmung mit den WIS2-Prinzipien. wis2box ermöglicht außerdem den Zugriff auf alle Daten im WIS2-Netzwerk. wis2box ist so konzipiert, dass es für Datenanbieter leicht zugänglich ist und Infrastruktur sowie Dienste für die Datenentdeckung, den Zugriff und die Visualisierung bereitstellt.

Diese Schulung bietet schrittweise Erklärungen zu verschiedenen Aspekten des wis2box-Projekts sowie eine Reihe von Übungen, um Ihnen zu helfen, Daten von WIS2 zu veröffentlichen und herunterzuladen. Die Schulung wird in Form von Übersichtspräsentationen sowie praktischen Übungen angeboten.

Teilnehmer werden in der Lage sein, mit Beispieltestdaten und Metadaten zu arbeiten sowie ihre eigenen Daten und Metadaten zu integrieren.

Diese Schulung deckt eine breite Palette von Themen ab (Installation/Konfiguration/Konfiguration, Veröffentlichung/Herunterladen von Daten usw.).

## Ziele und Lernergebnisse

Die Ziele dieser Schulung sind, sich mit den folgenden Punkten vertraut zu machen:

- Kernkonzepte und Komponenten der WIS2-Architektur
- Daten- und Metadatenformate, die in WIS2 für Entdeckung und Zugriff verwendet werden
- wis2box Architektur und Umgebung
- Kernfunktionen von wis2box:
    - Verwaltung von Metadaten
    - Datenerfassung und -umwandlung in das BUFR-Format
    - MQTT-Broker für die Veröffentlichung von WIS2-Nachrichten
    - HTTP-Endpunkt für den Daten-Download
    - API-Endpunkt für den programmatischen Zugriff auf Daten

## Navigation

Die linke Navigation bietet ein Inhaltsverzeichnis für die gesamte Schulung.

Die rechte Navigation bietet ein Inhaltsverzeichnis für eine spezifische Seite.

## Voraussetzungen

### Wissen

- Grundlegende Linux-Befehle (siehe das [Cheatsheet](cheatsheets/linux.md))
- Grundkenntnisse über Netzwerke und Internetprotokolle

### Software

Für diese Schulung werden folgende Tools benötigt:

- Eine Instanz mit Ubuntu-Betriebssystem (wird von WMO-Trainer während lokaler Schulungssitzungen bereitgestellt) siehe [Zugriff auf Ihr Studenten-VM](practical-sessions/accessing-your-student-vm.md#introduction)
- SSH-Client für den Zugriff auf Ihre Instanz
- MQTT Explorer auf Ihrem lokalen Rechner
- SCP- und FTP-Client zum Kopieren von Dateien von Ihrem lokalen Rechner

## Konventionen

!!! Frage

    Ein Abschnitt wie dieser fordert Sie auf, eine Frage zu beantworten.

Außerdem werden Sie Tipps und Hinweise innerhalb des Textes bemerken:

!!! Tipp

    Tipps geben Hilfe, wie man Aufgaben am besten bewältigt.

!!! Hinweis

    Hinweise bieten zusätzliche Informationen zum Thema der praktischen Sitzung sowie dazu, wie Aufgaben am besten bewältigt werden.

Beispiele werden wie folgt angezeigt:

Konfiguration
``` {.yaml linenums="1"}
my-collection-defined-in-yaml:
    type: collection
    title: mein Titel definiert als ein YAML-Attribut namens title
    description: meine Beschreibung als ein YAML-Attribut namens description
```

Code-Schnipsel, die in einem Terminal/Konsole eingegeben werden müssen, werden angezeigt als:

```bash
echo 'Hallo Welt'
```

Container-Namen (laufende Images) werden in **fett** dargestellt.

## Schulungsort und -materialien

Die Schulungsinhalte, das Wiki und der Issue Tracker werden auf GitHub unter [https://github.com/wmo-im/wis2box-training](https://github.com/wmo-im/wis2box-training) verwaltet.

## Drucken des Materials

Diese Schulung kann als PDF exportiert werden. Um dieses Schulungsmaterial zu speichern oder zu drucken, gehen Sie zur [Druckseite](print_page) und wählen
Datei > Drucken > Als PDF speichern.

## Übungsmaterialien

Übungsmaterialien können von der [exercise-materials.zip](/exercise-materials.zip) Zip-Datei heruntergeladen werden.

## Unterstützung

Für Probleme/Bugs/Vorschläge oder Verbesserungen/Beiträge zu dieser Schulung nutzen Sie bitte den [GitHub-Issue-Tracker](https://github.com/wmo-im/wis2box-training/issues).

Alle wis2box-Bugs, Verbesserungen und Probleme können auf [GitHub](https://github.com/wmo-im/wis2box/issues) gemeldet werden.

Für zusätzliche Unterstützung oder Fragen kontaktieren Sie bitte wis2-support@wmo.int.

Wie immer kann die Kern-Dokumentation von wis2box immer unter [https://docs.wis2box.wis.wmo.int](https://docs.wis2box.wis.wmo.int) gefunden werden.

Beiträge sind immer ermutigt und willkommen!