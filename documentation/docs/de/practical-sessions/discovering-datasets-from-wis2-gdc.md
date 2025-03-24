---
title: Entdecken von Datensätzen aus dem WIS2 Global Discovery Katalog
---

# Entdecken von Datensätzen aus dem WIS2 Global Discovery Katalog

!!! abstract "Lernergebnisse!"

    Am Ende dieser praktischen Sitzung werden Sie in der Lage sein:

    - pywiscat zu verwenden, um Datensätze aus dem Global Discovery Katalog (GDC) zu entdecken

## Einführung

In dieser Sitzung lernen Sie, wie man Daten aus dem WIS2 Global Discovery Katalog (GDC) entdeckt.

Derzeit sind die folgenden GDCs verfügbar:

- Umwelt und Klimawandel Kanada, Meteorologischer Dienst von Kanada: <https://wis2-gdc.weather.gc.ca>
- China Meteorological Administration: <https://gdc.wis.cma.cn/api>
- Deutscher Wetterdienst: <https://wis2.dwd.de/gdc>

Während lokaler Trainingssitzungen wird ein lokaler GDC eingerichtet, um den Teilnehmern zu ermöglichen, den GDC nach den von ihnen aus ihren wis2box-Instanzen veröffentlichten Metadaten zu durchsuchen. In diesem Fall werden die Trainer die URL zum lokalen GDC bereitstellen.

## Vorbereitung

!!! note
    Bitte loggen Sie sich vor Beginn in Ihre Studenten-VM ein.

## Installation von pywiscat

Verwenden Sie den Python-Paketinstaller `pip3`, um pywiscat auf Ihrer VM zu installieren:
```bash
pip3 install pywiscat
```

!!! note

    Wenn Sie auf den folgenden Fehler stoßen:

    ```
    WARNING: The script pywiscat is installed in '/home/username/.local/bin' which is not on PATH.
    Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
    ```

    Dann führen Sie den folgenden Befehl aus:

    ```bash
    export PATH=$PATH:/home/$USER/.local/bin
    ```

    ...wobei `$USER` Ihr Benutzername auf Ihrer VM ist.

Überprüfen Sie, ob die Installation erfolgreich war:

```bash
pywiscat --version
```

## Daten finden mit pywiscat

Standardmäßig verbindet sich pywiscat mit Kanadas Global Discovery Katalog. Konfigurieren wir pywiscat, um den Trainings-GDC abzufragen, indem wir die Umgebungsvariable `PYWISCAT_GDC_URL` setzen:

```bash
export PYWISCAT_GDC_URL=http://<local-gdc-host-or-ip>
```

Verwenden wir [pywiscat](https://github.com/wmo-im/pywiscat), um den GDC im Rahmen des Trainings abzufragen.

```bash
pywiscat search --help
```

Suchen Sie jetzt im GDC nach allen Datensätzen:

```bash
pywiscat search
```

!!! question

    Wie viele Datensätze werden von der Suche zurückgegeben?

??? success "Klicken, um die Antwort zu enthüllen"
    Die Anzahl der Datensätze hängt vom abgefragten GDC ab. Wenn Sie den lokalen Trainings-GDC verwenden, sollten Sie sehen, dass die Anzahl der Datensätze gleich der Anzahl der Datensätze ist, die während der anderen praktischen Sitzungen in den GDC eingespeist wurden.

Versuchen wir, den GDC mit einem Schlüsselwort abzufragen:

```bash
pywiscat search -q observations
```

!!! question

    Wie lautet die Datenrichtlinie der Ergebnisse?

??? success "Klicken, um die Antwort zu enthüllen"
    Alle zurückgegebenen Daten sollten als "Kerndaten" gekennzeichnet sein

Versuchen Sie zusätzliche Abfragen mit `-q`

!!! tip

    Das `-q` Flag ermöglicht die folgende Syntax:

    - `-q synop`: findet alle Datensätze mit dem Wort "synop"
    - `-q temp`: findet alle Datensätze mit dem Wort "temp"
    - `-q "observations AND fiji"`: findet alle Datensätze mit den Wörtern "observations" und "fiji"
    - `-q "observations NOT fiji"`: findet alle Datensätze, die das Wort "observations" enthalten, aber nicht das Wort "fiji"
    - `-q "synop OR temp"`: findet alle Datensätze mit "synop" oder "temp"
    - `-q "obs~"`: unscharfe Suche

    Bei der Suche nach Begriffen mit Leerzeichen setzen Sie diese in Anführungszeichen.

Lassen Sie uns mehr Details zu einem spezifischen Suchergebnis erhalten, das uns interessiert:

```bash
pywiscat get <id>
```

!!! tip

    Verwenden Sie den `id`-Wert aus der vorherigen Suche.


## Schlussfolgerung

!!! success "Herzlichen Glückwunsch!"

    In dieser praktischen Sitzung haben Sie gelernt, wie man:

    - pywiscat verwendet, um Datensätze aus dem WIS2 Global Discovery Katalog zu entdecken

