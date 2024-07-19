# User Management API

Este é um exemplo básico de API para gerenciar usuários, demonstrando funcionalidades CRUD usando o FastAPI. Na prática, você provavelmente usaria um banco de dados para persistir os dados e adicionaria mais funcionalidades e validações à sua API.

## Endpoints da API

- **POST /users/**: Cria um novo usuário.
- **GET /users/**: Retorna todos os usuários.
- **GET /users/{user_id}**: Retorna um usuário específico pelo seu ID.
- **PUT /users/{user_id}**: Atualiza um usuário existente pelo seu ID.
- **DELETE /users/{user_id}**: Deleta um usuário pelo seu ID.

## Como executar

Inicie o servidor:
```bash
uvicorn main:app --reload
```
Isso iniciará o servidor na URL `http://127.0.0.1:8000`.

## Testando a API

Você pode testar as rotas usando ferramentas como o Postman, curl ou até mesmo o próprio navegador. Aqui estão alguns exemplos de como usar as rotas:

- Criar um usuário:
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"name": "Novo Usuário", "email": "novo.usuario@example.com"}' http://127.0.0.1:8000/users/
  ```

- Listar todos os usuários:
  ```bash
  curl http://127.0.0.1:8000/users/
  ```

- Obter um usuário específico:
  ```bash
  curl http://127.0.0.1:8000/users/1
  ```

- Atualizar um usuário:
  ```bash
  curl -X PUT -H "Content-Type: application/json" -d '{"name": "Usuário Atualizado", "email": "atualizado.usuario@example.com"}' http://127.0.0.1:8000/users/1
  ```

- Deletar um usuário:
  ```bash
  curl -X DELETE http://127.0.0.1:8000/users/1
  ```

**Ou acesse a documentação interativa da API em:** `http://127.0.0.1:8000/docs`
<!-- 
## Estrutura do Código

### Dependências
```python
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional
```

### Modelos
```python
class User(BaseModel):
    id: int
    name: str
    email: str

class UserUpdated(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
```

### Banco de Dados Simulado
```python
users_db: List[User] = [
    User(id=1, name='João', email='joao@email.com'),
    User(id=2, name='Maria', email='maria@email.com'),
    User(id=3, name='José', email='jose@email.com'),
]

next_id = len(users_db) + 1
```

### Rotas

#### GET
```python
@app.get('/', status_code=200)
def root():
    return JSONResponse(status_code=200, content={'message': 'Bem vindos a nossa API'})

@app.get('/users', response_model=List[User])
async def read_users():
    return users_db

@app.get('/users/{user_id}', response_model=User)
async def read_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail='Usuário não encontrado')
```

#### POST
```python
@app.post('/users', response_model=User)
async def create_user(user: User):
    global next_id
    for u in users_db:
        if u.email == user.email:
            raise HTTPException(status_code=400, detail="Email já cadastrado")
    
    user.id = next_id
    next_id += 1
    users_db.append(user)
    return user
```

#### PUT
```python
@app.put('/users/{user_id}', response_model=User)
async def update_user(user_id: int, user_update: UserUpdated):
    for i, u in enumerate(users_db):
        if u.id == user_id:
            if user_update.name is not None:
                users_db[i].name = user_update.name
            if user_update.email is not None:
                users_db[i].email = user_update.email
            return users_db[i]
    raise HTTPException(status_code=404, detail='Usuário não encontrado')
```

#### DELETE
```python
@app.delete('/users/{user_id}', status_code=200)
async def delete_user(user_id: int):
    for i, u in enumerate(users_db):
        if u.id == user_id:
            del users_db[i]
            return JSONResponse(status_code=200, content={'message': 'Usuário deletado com sucesso'})
    raise HTTPException(status_code=404, detail='Usuário não encontrado')
``` -->
---
