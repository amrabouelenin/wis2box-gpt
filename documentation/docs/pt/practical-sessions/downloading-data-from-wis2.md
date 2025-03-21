---
title: Baixando e decodificando dados do WIS2
---

# Baixando e decodificando dados do WIS2

!!! abstract "Resultados de aprendizado!"

    Ao final desta sessão prática, você será capaz de:

    - usar o "wis2downloader" para se inscrever em notificações de dados do WIS2 e baixar dados para seu sistema local
    - visualizar o status dos downloads no painel do Grafana
    - decodificar alguns dados baixados usando o container "decode-bufr-jupyter"

## Introdução

Nesta sessão você aprenderá como configurar uma inscrição em um Broker do WIS2 e baixar automaticamente dados para seu sistema local usando o serviço "wis2downloader" incluído no wis2box.

!!! note "Sobre o wis2downloader"
     
     O wis2downloader também está disponível como um serviço autônomo que pode ser executado em um sistema diferente daquele que está publicando as notificações do WIS2. Veja [wis2downloader](https://pypi.org/project/wis2downloader/) para mais informações sobre o uso do wis2downloader como um serviço autônomo.

     Se você deseja desenvolver seu próprio serviço para se inscrever em notificações do WIS2 e baixar dados, você pode usar o [código fonte do wis2downloader](https://github.com/wmo-im/wis2downloader) como referência.

!!! Other tools for accessing WIS2 data

    As seguintes ferramentas também podem ser usadas para descobrir e acessar dados do WIS2:

    - [pywiscat](https://github.com/wmo-im/pywiscat) oferece capacidade de busca no Catálogo Global de Descoberta do WIS2 em apoio ao relatório e análise do Catálogo do WIS2 e seus metadados associados
    - [pywis-pubsub](https://github.com/wmo-im/pywis-pubsub) oferece capacidade de inscrição e download de dados da OMM a partir dos serviços de infraestrutura do WIS2

## Preparação

Antes de começar, por favor, faça login em sua VM de estudante e certifique-se de que sua instância do wis2box está funcionando.

## Exercício 1: visualizando o painel do wis2download no Grafana

Abra um navegador web e navegue até o painel do Grafana para sua instância do wis2box acessando `http://<seu-host>:3000`.

Clique em painéis no menu à esquerda, e então selecione o **painel do wis2downloader**.

Você deverá ver o seguinte painel:

![Painel do wis2downloader](../assets/img/wis2downloader-dashboard.png)

Este painel é baseado nas métricas publicadas pelo serviço do wis2downloader e mostrará o status dos downloads que estão em andamento.

No canto superior esquerdo você pode ver as inscrições que estão atualmente ativas.

Mantenha este painel aberto, pois você o usará para monitorar o progresso do download no próximo exercício.

## Exercício 2: revisando a configuração do wis2downloader

O serviço do wis2downloader iniciado pela pilha do wis2box pode ser configurado usando as variáveis de ambiente definidas em seu arquivo wis2box.env.

As seguintes variáveis de ambiente são usadas pelo wis2downloader:

    - DOWNLOAD_BROKER_HOST: O nome do host do broker MQTT a conectar. Padrão é globalbroker.meteo.fr
    - DOWNLOAD_BROKER_PORT: A porta do broker MQTT a conectar. Padrão é 443 (HTTPS para websockets)
    - DOWNLOAD_BROKER_USERNAME: O nome de usuário para usar ao conectar ao broker MQTT. Padrão é everyone
    - DOWNLOAD_BROKER_PASSWORD: A senha para usar ao conectar ao broker MQTT. Padrão é everyone
    - DOWNLOAD_BROKER_TRANSPORT: websockets ou tcp, o mecanismo de transporte para usar ao conectar ao broker MQTT. Padrão é websockets,
    - DOWNLOAD_RETENTION_PERIOD_HOURS: O período de retenção em horas para os dados baixados. Padrão é 24
    - DOWNLOAD_WORKERS: O número de trabalhadores de download para usar. Padrão é 8. Determina o número de downloads paralelos.
    - DOWNLOAD_MIN_FREE_SPACE_GB: O espaço livre mínimo em GB a manter no volume que hospeda os downloads. Padrão é 1.

Para revisar a configuração atual do wis2downloader, você pode usar o seguinte comando:

```bash
cat ~/wis2box-1.0.0rc1/wis2box.env | grep DOWNLOAD
```

!!! question "Reveja a configuração do wis2downloader"
    
    Qual é o broker MQTT padrão ao qual o wis2downloader se conecta?

    Qual é o período de retenção padrão para os dados baixados?

??? success "Clique para revelar a resposta"

    O broker MQTT padrão ao qual o wis2downloader se conecta é `globalbroker.meteo.fr`.

    O período de retenção padrão para os dados baixados é de 24 horas.

!!! note "Atualizando a configuração do wis2downloader"

    Para atualizar a configuração do wis2downloader, você pode editar o arquivo wis2box.env. Para aplicar as mudanças, você pode executar novamente o comando de início para a pilha do wis2box:

    ```bash
    python3 wis2box-ctl.py start
    ```

    E você verá o serviço do wis2downloader reiniciar com a nova configuração.

Você pode manter a configuração padrão para o propósito deste exercício.

## Exercício 3: adicionando inscrições ao wis2downloader

Dentro do container **wis2downloader**, você pode usar a linha de comando para listar, adicionar e deletar inscrições.

Para fazer login no container **wis2downloader**, use o seguinte comando:

```bash
python3 wis2box-ctl.py login wis2downloader
```

Em seguida, use o seguinte comando para listar as inscrições que estão atualmente ativas:

```bash
wis2downloader list-subscriptions
```

Este comando retorna uma lista vazia, pois não há inscrições ativas no momento.

Para o propósito deste exercício, vamos nos inscrever no seguinte tópico `cache/a/wis2/de-dwd-gts-to-wis2/#`, para se inscrever em dados publicados pelo gateway GTS-to-WIS2 hospedado pela DWD e notificações de download do Cache Global.

Para adicionar esta inscrição, use o seguinte comando:

```bash
wis2downloader add-subscription --topic cache/a/wis2/de-dwd-gts-to-wis2/#
```

Em seguida, saia do container **wis2downloader** digitando `exit`:

```bash
exit
```

Verifique o painel do wis2downloader no Grafana para ver a nova inscrição adicionada. Espere alguns minutos e você deverá ver os primeiros downloads começando. Vá para o próximo exercício assim que confirmar que os downloads estão começando.

## Exercício 4: visualizando os dados baixados

O serviço do wis2downloader na pilha do wis2box baixa os dados no diretório 'downloads' no diretório que você definiu como WIS2BOX_HOST_DATADIR em seu arquivo wis2box.env. Para visualizar o conteúdo do diretório de downloads, você pode usar o seguinte comando:

```bash
ls -R ~/wis2box-data/downloads
```

Note que os dados baixados são armazenados em diretórios nomeados após o tópico em que a Notificação WIS2 foi publicada.

## Exercício 5: removendo inscrições do wis2downloader

Em seguida, faça login novamente no container do wis2downloader:

```bash
python3 wis2box-ctl.py login wis2downloader
```

e remova a inscrição que você fez do wis2downloader, usando o seguinte comando:

```bash
wis2downloader remove-subscription --topic cache/a/wis2/de-dwd-gts-to-wis2/#
```

E saia do container do wis2downloader digitando `exit`:
    
```bash
exit
```

Verifique o painel do wis2downloader no Grafana para ver a inscrição removida. Você deverá ver os downloads parando.

## Exercício 6: inscreva-se no wis2training-broker e configure uma nova inscrição

Para o próximo exercício, vamos nos inscrever no wis2training-broker.

Isso demonstra como se inscrever em um broker que não é o broker padrão e permitirá que você baixe alguns dados publicados pelo Broker de Treinamento WIS2.

Edite o arquivo wis2box.env e altere o DOWNLOAD_BROKER_HOST para `wis2training-broker.wis2dev.io`, altere DOWNLOAD_BROKER_PORT para `1883` e altere DOWNLOAD_BROKER_TRANSPORT para `tcp`:

```copy
# configurações do downloader
DOWNLOAD_BROKER_HOST=wis2training-broker.wis2dev.io
DOWNLOAD_BROKER_PORT=1883
DOWNLOAD_BROKER_USERNAME=everyone
DOWNLOAD_BROKER_PASSWORD=everyone
# mecanismo de transporte de download (tcp ou websockets)
DOWNLOAD_BROKER_TRANSPORT=tcp
```

Em seguida, reinicie a pilha do wis2box para aplicar as mudanças:

```bash
python3 wis2box-ctl.py start
```

Verifique os logs do wis2downloader para ver se a conexão com o novo broker foi bem-sucedida:

```bash
docker logs wis2downloader
```

Você deverá ver a seguinte mensagem de log:

```copy
...
INFO - Conectando...
INFO - Host: wis2training-broker.wis2dev.io, port: 1883
INFO - Conectado com sucesso
```

Agora vamos configurar uma nova inscrição para o tópico para baixar dados de trajetória de ciclones do Broker de Treinamento WIS2.

Faça login no container **wis2downloader**:

```bash
python3 wis2box-ctl.py login wis2downloader
```

E execute o seguinte comando (copie e cole isso para evitar erros de digitação):

```bash
wis2downloader add-subscription --topic origin/a/wis2/int-wis2-training/data/core/weather/prediction/forecast/medium-range/probabilistic/trajectory
```

Saia do container **wis2downloader** digitando `exit`.

Espere até ver os downloads começando no painel do wis2downloader no Grafana.

!!! note "Baixando dados do Broker de Treinamento WIS2"

    O Broker de Treinamento WIS2 é um broker de teste que é usado para fins de treinamento e pode não publicar dados o tempo todo.

    Durante as sessões de treinamento presenciais, o instrutor local garantirá que o Broker de Treinamento WIS2 publique dados para você baixar.

    Se você estiver fazendo este exercício fora de uma sessão de treinamento, você pode não ver nenhum dado sendo baixado.

Verifique se os dados foram baixados verificando os logs do wis2downloader novamente com:

```bash
docker logs wis2downloader
```

Você deverá ver uma mensagem de log semelhante à seguinte:

```copy
[...] INFO - Mensagem recebida sob o tópico origin/a/wis2/int-wis2-training/data/core/weather/prediction/forecast/medium-range/probabilistic/trajectory
[...] INFO - Baixado A_JSXX05ECEP020000_C_ECMP_...
```

## Exercício 7: decodificando os dados baixados

Para demonstrar como você pode decodificar os dados baixados, vamos iniciar um novo container usando a imagem 'decode-bufr-jupyter'.

Este container iniciará um servidor de notebook Jupyter em sua instância que inclui a biblioteca "ecCodes" que você pode usar para decodificar dados BUFR.

Usaremos os notebooks de exemplo incluídos em `~/exercise-materials/notebook-examples` para decodificar os dados baixados para as trajetórias de ciclones.

Para iniciar o container, use o seguinte comando:

```bash
docker run -d --name decode-bufr-jupyter \
    -v ~/wis2box-data/downloads:/root/downloads \
    -p 8888:8888 \
    -e JUPYTER_TOKEN=dataismagic! \
    mlimper/decode-bufr-jupyter
```

!!! note "Sobre o container decode-bufr-jupyter"

    O container `decode-bufr-jupyter` é um container personalizado que inclui a biblioteca ecCodes e executa um servidor de notebook Jupyter. O container é baseado em uma imagem que inclui a biblioteca `ecCodes` para decodificar dados BUFR, junto com bibliotecas para plotagem e análise de dados.

    O comando acima inicia o container no modo desanexado, com o nome `decode-bufr-jupyter`, a porta 8888 é mapeada para o sistema hospedeiro e a variável de ambiente `JUPYTER_TOKEN` é definida como `dataismagic!`.
    
    O comando acima também monta o diretório `~/wis2box-data/downloads` para `/root/downloads` no container. Isso garante que os dados baixados estejam disponíveis para o servidor de notebook Jupyter.
    
Uma vez que o container seja iniciado, você pode acessar o servidor de notebook Jupyter navegando até `http://<seu-host>:8888` em seu navegador web.

Você verá uma tela solicitando que você insira uma "Senha ou token".

Forneça o token `dataismagic!` para fazer login no servidor de notebook Jupyter.

Após fazer login, você deverá ver a seguinte tela listando os diretórios no container:

![Tela inicial do notebook Jupyter](../assets/img/jupyter-files-screen1.png)

Dê um duplo clique no diretório `example-notebooks` para abri-lo.

Você deverá ver a seguinte tela listando os notebooks de exemplo, dê um duplo clique no notebook `tropical_cyclone_track.ipynb` para abri-lo:

![Notebooks de exemplo do Jupyter](../assets/img/jupyter-files-screen2.png)

Você agora está no notebook Jupyter para decodificar os dados da trajetória do ciclone tropical:

![Notebook Jupyter da trajetória do ciclone tropical](../assets/img/jupyter-tropical-cyclone-track.png)

Leia as instruções no notebook e execute as células para decodificar os dados baixados para as trajetórias dos ciclones tropicais. Execute cada célula clicando na célula e depois clicando no botão de executar na barra de ferramentas ou pressionando `Shift+Enter`.

No final, você deverá ver um gráfico da probabilidade de impacto para as trajetórias dos ciclones tropicais:

![Trajetórias dos ciclones tropicais](../assets/img/tropical-cyclone-track-map.png)

!!! question 

    O resultado exibe a probabilidade prevista de trajetória de tempestade tropical dentro de 200 km. Como você atualizaria o notebook para exibir a probabilidade prevista de trajetória de tempestade tropical dentro de 300 km?

??? success "Clique para revelar a resposta"

    Para atualizar o notebook para exibir a probabilidade prevista de trajetória de tempestade tropical dentro de uma distância diferente, você pode atualizar a variável `distance_threshold` no bloco de código que calcula a probabilidade de impacto.

    Para exibir a probabilidade prevista de trajetória de tempestade tropical dentro de 300 km,

    ```python
    # definir o limite de distância (metros)
    distance_threshold = 300000  # 300 km em metros
    ```

    Em seguida, execute novamente as células no notebook para ver o gráfico atualizado.

!!! note "Decodificando dados BUFR"

    O exercício que você acabou de fazer forneceu um exemplo específico de como você pode decodificar dados BUFR usando a biblioteca ecCodes. Diferentes tipos de dados podem exigir diferentes etapas de decodificação e você pode precisar consultar a documentação para o tipo de dados com o qual está trabalhando.
    
    Para mais informações, consulte a [documentação do ecCodes](https://confluence.ecmwf.int/display/ECC).


## Conclusão

!!! success "Parabéns!"

    Nesta sessão prática, você aprendeu como:

    - usar o 'wis2downloader' para se inscrever em um Broker do WIS2 e baixar dados para seu sistema local
    - visualizar o status dos downloads no painel do Grafana
    - decodificar alguns dados baixados usando o container 'decode-bufr-jupyter'