# Acordb

O Acordb é uma aplicação web para gestão de acórdãos (decisões judiciais) de varios tribunais nacionais. Esta aplicação dá um interface amigavel ao utilizador que permite gerir,pesquisar,analisar dados de um acordão. O sistema foi construido usando uma REST Api em Django e Svelt kit para frontent.

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

Antes de correr o acordb verifique que tem as seguintes aplicações instaladas:

- Docker
- Docker Compose

Tambem é necessario ter criado uma aplicação de autenticação com google para poder usar login com google no acordb.
# Instalação

1. Clone o repositorio:
git clone https://github.com/gweebg/acordb.git
cd acordb

2. Contruir e começar os containers Docker:

docker-compose up --build

Este comando ira contruir as imagens Docker necessarias e começar as bases de dados (MongoDB e PostgreSQL) assim como a frontend e o backend


3. A aplicação web esta disponivel no browser em `http://localhost/`.

## Como utilizar

- A REST Api (Django) está acessivel em `http://localhost:8000`.
- A aplicação Web (Svelt Kit) está acessivel em `http://localhost:80`.
- A base de dados não relacional (MongoDB) é acessivel por `mongodb://localhost:27017`.
- A base de dados relacional (PostgreSQL) é acessivel por `postgresql://localhost:5432`.


## Configuração

O Acordb dispõe de varias opções de configuração. As principais configurações incluem:

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

## Seeding da base de dados

Para colocar automaticamente os dados nas bases de dados foi gerado um comando de gestão Django para dar seed de um ficheiro,ou varios (caso um caminho para uma pasta lhe seja fornecido) , chamado seed.

Para usar basta executar dentro do container da backend: python3 manage.py seed `PATH`
Em que PATH representa o caminho para o ficheiro ou pasta dentro do container Docker.

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
