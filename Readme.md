# Ambiente

## Dependências

- Ambiente Linux ou Windows (WSL2)
- Python 3.8+ (instalado no Linux ou WSL2)

## Como executar o projeto

Para instalar o sistema, é necessário seguir alguns passos, como baixar o projeto e realizar algumas instalações. Para isso, é necessário abrir uma aba do terminal e digitar o seguinte código.

### Esse passo é baixar o projeto

### Entrar na pasta

cd

### Criar um ambiente virtual

python3 -m venv venv

### Entrar no ambiente virtual

source venv/bin/activate

### Instalar as depedências e migrações:

pip install -r requirements.txt

Depois de ter instalado as dependências, é necessário rodar as migrations para que o banco de dados e as tabelas sejam criadas:

./manage.py migrate

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
