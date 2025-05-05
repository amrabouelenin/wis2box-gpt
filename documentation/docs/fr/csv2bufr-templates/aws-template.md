---
title: Modèle AWS
---

# Modèle csv2bufr pour les stations météorologiques automatiques transmettant des données GBON horaires

Le **Modèle AWS** utilise un format CSV standardisé pour ingérer des données provenant des stations météorologiques automatiques conformément aux exigences de transmission GBON. Ce modèle de mappage convertit les données CSV en séquence BUFR 301150, 307096.

Le format est destiné à être utilisé avec des stations météorologiques automatiques qui transmettent un nombre minimal de paramètres, notamment la pression, la température et l'humidité de l'air, la vitesse et la direction du vent ainsi que les précipitations sur une base horaire.

## Colonnes CSV et description

{{ read_csv("docs/assets/tables/aws-minimal.csv") }}

## Exemple

Exemple de fichier CSV conforme au modèle AWS : [aws-example.csv](/sample-data/aws-example.csv).