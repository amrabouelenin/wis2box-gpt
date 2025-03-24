---
title: Zugriff auf dein Studenten-VM
---

# Zugriff auf dein Studenten-VM

!!! abstract "Lernergebnisse"

    Am Ende dieser praktischen Sitzung wirst du in der Lage sein:

    - auf dein Studenten-VM über SSH und WinSCP zuzugreifen
    - zu überprüfen, ob die erforderliche Software für die praktischen Übungen installiert ist
    - zu überprüfen, ob du Zugang zu den Übungsmaterialien für dieses Training auf deinem lokalen Studenten-VM hast

## Einleitung

Im Rahmen von lokal durchgeführten wis2box-Schulungen kannst du auf dein persönliches Studenten-VM im lokalen Trainingsnetzwerk namens "WIS2-Training" zugreifen.

Auf deinem Studenten-VM ist die folgende Software vorinstalliert:

- Ubuntu 22.0.4.3 LTS [ubuntu-22.04.3-live-server-amd64.iso](https://releases.ubuntu.com/jammy/ubuntu-22.04.3-live-server-amd64.iso)
- Python 3.10.12
- Docker 24.0.6
- Docker Compose 2.21.0
- Texteditoren: vim, nano

!!! note

    Wenn du dieses Training außerhalb einer lokalen Schulungssitzung durchführen möchtest, kannst du deine eigene Instanz über einen beliebigen Cloud-Anbieter bereitstellen, zum Beispiel:

    - GCP (Google Cloud Platform) VM-Instanz `e2-medium`
    - AWS (Amazon Web Services) ec2-Instanz `t3a.medium`
    - Azure (Microsoft) Azure Virtual Machine `standard_b2s`

    Wähle als Betriebssystem Ubuntu Server 22.0.4 LTS.
    
    Nachdem du deine VM erstellt hast, stelle sicher, dass Python, Docker und Docker Compose installiert sind, wie unter [wis2box-software-dependencies](https://docs.wis2box.wis.wmo.int/en/latest/user/getting-started.html#software-dependencies) beschrieben.
    
    Das Release-Archiv für wis2box, das in diesem Training verwendet wird, kann wie folgt heruntergeladen werden:

    ```bash
    wget https://github.com/wmo-im/wis2box/releases/download/1.0.0rc1/wis2box-setup-1.0.0rc1.zip
    unzip wis2box-setup-1.0.0rc1.zip
    ```
    
    Das neueste 'wis2box-setup'-Archiv findest du immer unter [https://github.com/wmo-im/wis2box/releases](https://github.com/wmo-im/wis2box/releases).

    Das Übungsmaterial, das in diesem Training verwendet wird, kann wie folgt heruntergeladen werden:

    ```bash
    wget https://training.wis2box.wis.wmo.int/exercise-materials.zip
    unzip exercise-materials.zip
    ```

    Die folgenden zusätzlichen Python-Pakete sind erforderlich, um die Übungsmaterialien auszuführen:

    ```bash
    pip3 install minio
    ```

    Wenn du das Studenten-VM verwendest, das während der lokalen WIS2-Schulungen bereitgestellt wird, ist die erforderliche Software bereits installiert.

## Verbinde dich mit deinem Studenten-VM im lokalen Trainingsnetzwerk

Verbinde deinen PC mit dem lokalen WLAN, das während der WIS2-Schulung im Raum ausgestrahlt wird, gemäß den Anweisungen des Trainers.

Verwende einen SSH-Client, um dich mit deinem Studenten-VM zu verbinden, verwende dazu:

- **Host: (während der Präsenzschulung bereitgestellt)**
- **Port: 22**
- **Benutzername: (während der Präsenzschulung bereitgestellt)**
- **Passwort: (während der Präsenzschulung bereitgestellt)**

!!! tip
    Kontaktiere einen Trainer, wenn du dir beim Hostnamen/Benutzernamen unsicher bist oder Probleme beim Verbinden hast.

Sobald du verbunden bist, ändere bitte dein Passwort, um sicherzustellen, dass andere keinen Zugriff auf dein VM haben:

```bash
limper@student-vm:~$ passwd
Passwort ändern für testuser.
Aktuelles Passwort:
Neues Passwort:
Neues Passwort wiederholen:
passwd: Passwort erfolgreich aktualisiert
```

## Überprüfe die Softwareversionen

Um wis2box ausführen zu können, sollten Python, Docker und Docker Compose auf dem Studenten-VM vorinstalliert sein.

Überprüfe die Python-Version:
```bash
python3 --version
```
gibt zurück:
```console
Python 3.10.12
```

Überprüfe die Docker-Version:
```bash
docker --version
```
gibt zurück:
```console
Docker-Version 24.0.6, Build ed223bc
```

Überprüfe die Docker Compose-Version:
```bash
docker compose version
```
gibt zurück:
```console
Docker Compose-Version v2.21.0
```

Um sicherzustellen, dass dein Benutzer Docker-Befehle ausführen kann, wurde dein Benutzer zur `docker`-Gruppe hinzugefügt.

Um zu testen, dass dein Benutzer docker hello-world ausführen kann, führe den folgenden Befehl aus:
```bash
docker run hello-world
```

Dies sollte das hello-world-Image herunterladen und einen Container ausführen, der eine Nachricht ausgibt.

Überprüfe, ob du Folgendes in der Ausgabe siehst:

```console
...
Hallo von Docker!
Diese Nachricht zeigt, dass deine Installation anscheinend korrekt funktioniert.
...
```

## Überprüfe die Übungsmaterialien

Überprüfe den Inhalt deines Home-Verzeichnisses; diese Materialien werden als Teil des Trainings und der praktischen Sitzungen verwendet.

```bash
ls ~/
```
gibt zurück:
```console
exercise-materials  wis2box-1.0.0rc1
```

Wenn du WinSCP auf deinem lokalen PC installiert hast, kannst du es verwenden, um dich mit deinem Studenten-VM zu verbinden und den Inhalt deines Home-Verzeichnisses zu inspizieren sowie Dateien zwischen deinem VM und deinem lokalen PC herunterzuladen oder hochzuladen.

WinSCP ist nicht für das Training erforderlich, kann aber nützlich sein, wenn du Dateien auf deinem VM mit einem Texteditor auf deinem lokalen PC bearbeiten möchtest.

So kannst du dich mit WinSCP mit deinem Studenten-VM verbinden:

Öffne WinSCP und klicke auf "Neue Seite". Du kannst eine neue SCP-Verbindung zu deinem VM wie folgt erstellen:

<img alt="winscp-student-vm-scp.png" src="../../assets/img/winscp-student-vm-scp.png" width="400">

Klicke auf 'Speichern' und dann auf 'Anmelden', um dich mit deinem VM zu verbinden.

Und du solltest den folgenden Inhalt sehen können:

<img alt="winscp-student-vm-exercise-materials.png" src="../../assets/img/winscp-student-vm-exercise-materials.png" width="600">

## Schlussfolgerung

!!! success "Herzlichen Glückwunsch!"
    In dieser praktischen Sitzung hast du gelernt, wie man:

    - auf dein Studenten-VM über SSH und WinSCP zugreift
    - überprüft, ob die erforderliche Software für die praktischen Übungen installiert ist
    - überprüft, ob du Zugang zu den Übungsmaterialien für dieses Training auf deinem lokalen Studenten-VM hast