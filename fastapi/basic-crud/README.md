# Basic CRUD 

Este projeto demonstra a criação de uma API básica utilizando o FastAPI. A API fornece operações CRUD (Create, Read, Update, Delete) para manipulação de itens.

## Explicação 

O **Pydantic** é uma biblioteca de validação de dados e gerenciamento de configurações usando a notação de type hints do Python. Ele é utilizado no FastAPI para garantir que os dados que entram e saem da nossa API sejam válidos e estejam no formato correto.


O módulo **typing** fornece suporte para dicas de tipos (type hints) que ajudam a melhorar a legibilidade e a robustez do código.

A variável `items` é um dicionário que simula um banco de dados na memória. Ele armazena itens onde a chave é um ID do tipo inteiro e o valor é um objeto do tipo `Item`.


## Como executar
1. Inicie o servidor:
```
uvicorn main:app --reload
```
2. Acesse a aplicação em `http://localhost:8000/`

3. Acesse a documentação interativa da API em `http://127.0.0.1:8000/docs`

### Endpoints da API

- **GET /**: Retorna uma mensagem de boas-vindas.
- **GET /items**: Retorna todos os itens cadastrados.
- **GET /items/{item_id}**: Retorna um item específico pelo seu ID.
- **POST /items/**: Cria um novo item.
- **PUT /items/{item_id}**: Atualiza um item existente pelo seu ID.
- **DELETE /items/{item_id}**: Deleta um item pelo seu ID.

