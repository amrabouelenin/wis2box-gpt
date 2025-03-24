---
title: WIS2 in a box - scheda di riferimento rapido
---

# WIS2 in a box - scheda di riferimento rapido

## Panoramica

wis2box funziona come una suite di comandi Docker Compose. Il comando ``wis2box-ctl.py`` è uno strumento
(scritto in Python) per eseguire comandi Docker Compose facilmente.

## Comandi essenziali di wis2box

### Avvio e arresto

* Avvia wis2box:

```bash
python3 wis2box-ctl.py start
```

* Arresta wis2box:

```bash
python3 wis2box-ctl.py stop
```

* Verifica che tutti i container di wis2box siano in esecuzione:

```bash
python3 wis2box-ctl.py status
```

* Accedi a un container di wis2box (*wis2box-management* di default):

```bash
python3 wis2box-ctl.py login
```

* Accedi a un container specifico di wis2box:

```bash
python3 wis2box-ctl.py login wis2box-api
```