---
title: Configurando um conjunto de dados recomendado com controle de acesso
---

# Configurando um conjunto de dados recomendado com controle de acesso

!!! abstract "Resultados de aprendizado"
    Ao final desta sessão prática, você será capaz de:

    - criar um novo conjunto de dados com política de dados 'recomendada'
    - adicionar um token de acesso ao conjunto de dados
    - validar que o conjunto de dados não pode ser acessado sem o token de acesso
    - adicionar o token de acesso aos cabeçalhos HTTP para acessar o conjunto de dados

## Introdução

Conjuntos de dados que não são considerados 'núcleo' no WMO podem ser configurados opcionalmente com uma política de controle de acesso. O wis2box fornece um mecanismo para adicionar um token de acesso a um conjunto de dados, o que impedirá os usuários de baixar dados a menos que forneçam o token de acesso nos cabeçalhos HTTP.

## Preparação

Certifique-se de ter acesso SSH à sua VM de estudante e que sua instância do wis2box esteja funcionando.

Certifique-se de estar conectado ao broker MQTT da sua instância do wis2box usando o MQTT Explorer. Você pode usar as credenciais públicas `everyone/everyone` para se conectar ao broker.

Certifique-se de ter um navegador web aberto com o wis2box-webapp para sua instância acessando `http://<seu-host>/wis2box-webapp`.

## Exercício 1: criar um novo conjunto de dados com política de dados 'recomendada'

Vá para a página 'editor de conjunto de dados' no wis2box-webapp e crie um novo conjunto de dados. Use o mesmo centro-id das sessões práticas anteriores e use o template='surface-weather-observations/synop'.

Clique em 'OK' para prosseguir.

No editor de conjunto de dados, defina a política de dados para 'recomendada' (note que alterar a política de dados atualizará a 'Hierarquia de Tópicos').
Substitua o 'ID Local' gerado automaticamente por um nome descritivo para o conjunto de dados, por exemplo, 'dados-recomendados-com-controle-de-acesso':

<img alt="create-dataset-recommended" src="../../assets/img/create-dataset-recommended.png" width="800">

Continue preenchendo os campos necessários para Propriedades Espaciais e Informações de Contato, e 'Validar formulário' para verificar se há erros.

Finalmente, envie o conjunto de dados, usando o token de autenticação criado anteriormente, e verifique se o novo conjunto de dados foi criado no wis2box-webapp.

Verifique o MQTT-explorer para ver se você recebe a Mensagem de Notificação WIS2 anunciando o novo registro de Metadados de Descoberta no tópico `origin/a/wis2/<seu-centre-id>/metadata`.

## Exercício 2: adicionar um token de acesso ao conjunto de dados

Faça login no container de gerenciamento do wis2box,

```bash
cd ~/wis2box-1.0.0rc1
python3 wis2box-ctl.py login
```

Do comando de linha dentro do container, você pode proteger um conjunto de dados usando o comando `wis2box auth add-token`, usando a flag `--metadata-id` para especificar o identificador de metadados do conjunto de dados e o token de acesso como argumento.

Por exemplo, para adicionar o token de acesso `S3cr3tT0k3n` ao conjunto de dados com identificador de metadados `urn:wmo:md:not-my-centre:core.surface-based-observations.synop`:

```bash
wis2box auth add-token --metadata-id urn:wmo:md:not-my-centre:reco.surface-based-observations.synop S3cr3tT0k3n
```

Saia do container de gerenciamento do wis2box:

```bash
exit
```

## Exercício 3: publicar alguns dados no conjunto de dados

Copie o arquivo `exercise-materials/access-control-exercises/aws-example2.csv` para o diretório definido por `WIS2BOX_HOST_DATADIR` no seu `wis2box.env`:

```bash
cp ~/exercise-materials/access-control-exercises/aws-example2.csv ~/wis2box-data
```

Em seguida, use o WinSCP ou um editor de linha de comando para editar o arquivo `aws-example2.csv` e atualizar os identificadores de estação WIGOS nos dados de entrada para corresponder às estações que você tem em sua instância do wis2box.

Depois, vá para o editor de estações no wis2box-webapp. Para cada estação que você usou em `aws-example2.csv`, atualize o campo 'tópico' para corresponder ao 'tópico' do conjunto de dados que você criou no exercício anterior.

Esta estação agora estará associada a 2 tópicos, um para o conjunto de dados 'núcleo' e outro para o conjunto de dados 'recomendado':

<img alt="edit-stations-add-topics" src="../../assets/img/edit-stations-add-topics.png" width="600">

Você precisará usar seu token para `collections/stations` para salvar os dados atualizados da estação.

Em seguida, faça login no container de gerenciamento do wis2box:

```bash
cd ~/wis2box-1.0.0rc1
python3 wis2box-ctl.py login
```

Do comando de linha do wis2box, podemos ingerir o arquivo de dados de exemplo `aws-example2.csv` em um conjunto de dados específico da seguinte forma:

```bash
wis2box data ingest -p /data/wis2box/aws-example2.csv --metadata-id urn:wmo:md:not-my-centre:reco.surface-based-observations.synop
```

Certifique-se de fornecer o identificador de metadados correto para seu conjunto de dados e **verifique se você recebe notificações de dados WIS2 no MQTT Explorer**, no tópico `origin/a/wis2/<seu-centre-id>/data/recommended/surface-based-observations/synop`.

Verifique o link canônico na Mensagem de Notificação WIS2 e copie/cole o link no navegador para tentar baixar os dados.

Você deve ver um erro 403 Proibido.

## Exercício 4: adicionar o token de acesso aos cabeçalhos HTTP para acessar o conjunto de dados

Para demonstrar que o token de acesso é necessário para acessar o conjunto de dados, reproduziremos o erro que você viu no navegador usando a função de linha de comando `wget`.

Da linha de comando na sua VM de estudante, use o comando `wget` com o link canônico que você copiou da Mensagem de Notificação WIS2.

```bash
wget <canonical-link>
```

Você verá que a solicitação HTTP retorna com *401 Não autorizado* e os dados não são baixados.

Agora adicione o token de acesso aos cabeçalhos HTTP para acessar o conjunto de dados.

```bash
wget --header="Authorization: Bearer S3cr3tT0k3n" <canonical-link>
```

Agora os dados devem ser baixados com sucesso.

## Conclusão

!!! success "Parabéns!"
    Nesta sessão prática, você aprendeu como:

    - criar um novo conjunto de dados com política de dados 'recomendada'
    - adicionar um token de acesso ao conjunto de dados
    - validar que o conjunto de dados não pode ser acessado sem o token de acesso
    - adicionar o token de acesso aos cabeçalhos HTTP para acessar o conjunto de dados