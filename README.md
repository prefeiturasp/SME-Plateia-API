# Plateia API

Este projeto implementa uma API RESTful que tem como objetivo fornecer acesso a informações e funcionalidades relacionadas aos eventos da plataforma Plateia, disponibilizando recursos para a construção do aplicativo mobile.

## Tecnologias Utilizadas

- Python 3.11
- Django 4.1
- Django REST framework 3.14

## Instalação

1. Clone este repositório para sua máquina local.
2. Crie um ambiente virtual para isolar as dependências do projeto.
3. Ative o ambiente virtual.
4. Instale as dependências do projeto com o comando `pip install -r requirements.txt`.

## Rotas

### Autenticação

- `api/v1/autenticacao/entrar`: autenticação JWT
- `api/v1/autenticacao/token/atualizar/`: atualização do token JWT

### Eventos

- `api/v1/locais_meus_eventos`: lista de locais dos eventos do usuário para ser utilizado no autocomplete
- `api/v1/meus_eventos/<int:pk>/`: busca de um evento do usuário por id
- `api/v1/meus_eventos`: busca da lista de todos os eventos do usuário, com possibilidade de filtro por local, período e nome do evento.

### Ingressos

- `api/v1/inscricao/<int:pk>/voucher`: retorna o QR code da inscrição e o PDF do ingresso.

## Testes

Este projeto conta com testes unitários implementados nos apps `user`, `inscription` e `event`. Vale ressaltar que as tabelas do banco de dados são todas definidas como `managed=False`, pois o projeto apenas acessa os dados já existentes e não tem a responsabilidade de gerenciar o esquema do banco de dados.

## Documentação

A documentação completa da API pode ser acessada através da rota `api/v1/schema/swagger-ui/#/`, onde é possível encontrar informações detalhadas sobre cada rota e seus respectivos parâmetros.

Caso precise de uma visão geral das funcionalidades da API, este README oferece um resumo das principais rotas e recursos disponíveis.
