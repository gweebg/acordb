# Acordb

Através da realização deste projeto foi criada a plataforma **Acordb** com o intuído de auxiliar qualquer tipo de pessoa ou organização a procurar, guardar ou editar acórdãos.
Dado a que cada tribunal, com autonomia própria, disponibiliza periodicamente um conjunto de acórdãos públicos, a aplicação, por defeito, possui aproximadamente 340.000 acórdãos espalhados por 14 tribunais diferentes. Tais registos podem ser pesquisados a qualquer nível de detalhe, guardados nos favoritos ou até alterados através de pedidos de sugestão.

Ao longo do projeto, foram utilizadas diferentes *stacks* de tecnologias. De um modo geral, o *backend* foi desenvolvido em Python (Django), devivo à facilidade de processamento, parsing, manipulação e normalização de dados. E no *frontend* Sveltekit (Svelte + JavaScript) devido à sua grande abstração de tarefas que noutras ***********frameworks*********** seriam, no mínimo, cansativas. 

Relativamente às bases de dados, o conteúdo dos acórdãos é maioritariamente guardado em MongoDB enquanto que os meta-dados relativos a acórdãos e dados de utilizadores são guardados em Postgres. Devido aos limites de velocidade impostos por serviços de *******hosting,*******  todas as bases de dados são alojadas localmente num ****************docker container**************** (assim como todo o projeto).

Nesta aplicação, existem três tipos de acesso. Utilizadores sem conta apenas conseguem consultar e pesquisar acórdãos, consumidores (utilizadores com conta) têm as mesmas vantagens que os anteriores, porém também conseguem sugerir alterações aos acórdãos e adicioná-los aos favoritos. Finalmente, os administradores conseguem realizar qualquer funcionalidade anteriormente descrita, e também aceitar sugestões realizadas. 

No presente relatório, são explicadas as ferramentas e tecnologias usadas, a arquitetura implementada, o tratamento de dados feito, a implementação de bases de dados e ainda a interface da aplicação.

## Pré-requisitos e Manual de Utilização

A plataforma depende de vários serviços, pelo que é necessário ter instaladas as aplicações :

- Docker
- Docker-Compose
- Python 3.10 (Apenas utilizado para normalização de dados, opcional)

**********Nota:********** Caso pretenda utilizar autenticação através do Google, é necessária a criação de uma aplicação no [Google](https://developers.google.com/identity/sign-in/web/sign-in).

Para iniciar a aplicação temos de executar:

```bash
git clone https://github.com/gweebg/acordb
cd acordb
docker-compose up --build
```

Após isto, temos garantidamente a API de dados a ser executada em [localhost:8000](http://localhost:8000) e a interface em [localhost:80/home](http://localhost/home), ambas prontas a ser utilizadas.

Relativamente às bases de dados, estas podem ser acedidas através `mongodb://localhost:27017`(MongoDB) e `postgresql://localhost:5432` (Postgres).

### Configuração

O **Acordb** dispõe de varias opções de configuração. As principais configurações incluem:

- `settings.py`: Configura algumas definições da *backend* assim como ficheiros estáticos e tipos de base de dados a serem usadas.
- `docker-compose.yml`: Define os serviços, redes, volumes de dados dos containers Docker.
- `.env`: Guarda variáveis de ambiente usadas dentro do `settings.py` para guardar chaves e credenciais.

## Funcionalidades Implementadas

### Níveis de Acesso e Utilizadores

- Três níveis de acesso (utilizadores sem conta, utilizadores com conta (consumidores) e administradores) com diferentes níveis de permissões.
- Utilizadores sem conta conseguem apenas consultar/pesquisar acórdãos.
- Consumidores conseguem consultar/pesquisar, sugerir alterações e guardar acórdãos nos favoritos.
- Administradores conseguem consultar/pesquisar, sugerir alterações, guardar acórdãos nos favoritos, aprovar pedir de alterações e criar através de formulário ou ******upload****** de ficheiro acórdãos. Para além disso, os administradores podem tornar outros utilizadores em administradores.
- Todos os utilizadores com conta registada têm a liberdade de alterar o seu nome (primeiro nome, segundo nome) e/ou ********password********.

### Autenticação, Autorização

- Autenticação através de ******email****** e *********password.*********
- Autorização através de API ***Key***.
- Autenticação através da conta Google.
- Criação de contas através da conta Google ou formulário.

### Acórdãos

- Capacidade de criação e/ou adição de novos acórdãos.
- Pesquisa avançada sobre os dados de um acórdão.
- Possibilidade de guardar acórdãos nos favoritos.
- Possibilidade de sugerir alterações a acórdãos.
- Capacidade de verificar o histórico de modificações realizadas a um acórdão.

### Interface

- Interface reativa, intuitiva, consistente e minimalista.

# Arquitetura da Aplicação

A aplicação está divida em quatro partes distintas.

1. ***Frontend (Interface)***
Desenvolvido em [SvelteKit](https://kit.svelte.dev/), comunica diretamente com o *backend* para gestão de dados. É  responsável por mostrar ao utilizador os dados dos acórdãos, e a possibilidade de gestão dos mesmos.
2. ***Backend***
Desenvolvido em Django, providencia uma ****Restfull**** API com a qual o *frontend* comunica. Para além disso comunica com ambas as bases de dados para implementar a lógica da aplicação.
3. ***Base de Dados Não Relacional (MongoDB)***
Desenvolvida em MongoDB, é utilizada para guardar dados sobre os quais não se tem a certeza quais os seus campos nem o tamanho/tipo dos seus valores. Neste caso foi usado para guardar os dados das várias versões de um acórdão.
4. **Base de dados relacional (PostgresSQL)**
Esta foi feita em PostgreSQL devido a sua velocidade. É usada para guardar todos os dados relativos aos utilizadores, favoritos, chaves de API e meta-data sobre os acórdãos (quem adicionou, quando adicionou, etc.).

A escolha de ter duas bases de dados veio da incompatibilidade base de Django com MongoDB, no entanto, devido a velocidade de PostgreSQL esta decisão acabou por se tornar bastante boa mantendo um nível simples de controlo e permitindo uma solução especifica para o problema na comunicação com MongoDB.

Na seguinte figura, podemos observar um diagrama que representa a arquitetura geral do sistema:

![image.png](https://github.com/gweebg/acordb/blob/main/docs/arq.svg)

# Desenvolvimento do *******Backend*******

### Normalização dos ****datasets****

Dado que eram fornecidos 14 *datasets* diferentes, com o objetivo de reduzir o número de chaves foi feita uma normalização deste *datasets*. Visto que havia vários descritores com o mesmo significado ou um descritor com a informação de vários estes foram também normalizados.

Para isto criaram-se os *scripts* `keysByFile.py` e `typesToTable`.py que permitem analisar as chaves existentes e ajudar a juntar vários campos em um chamado apêndice.

Como normalizar os datasets:

```bash
mv {local_com_os_acórdãos} norm/acordãos_in
cd norm
python3 normalizers/run.py
```

Os datasets normalizados podem ser encontrados na pasta `norm/acordãos_out`. 

Na normalização de descritores é feita uma lista com todos os descritores existentes comparando os novos aos já existentes. Caso a única diferença seja ter `"."` no fim, os acórdãos são considerados o mesmo sendo guardado o que já existia. Para além disso é verificada a existência de separações dentro de um descritor criando assim 2 descritores separados.

Na normalização de *datasets* a principal operação é a de adicionar valores ao apêndice sendo este o caso quando a chave de um valor se encontra usado no texto integral e/ou sumário (exceto situações em que é um campo existente em todos os registos). Outros casos de agrupamentos são `areaTematica`,`jurisprudências`,`normas`,`legislações` e `referências` que foram juntadas numa só chave.

### *Seeding* da base de dados

Para colocar automaticamente os dados nas bases de dados foi gerado um comando de gestão Django para dar seed de um ou vários ficheiros (caso um caminho para uma pasta lhe seja fornecido), chamado `seed`.

Para utilizar basta executar dentro do *container* da *backend*:

```bash
python manage.py seed {pasta_com_os_datasets}
```

Os datasets já normalizados estão disponíveis no [OneDrive](https://uminho365-my.sharepoint.com/:f:/g/personal/a96681_uminho_pt/EnGrLHYMyEBOufUKmbFotNoBm32uLj23-LHS6pYDQO7UnQ?e=j1aXA5).

### *Backend*

Visto que parte do grupo já tinha bastante experiência com a *framework* `Django` e esta possui bastantes extensões, que nos foram úteis, o grupo decidiu usá-la.

Um problema que encontramos com a nossa escolha de framework foi a falta de interação com bases de dados não relacionais como MongoDB. Visto que, desde início, a intenção era a generalidade dos acórdãos, seria necessário que qualquer chave fosse aceite, não fazendo sentido usar uma base de dados relacional. Daqui surgiu a ideia de ter duas bases de dados. Para resolver o problema apresentado criaram-se várias funções que tomam uso de `PyMongo` para comunicarem com uma base de dados onde todos os dados dos acórdãos e alterações de dados são guardadas.

Esta camada dispões de várias rotas públicas e acessíveis a qualquer utilizador (desde que possua uma chave secreta), na seguinte tabela podemos observar todos as rotas (divididas por grupos) existentes juntamente com a descrição de cada.

A documentação e listagem de todas as rotas públicas e privadas está totalmente documentada e pode ser consultada:

- No `Postman`, importando o ficheiro **[Acordãos.postman_collection.json](https://github.com/gweebg/acordb/blob/main/server/Acord%C3%A3os.postman_collection.json).**
- No *****browser***** através de `Swagger Docs`, acessível por http://localhost:8000/swagger/.
- No *******browser******* através de `Redoc`, acessível por http://localhost:8000/redoc/.

# Desenvolvimento do ********Frontend********

### ********Frontend********

Para a realização do ********frontend******** foi utilizado `Svelte + JavaScript` juntamente com a *********framework********* `Sveltekit`, visto que, mais uma vez, parte do grupo já possuia experiência.  Algumas das vantagens de usar o `SvelteKit` em relação a outras *frameworks* como `React`, `Vue` e `Angular` incluem a sua simplicidade, desempenho e tamanho. `SvelteKit` foi projetado para ser leve e rápido, com um tamanho de pacote pequeno que permite carregamentos rápidos de página. Além disso, possui uma sintaxe e API mais simples do que outras *frameworks.* Finalmente, `SvelteKit` possui renderização do lado do servidor integrada e suporta geração de sites estáticos, tornando-o adequado para construir sites rápidos e amigáveis.

Esta camada é responsável por comunicar com o ****backend,**** porém, esta, também possui a sua própria API que facilita a gestão de rotas (por exemplo impedir que o utilizador volte a uma página protegida logo após o *******logout*******) e autenticação através do Google.

Como já referido previamente, podemos testar a interface em http://localhost/home que nos leva à página principal da nossa aplicação onde podemos executar qualquer pesquisa, consultar os 10 acórdãos mas recentes assim como as estatísticas gerais relativas ao serviço.
