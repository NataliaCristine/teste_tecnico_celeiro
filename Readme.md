# Ambiente

## Dependências

- Ambiente Linux ou Windows (WSL2)
- Python 3.8+ (instalado no Linux ou WSL2)

## Como executar o projeto

Para instalar o sistema, é necessário seguir alguns passos, como baixar o projeto e realizar algumas instalações. Para isso, é necessário abrir uma aba do terminal e digitar o seguinte código.

### Esse passo é baixar o projeto

https://github.com/NataliaCristine/teste_tecnico_celeiro.git

### Entrar na pasta

cd teste_tecnico_celeiro

### Criar um ambiente virtual

python3 -m venv venv

### Entrar no ambiente virtual

source venv/bin/activate

### Instalar as depedências e migrações:

pip install -r requirements.txt

Depois de ter instalado as dependências, é necessário rodar as migrations para que o banco de dados e as tabelas sejam criadas:

./manage.py migrate

Para popular o banco de dados rode o comando:

python manage.py population_database

Então, para rodar, basta digitar o seguinte, no terminal:

./manage.py runserver
E o sistema estará rodando em http://127.0.0.1:8000/

## Utilização

Para utilizar deve utilizar um API Client como Insomnia.

### Exemplos de uso

### Rotas

POST api/user/

EXEMPLO
REQUEST
{
"name": "Tempestade",
"sex":"F"
}

RESPONSE STATUS -> HTTP 201 CREATED
{
"id": 1,
"name": "Tempestade",
"sex": "F"
}

GET api/user/

EXEMPLO
RESPONSE STATUS -> HTTP 200 OK
[{
"id": 1,
"name": "Tempestade",
"sex": "F"
}]

api/user/user_id/

EXEMPLO

RESPONSE STATUS -> HTTP 200 OK
[{
"id": 1,
"name": "Tempestade",
"sex": "F"
}]

PATCH api/user/user_id/

EXEMPLO:
REQUEST
{
"name": "Jean grey",

}

RESPONSE STATUS -> HTTP 200 OK
{
"id": 1,
"name": "Jean grey",
"sex": "F"
}

DELETE api/user/user_id/

EXEMPLO:

RESPONSE STATUS -> HTTP 204 NO CONTENT

POST api/localization/

EXEMPLO
REQUEST
{
"city":"nova york"
}

RESPONSE STATUS -> HTTP 201 CREATED
{
"uuid": "b59f01f3-2660-402f-b160-a5d52b7ef27f",
"city": "nova york"
}

GET api/localization/

EXEMPLO

RESPONSE STATUS -> HTTP 200 OK

[{
"uuid": "b59f01f3-2660-402f-b160-a5d52b7ef27f",
"city": "nova york"
}]

GET api/localization/localization_id/

EXEMPLO

RESPONSE STATUS -> HTTP 200 OK

{
"uuid": "b59f01f3-2660-402f-b160-a5d52b7ef27f",
"city": "nova york"
}

PATCH api/localization/localization_id/

EXEMPLO
REQUEST
{
"city":"nova york 2"
}

RESPONSE STATUS -> HTTP 200 OK

{
"uuid": "b59f01f3-2660-402f-b160-a5d52b7ef27f",
"city": "nova york 2"
}

DELETE api/localization/localization_id/

EXEMPLO

RESPONSE STATUS -> HTTP 204 NO CONTENT

POST api/measure/

EXEMPLO
REQUEST
{
"heigth": 7,
"wheight":10,
"age" : 25,
"user_id": 3
}

RESPONSE STATUS -> HTTP 201 CREATED

{
"heigth": 7,
"wheight": 10,
"age": "25"
}

GET api/measure/

EXEMPLO

RESPONSE STATUS -> HTTP 200 OK

[
{
"uuid": "053fae52-ced9-4849-bf19-5c2dcebaf095",
"heigth": 7,
"wheight": 10,
"age": "25",
"user": {
"id": 3,
"name": "Tempestade",
"sex": "F"
}
}
]

GET api/measure/measure_id/
EXEMPLO

RESPONSE STATUS -> HTTP 200 OK

{
"uuid": "053fae52-ced9-4849-bf19-5c2dcebaf095",
"heigth": 7,
"wheight": 10,
"age": "25",
"user": {
"id": 3,
"name": "Tempestade",
"sex": "F"
}
}

PATCH api/measure/measure_id/

EXEMPLO
REQUEST
{
"age" : 35
}

RESPONSE STATUS -> HTTP 200 OK

{
"uuid": "3cd89d9f-a30f-437d-9ae3-ced0a6f0b002",
"heigth": 7,
"wheight": 10,
"age": "35",
"user": {
"id": 3,
"name": "Tempestade",
"sex": "F"
}
}

DELETE api/measure/measure_id/

EXEMPLO

RESPONSE STATUS -> HTTP 204 NO CONTENT

POST api/team/

EXEMPLO
REQUEST
{
"name": "EUA",
"ndc":"EUA",
"user_id": 3
}

RESPONSE STATUS -> HTTP 201 CREATED

{
"uuid": "de24d5cb-48df-4128-b880-b00f7e777820",
"name": "EUA",
"ndc": "EUA"
}

GET api/team/

EXEMPLO

RESPONSE STATUS -> HTTP 200 OK

[
{
"uuid": "8b6c5656-cad2-4cbd-9945-dd61e56d01d8",
"name": "EUA",
"ndc": "EUA"
}
]

GET api/team/team_id/

EXEMPLO

RESPONSE STATUS -> HTTP 200 OK

{
"uuid": "8b6c5656-cad2-4cbd-9945-dd61e56d01d8",
"name": "EUA",
"ndc": "EUA"
}

PATCH api/team/team_id/

EXEMPLO
REQUEST
{
"name": "Misure",

}

RESPONSE STATUS -> HTTP 200 OK

{
"uuid": "de24d5cb-48df-4128-b880-b00f7e777820",
"name": "misure",
"ndc": "EUA"
}

DELETE api/team/team_id/

EXEMPLO

RESPONSE STATUS -> HTTP 204 NO CONTENT

POST api/game/

EXEMPLO
REQUEST
{
"name": "festival",
"year": 2022,
"season":"1000"
}

RESPONSE STATUS -> HTTP 201 CREATED

{
"uuid": "6cd37a6a-027d-4efc-9b7f-ea9504b80e5e",
"name": "festival",
"year": 2022,
"season": "1000",
"teams": []
}

GET api/game/
EXEMPLO

RESPONSE STATUS -> HTTP 200 OK

[
{
"uuid": "4b67cad3-15a5-4481-91c7-ba5bdf013623",
"name": "festival5",
"year": 2022,
"season": "1000",
"teams": [
{
"uuid": "8b6c5656-cad2-4cbd-9945-dd61e56d01d8",
"name": "misure",
"ndc": "EUA"
}
]
},
{
"uuid": "6cd37a6a-027d-4efc-9b7f-ea9504b80e5e",
"name": "festival",
"year": 2022,
"season": "1000",
"teams": []
}
]

GET api/game/game_id
EXEMPLO

RESPONSE STATUS -> HTTP 200 OK

{
"uuid": "4b67cad3-15a5-4481-91c7-ba5bdf013623",
"name": "festival5",
"year": 2022,
"season": "1000",
"teams": [
{
"uuid": "8b6c5656-cad2-4cbd-9945-dd61e56d01d8",
"name": "misure",
"ndc": "EUA"
}
]
}

PATCH api/game/game_id
EXEMPLO obs- No team_id é uma lista com os ids dos times
REQUEST
{
"name": "festival5",
"team_id":["8b6c5656-cad2-4cbd-9945-dd61e56d01d8"]
}

RESPONSE STATUS -> HTTP 200 OK

{
"uuid": "4b67cad3-15a5-4481-91c7-ba5bdf013623",
"name": "festival5",
"year": 2022,
"season": "1000",
"teams": [
{
"uuid": "8b6c5656-cad2-4cbd-9945-dd61e56d01d8",
"name": "misure",
"ndc": "EUA"
}
]
}

POST api/event/

EXEMPLO
REQUEST
{
"name": "festival evento",
"sport":"basquete",
"localization_id":"72a8ca52-eb8b-43fd-bd7e-c9402edbe739",
"game_id":"4b67cad3-15a5-4481-91c7-ba5bdf013623"
}
RESPONSE STATUS -> HTTP 201 CREATED

{
"uuid": "cc2c3e21-0231-46a4-bc90-ee8c98bad839",
"name": "festival evento",
"sport": "basquete",
"localization": {
"uuid": "72a8ca52-eb8b-43fd-bd7e-c9402edbe739",
"city": "nova york"
},
"users": [
{
"id": 1,
"name": "Jean grey xmen",
"sex": "F"
},
{
"id": 4,
"name": "Tempestade",
"sex": "F"
},
{
"id": 5,
"name": "Tempestade",
"sex": "F"
}
],
"game": {
"uuid": "4b67cad3-15a5-4481-91c7-ba5bdf013623",
"name": "festival5",
"year": 2022,
"season": "1000",
"teams": [
{
"uuid": "8b6c5656-cad2-4cbd-9945-dd61e56d01d8",
"name": "misure",
"ndc": "EUA"
}
]
}
}

GET api/event/event_id
EXEMPLO

RESPONSE STATUS -> HTTP 200 OK

[
{
"uuid": "cc2c3e21-0231-46a4-bc90-ee8c98bad839",
"name": "festival evento",
"sport": "basquete",
"localization": {
"uuid": "72a8ca52-eb8b-43fd-bd7e-c9402edbe739",
"city": "nova york"
},
"users": [
{
"id": 1,
"name": "Jean grey xmen",
"sex": "F"
},
{
"id": 4,
"name": "Tempestade",
"sex": "F"
},
{
"id": 5,
"name": "Tempestade",
"sex": "F"
}
],
"game": {
"uuid": "4b67cad3-15a5-4481-91c7-ba5bdf013623",
"name": "festival5",
"year": 2022,
"season": "1000",
"teams": [
{
"uuid": "8b6c5656-cad2-4cbd-9945-dd61e56d01d8",
"name": "misure",
"ndc": "EUA"
}
]
}
}
]

GET api/event/
EXEMPLO

RESPONSE STATUS -> HTTP 200 OK
[
{
"uuid": "cc2c3e21-0231-46a4-bc90-ee8c98bad839",
"name": "festival evento",
"sport": "basquete",
"localization": {
"uuid": "72a8ca52-eb8b-43fd-bd7e-c9402edbe739",
"city": "nova york"
},
"users": [
{
"id": 1,
"name": "Jean grey xmen",
"sex": "F"
},
{
"id": 4,
"name": "Tempestade",
"sex": "F"
},
{
"id": 5,
"name": "Tempestade",
"sex": "F"
}
],
"game": {
"uuid": "4b67cad3-15a5-4481-91c7-ba5bdf013623",
"name": "festival5",
"year": 2022,
"season": "1000",
"teams": [
{
"uuid": "8b6c5656-cad2-4cbd-9945-dd61e56d01d8",
"name": "misure",
"ndc": "EUA"
}
]
}
},
{
"uuid": "014be5ee-3812-459a-9557-aad8ddcc59df",
"name": "festival evento2",
"sport": "basquete",
"localization": {
"uuid": "72a8ca52-eb8b-43fd-bd7e-c9402edbe739",
"city": "nova york"
},
"users": [],
"game": {
"uuid": "4b67cad3-15a5-4481-91c7-ba5bdf013623",
"name": "festival5",
"year": 2022,
"season": "1000",
"teams": [
{
"uuid": "8b6c5656-cad2-4cbd-9945-dd61e56d01d8",
"name": "misure",
"ndc": "EUA"
}
]
}
}
]

PATCH api/event/event_id
EXEMPLO obs- No user_id é uma lista com os ids dos usuários
REQUEST
{
"user_id":[1,4,5]
}
{
"uuid": "cc2c3e21-0231-46a4-bc90-ee8c98bad839",
"name": "festival evento",
"sport": "basquete",
"localization": {
"uuid": "72a8ca52-eb8b-43fd-bd7e-c9402edbe739",
"city": "nova york"
},
"users": [
{
"id": 1,
"name": "Jean grey xmen",
"sex": "F"
},
{
"id": 4,
"name": "Tempestade",
"sex": "F"
},
{
"id": 5,
"name": "Tempestade",
"sex": "F"
}
],
"game": {
"uuid": "4b67cad3-15a5-4481-91c7-ba5bdf013623",
"name": "festival5",
"year": 2022,
"season": "1000",
"teams": [
{
"uuid": "8b6c5656-cad2-4cbd-9945-dd61e56d01d8",
"name": "misure",
"ndc": "EUA"
}
]
}
}
