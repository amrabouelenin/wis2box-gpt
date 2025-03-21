---
title: Configurando conjuntos de dados no wis2box
---

# Configurando conjuntos de dados no wis2box

!!! abstract "Resultados de aprendizado"
    Ao final desta sessão prática, você será capaz de:

    - criar um novo conjunto de dados
    - criar metadados de descoberta para um conjunto de dados
    - configurar mapeamentos de dados para um conjunto de dados
    - publicar uma notificação WIS2 com um registro WCMP2
    - atualizar e republicar seu conjunto de dados

## Introdução

O wis2box utiliza conjuntos de dados que estão associados a metadados de descoberta e mapeamentos de dados.

Metadados de descoberta são usados para criar um registro WCMP2 (Perfil de Metadados Básicos do WMO 2) que é compartilhado usando uma notificação WIS2 publicada no seu wis2box-broker.

Os mapeamentos de dados são usados para associar um plugin de dados aos seus dados de entrada, permitindo que seus dados sejam transformados antes de serem publicados usando a notificação WIS2.

Esta sessão irá guiá-lo na criação de um novo conjunto de dados, na criação de metadados de descoberta e na configuração de mapeamentos de dados. Você irá inspecionar seu conjunto de dados na wis2box-api e revisar a notificação WIS2 para seus metadados de descoberta.

## Preparação

Conecte-se ao seu broker usando o MQTT Explorer.

Em vez de usar suas credenciais internas do broker, use as credenciais públicas `everyone/everyone`:

<img alt="MQTT Explorer: Conectar ao broker" src="../../assets/img/mqtt-explorer-wis2box-broker-everyone-everyone.png" width="800">

!!! Note

    Você nunca precisa compartilhar as credenciais do seu broker interno com usuários externos. O usuário 'everyone' é um usuário público para permitir o compartilhamento de notificações WIS2.

    As credenciais `everyone/everyone` têm acesso somente leitura no tópico 'origin/a/wis2/#'. Este é o tópico onde as notificações WIS2 são publicadas. O Broker Global pode se inscrever com essas credenciais públicas para receber as notificações.
    
    O usuário 'everyone' não verá tópicos internos ou poderá publicar mensagens.
    
Abra um navegador e abra uma página para `http://<seu-host>/wis2box-webapp`. Certifique-se de que você está logado e pode acessar a página 'editor de conjuntos de dados'.

Veja a seção sobre [Inicializando o wis2box](/practical-sessions/initializing-wis2box) se você precisar lembrar como conectar ao broker ou acessar o wis2box-webapp.

## Criar um token de autorização para processes/wis2box

Você precisará de um token de autorização para o endpoint 'processes/wis2box' para publicar seu conjunto de dados.

Para criar um token de autorização, acesse sua VM de treinamento via SSH e use os seguintes comandos para fazer login no contêiner de gerenciamento do wis2box:

```bash
cd ~/wis2box-1.0.0rc1
python3 wis2box-ctl.py login
```

Em seguida, execute o seguinte comando para criar um token de autorização gerado aleatoriamente para o endpoint 'processes/wis2box':

```bash
wis2box auth add-token --path processes/wis2box
```

Você também pode criar um token com um valor específico fornecendo o token como argumento para o comando:

```bash
wis2box auth add-token --path processes/wis2box MyS3cretToken
```

Certifique-se de copiar o valor do token e armazená-lo em sua máquina local, pois você precisará dele mais tarde.

Uma vez que você tenha seu token, você pode sair do contêiner de gerenciamento do wis2box:

```bash
exit
```

## Criando um novo conjunto de dados no wis2box-webapp

Navegue até a página 'editor de conjuntos de dados' no wis2box-webapp da sua instância wis2box indo para `http://<seu-host>/wis2box-webapp` e selecionando 'editor de conjuntos de dados' no menu do lado esquerdo.

Na página 'editor de conjuntos de dados', na aba 'Conjuntos de Dados', clique em "Criar Novo ...":

<img alt="Criar Novo Conjunto de Dados" src="../../assets/img/wis2box-create-new-dataset.png" width="800">

Uma janela pop-up aparecerá, pedindo que você forneça:

- **ID do Centro**: este é o acrônimo da agência (em letras minúsculas e sem espaços), conforme especificado pelo Membro da WMO, que identifica o centro de dados responsável pela publicação dos dados.
- **Tipo de Dados**: O tipo de dados para o qual você está criando metadados. Você pode escolher entre usar um modelo predefinido ou selecionar 'outro'. Se 'outro' for selecionado, mais campos terão que ser preenchidos manualmente.

!!! Note "ID do Centro"

    Seu id de centro deve começar com o TLD do seu país, seguido por um traço (`-`) e um nome abreviado da sua organização (por exemplo, `br-inmet`). O id do centro deve ser em letras minúsculas e usar apenas caracteres alfanuméricos. A lista suspensa mostra todos os ids de centro atualmente registrados no WIS2, bem como qualquer id de centro que você já tenha criado no wis2box.

!!! Note "Modelos de Tipo de Dados"

    O campo *Tipo de Dados* permite que você selecione de uma lista de modelos disponíveis no editor de conjuntos de dados do wis2box-webapp. Um modelo irá pré-preencher o formulário com valores padrão sugeridos apropriados para o tipo de dados. Isso inclui título sugerido e palavras-chave para os metadados e plugins de dados pré-configurados. O tópico será fixado ao tópico padrão para o tipo de dados.

    Para o propósito do treinamento, usaremos o tipo de dados *weather/surface-based-observations/synop* que inclui plugins de dados que garantem que os dados sejam transformados em formato BUFR antes de serem publicados.

    Se você quiser publicar alertas CAP usando o wis2box, use o modelo *weather/advisories-warnings*. Este modelo inclui um plugin de dados que verifica se os dados de entrada são um alerta CAP válido antes da publicação. Para criar alertas CAP e publicá-los via wis2box, você pode usar o [CAP Composer](https://github.com/wmo-raf/cap-composer).

Por favor, escolha um id de centro apropriado para sua organização.

Para **Tipo de Dados**, selecione **weather/surface-based-observations/synop**:

<img alt="Formulário de Criação de Novo Conjunto de Dados: Informações Iniciais" src="../../assets/img/wis2box-create-new-dataset-form-initial.png" width="450">

Clique em *continuar para o formulário* para prosseguir, agora você será apresentado ao **Formulário do Editor de Conjuntos de Dados**.

Como você selecionou o tipo de dados **weather/surface-based-observations/synop**, o formulário será pré-preenchido com alguns valores iniciais relacionados a esse tipo de dados.

## Criando metadados de descoberta

O Formulário do Editor de Conjuntos de Dados permite que você forneça os Metadados de Descoberta para seu conjunto de dados que o contêiner de gerenciamento do wis2box usará para publicar um registro WCMP2.

Como você selecionou o tipo de dados 'weather/surface-based-observations/synop', o formulário será pré-preenchido com alguns valores padrão.

Por favor, certifique-se de substituir o 'ID Local' auto-gerado por um nome descritivo para seu conjunto de dados, por exemplo, 'conjunto-de-dados-synop-wis2treinamento':

<img alt="Editor de Metadados: título, descrição, palavras-chave" src="../../assets/img/wis2box-metadata-editor-part1.png" width="800">

Revise o título e as palavras-chave, atualize-os conforme necessário e forneça uma descrição para seu conjunto de dados.

Observe que há opções para alterar a 'Política de Dados da WMO' de 'core' para 'recomendada' ou para modificar seu Identificador de Metadados padrão, mantenha a política de dados como 'core' e use o Identificador de Metadados padrão.

Em seguida, revise a seção que define suas 'Propriedades Temporais' e 'Propriedades Espaciais'. Você pode ajustar a caixa delimitadora atualizando os campos 'Latitude Norte', 'Latitude Sul', 'Longitude Leste' e 'Longitude Oeste':

<img alt="Editor de Metadados: propriedades temporais, propriedades espaciais" src="../../assets/img/wis2box-metadata-editor-part2.png" width="800">

Em seguida, preencha a seção que define as 'Informações de Contato do Provedor de Dados':

<img alt="Editor de Metadados: informações de contato" src="../../assets/img/wis2box-metadata-editor-part3.png" width="800">

Finalmente, preencha a seção que define as 'Informações de Qualidade dos Dados':

Uma vez que você tenha preenchido todas as seções, clique em 'VALIDAR FORMULÁRIO' e verifique o formulário quanto a erros:

<img alt="Editor de Metadados: validação" src="../../assets/img/wis2box-metadata-validation-error.png" width="800">

Se houver algum erro, corrija-os e clique em 'VALIDAR FORMULÁRIO' novamente.

Certifique-se de que não há erros e que você recebe uma indicação pop-up de que seu formulário foi validado:

<img alt="Editor de Metadados: sucesso na validação" src="../../assets/img/wis2box-metadata-validation-success.png" width="800">

Em seguida, antes de enviar seu conjunto de dados, revise os mapeamentos de dados para seu conjunto de dados.

## Configurando mapeamentos de dados

Como você usou um modelo para criar seu conjunto de dados, os mapeamentos de dados foram pré-preenchidos com os plugins padrão para o tipo de dados 'weather/surface-based-observations/synop'. Plugins de dados são usados no wis2box para transformar dados antes de serem publicados usando a notificação WIS2.

<img alt="Mapeamentos de Dados: atualizar plugin" src="../../assets/img/wis2box-data-mappings.png" width="800">

Observe que você pode clicar no botão "atualizar" para alterar configurações para o plugin, como extensão de arquivo e o padrão de arquivo, você pode deixar as configurações padrão por enquanto. Em uma sessão posterior, você aprenderá mais sobre BUFR e a transformação de dados em formato BUFR.

## Enviando seu conjunto de dados

Finalmente, você pode clicar em 'enviar' para publicar seu conjunto de dados.

Você precisará fornecer o token de autorização para 'processes/wis2box' que você criou anteriormente. Se você ainda não o fez, pode criar um novo token seguindo as instruções na seção de preparação.

Verifique se você recebe a seguinte mensagem após enviar seu conjunto de dados, indicando que o conjunto de dados foi enviado com sucesso:

<img alt="Sucesso ao Enviar Conjunto de Dados" src="../../assets/img/wis2box-submit-dataset-success.png" width="400">

Após clicar em 'OK', você será redirecionado para a página inicial do Editor de Conjuntos de Dados. Agora, se você clicar na aba 'Conjunto de Dados', você deve ver seu novo conjunto de dados listado:

<img alt="Editor de Conjuntos de Dados: novo conjunto de dados" src="../../assets/img/wis2box-dataset-editor-new-dataset.png" width="800">

## Revisando a notificação WIS2 para seus metadados de descoberta

Vá para o MQTT Explorer, se você estava conectado ao broker, você deve ver uma nova notificação WIS2 publicada no tópico `origin/a/wis2/<seu-id-de-centro>/metadata`:

<img alt="MQTT Explorer: notificação WIS2" src="../../assets/img/mqtt-explorer-wis2-notification-metadata.png" width="800">

Inspecione o conteúdo da notificação WIS2 que você publicou. Você deve ver um JSON com uma estrutura correspondente ao formato da Mensagem de Notificação WIS (WNM).

!!! question

    Em que tópico é publicada a notificação WIS2?

??? success "Clique para revelar a resposta"

    A notificação WIS2 é publicada no tópico `origin/a/wis2/<seu-id-de-centro>/metadata`.

!!! question
    
    Tente encontrar o título, a descrição e as palavras-chave que você forneceu nos metadados de descoberta na notificação WIS2. Você consegue encontrá-los?

??? success "Clique para revelar a resposta"

    Observe que o título, a descrição e as palavras-chave que você forneceu nos metadados de descoberta **não** estão presentes no payload da notificação WIS2!
    
    Em vez disso, tente procurar pelo link canônico na seção "links" na notificação WIS2:

    <img alt="Notificação WIS2 para metadados, seções de links" src="../../assets/img/wis2-notification-metadata-links.png" width="800">

    A notificação WIS2 contém um link canônico para o registro WCMP2 que foi publicado. Se você copiar e colar esse link em um navegador, você baixará o registro WCMP2 e verá o título, a descrição e as palavras-chave que você forneceu.

## Conclusão

!!! success "Parabéns!"
    Nesta sessão prática, você aprendeu como:

    - criar um novo conjunto de dados
    - definir seus metadados de descoberta
    - revisar seus mapeamentos de dados
    - publicar metadados de descoberta
    - revisar a notificação WIS2 para seus metadados de descoberta