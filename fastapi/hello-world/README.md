# Projeto FastAPI Simples

Este é um projeto FastAPI simples que retorna uma mensagem "hello world" quando a rota raiz (`/`) é acessada.

## Execução
1. Inicie o servidor:
```
uvicorn main:app --reload
```
2. Acesse a aplicação em `http://localhost:8000/`

## Endpoints
- `GET /`: Retorna a mensagem "hello world"