# AcorDB

Neste projeto foi criada uma plataforma (AcorDB) com o intuito de auxiliar o Ministério da
Justiça portuguêsa e advogados na disponiblização e procura de acordãos.
Cada tribunal, com autonomia própria, disponibiliza periodicamente um conjunto de acordãos
que se tornam públicos. Desta forma, cada tribunal tem a sua própria base de dados, resultando
num conjunto distinto de 14 base de dados.
Para ser possível realizar o carregamento de todos os dados fornecidos foram realizados scripts
em Python para o processamento, parsing, manipulação e normalização dos dados. Para o servidor
da base de dados foi utilizado inicialmente Mongo atlas e sqlite e, numa fase posterior, optou-se
por MongoDB e Postgres hosteado localmente devido a limites de velocidade impostos por serviços de hosting.
Para a comunicação entre a base de dados e a interface web, foi necessário criar uma API e para
isso foi utilizado Django.
Foi ainda criada um interface web dinâmica que tem ao dispor toda a informação existente, havendo diversas possibilidades de pesquisa como pesquisa por campos,descritores ou intervalos de datas.
Nesta plataforma, existem dois tipos de utilizadores. Os administradores, com as permissões
mais elevadas, têm acesso a todas as operações. Os consumidores apenas podem consultar os dados
disponibilizados, guardar favoritos e suguerir alterações. No entanto, só os administradores  ́e que
podem aceitar e realizar as alterações sugeridas. O sistema está protegido com autenticação, podendo
esta ser feita através de username+password, chaveAPI ou Google.
Neste relatório, são explicadas as ferramentas usadas, a arquitetura implementada, o tratamento
de dados feito, a implementação de bases de dados e ainda a interface da aplicação.

## Features

- Dois niveis de utilizadores com diferentes niveis de permissões.
- Capacidade de administradores poderem criar novos acordãos.
- Pesquisa avançada sobre os dados de um acordão.
- Possibilidade de guardar favoritos. 
- Login através de password,conta Google ou API Key para acesso a api de dados
- Interface reativa e intuitiva
- Histórico das modificações feitas a um acordão
- Possibilidade de adicionar novos utilizadores

## Prerequesitos

Antes de correr o AcorDB verifique que tem as seguintes aplicações instaladas:

- Docker
- Docker Compose

Tambem é necessario ter criado uma aplicação de autenticação com google para poder usar login com google no AcorDB.
# Instalação

1. Clone o repositorio:
git clone https://github.com/gweebg/acordb.git
cd acordb

2. Contruir e começar os containers Docker:

docker-compose up --build

Este comando ira contruir as imagens Docker necessarias e começar as bases de dados (MongoDB e PostgreSQL) assim como a frontend e o backend


3. A aplicação web esta disponivel no browser em `http://localhost/`.

## Partes da aplicação

- A REST Api (Django) está acessivel em `http://localhost:8000`.
- A aplicação Web (Svelt Kit) está acessivel em `http://localhost:80`.
- A base de dados não relacional (MongoDB) é acessivel por `mongodb://localhost:27017`.
- A base de dados relacional (PostgreSQL) é acessivel por `postgresql://localhost:5432`.


## Configuração

O AcorDB dispõe de varias opções de configuração. As principais configurações incluem:

- `settings.py`: Configura algumas defenições da backend assim como ficherios estaticos e tipos de base de dados a serem usadas.
- `docker-compose.yml`: Define os serviços,redes,volumes de dados dos containers Docker.
- `.env`: Guarda variveis de ambiente usadas dentro do `settings.py` para guardar chaves e credenciais.

## Normalização dos datasets

Dado que eram fornecidos 14 datasets diferentes, com o objetivo de reduzir o numero de chaves foi feita uma normalização deste datasets. Visto que havia varios descritores com o mesmo significado ou um descritor com a informação de varios estes foram tambem normalizados.

Para isto criaram-se os Scripts `keysByFile.py` e `typesToTable` que permitiram analizar as chaves existentes e ajudaram a juntar varios campos em um chamado apêndice.

Como normalizar os datasets:
1. Colocar na pasta `norm/acordãos_in` os ficheros do dataset
2. cd norm
3. python3 normalizers/run.py
4. Os datasets normalizados estaram disponiveis na pasta `norm/acordãos_out`

Na normalização de descritores é feita uma lista de todos os descritores existentes comparando os novos ao já existentes e caso sejam iguais exeto ter `.` no fim são considerados o mesmo sendo guardado o que já existia.Para além disso é verificada a existencia de separações dentro de um descritor criando assim 2 descritores separadoss.

Na normalização de datasets a principal operação é a de adicionar valores a apêndice sendo este o caso quando a chave de um valor se encontra usado no texto integral e/ou sumário (exeto situações em que é um campo existente em todos os registos),outros casos de agrupamentos são areaTematica,jurisprudências,normas,legislações e referências que foram juntadas numa só chave.

## Seeding da base de dados

Para colocar automaticamente os dados nas bases de dados foi gerado um comando de gestão Django para dar seed de um ficheiro,ou varios (caso um caminho para uma pasta lhe seja fornecido) , chamado seed.

Para usar basta executar dentro do container da backend: python3 manage.py seed `PATH`
Em que PATH representa o caminho para o ficheiro ou pasta dentro do container Docker.

Os datasets já normalizados estão disponiveis em [OneDrive](https://uminho365-my.sharepoint.com/:f:/g/personal/a96681_uminho_pt/EnGrLHYMyEBOufUKmbFotNoBm32uLj23-LHS6pYDQO7UnQ?e=j1aXA5)

## Arquitetura

A aplicação está divida em 4 partes distintas.
1. Frontend
Este foi desenvolvido em Svelt Kit e comunica diretamente com a backend para gestão de dados.Sendo esta responsavel por mostrar ao utilizador os dados dos acordãos, e a possibilidade de fazer gestão destes.
2. Backend
Este foi desenvolvido em Django e providencia uma REST Api com a qual o frontend comunica. Para alem disso comunica com ambas as bases de dados para implementar a logica da aplicação.
3. Base de dados não relacional
Esta foi feita em MongoDB e é utilizada para guardar dados sobre os quais não se tem a certeza quais os seus campos nem o tamanho/tipo dos seus valores. Neste caso foi usado para guardar os dados das varias versoes de um acordão
4. Base de dados realcional.
Esta fou feita em PostgreSQL devido a sua velocidade. Esta é usada para guardar todos os dados do utilizador,favoritos,apiKeys e alguns dados sobre os acordãos.

A escolha de ter duas bases de dados veio da incompatibilidade base de django com MongoDB, no entanto, devido a velocidade de PostgreSQL esta decisão acabou por se tornar bastante boa mantendo um nivel simples de controlo atras de django e criar uma solução expecifica para o nosso caso na comunicação com MongoDB.


## Backend
Visto que parte do grupo já tinha bastante experiencia com a framework `Django` e esta tem bastantes extensões, que nos foram úteis, o grupo decidiu usá-la.

Um problema que encontramos com a nossa escolha de framework foi a falta de interação com bases de dados não relacionais como \textit{MongoDB}.Visto que desde início a intenção era os acórdãos poderem ser o mais genéricos possível é necessário que qualquer chave seja aceite, não fazendo sentido usar uma base de dados relacional. Daqui surgiu a ideia de ter duas bases de dados. Para resolver o problema apresentado criaram-se várias funções que tomam uso de \textit{PyMongo} para comunicarem com uma base de dados onde todos os dados dos acórdãos e alteração de dados é guardado.