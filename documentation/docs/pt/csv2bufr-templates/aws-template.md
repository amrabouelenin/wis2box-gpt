---
title: Template AWS
---

# Template csv2bufr para Estações Meteorológicas Automáticas reportando dados GBON por hora

O **Template AWS** usa um formato CSV padronizado para ingerir dados de Estações Meteorológicas Automáticas em suporte aos requisitos de relatórios GBON. Este template de mapeamento converte dados CSV para a sequência BUFR 301150, 307096.

O formato é destinado ao uso com estações meteorológicas automáticas que reportam um número mínimo de parâmetros, incluindo pressão, temperatura do ar e umidade, velocidade e direção do vento e precipitação em base horária.

## Colunas CSV e descrição

{{ read_csv("docs/assets/tables/aws-minimal.csv") }}

## Exemplo

Arquivo CSV de exemplo que está em conformidade com o template AWS: [aws-example.csv](/sample-data/aws-example.csv).