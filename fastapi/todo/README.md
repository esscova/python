# To-do List
Este é mais um exemplo básico para demonstrar as funcionalidades CRUD usando o FastAPI. Na prática, você provavelmente usaria um banco de dados para persistir os dados e adicionaria mais funcionalidades e validações à sua API.

## Endpoints da API

- **POST /tasks/**: Cria uma nova tarefa.
- **GET /tasks/**: Retorna todas as tarefas.
- **GET /tasks/{task_id}**: Retorna uma tarefa específica pelo seu ID.
- **PUT /tasks/{task_id}**: Atualiza uma tarefa existente pelo seu ID.
- **DELETE /tasks/{task_id}**: Deleta uma tarefa pelo seu ID.

## Como executar

Inicie o servidor:
```bash
uvicorn main:app --reload
```
Isso iniciará o servidor na URL `http://127.0.0.1:8000`.

## Testando a API

Você pode testar as rotas usando ferramentas como o Postman, curl ou até mesmo o próprio navegador. Aqui estão alguns exemplos de como usar as rotas:

- Criar uma tarefa:
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"id": 1, "title": "Tarefa 1", "description": "Descrição da tarefa 1"}' http://127.0.0.1:8000/tasks/
  ```

- Listar todas as tarefas:
  ```bash
  curl http://127.0.0.1:8000/tasks/
  ```

- Obter uma tarefa específica:
  ```bash
  curl http://127.0.0.1:8000/tasks/1
  ```

- Atualizar uma tarefa:
  ```bash
  curl -X PUT -H "Content-Type: application/json" -d '{"id": 1, "title": "Tarefa atualizada", "description": "Nova descrição da tarefa"}' http://127.0.0.1:8000/tasks/1
  ```

- Deletar uma tarefa:
  ```bash
  curl -X DELETE http://127.0.0.1:8000/tasks/1
  ```

**Ou acesse a documentação interativa da API em:** `http://127.0.0.1:8000/docs`