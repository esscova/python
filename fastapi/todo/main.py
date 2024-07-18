from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI() # instancia 

tasks = [] #mock db

class Task(BaseModel): # modelo de dados
	id:int
	title:str
	description:str

## rotas CRUD

# criar
@app.post('/tasks/') 
def create_task(task:Task):
	for existing_task in tasks: # verificar id existente
		if existing_task['id'] == task.id:
			raise HTTPException(status_code=400, detail='Id já existe')
	tasks.append(task.dict())
	return task

# listar
@app.get('/tasks/')
def read_tasks():
	return tasks

# listar uma especifica
@app.get('/tasks/{task_id}')
def read_task(task_id:int):
	for task in tasks:
		if task['id'] == task_id:
			return task
	raise HTTPException(status_code=404, detail='tarefa não encontrada')

# atualizar
@app.put('/tasks/{task_id}')
def update_task(task_id:int, updated_task:Task):
	for i, task in enumerate(tasks):
		if task['id'] == task_id:
			tasks[i] = updated_task.dict()
			return updated_task

	raise HTTPException(status_code=404, detail='Tarefa não encontrada')

# deletar
@app.delete('/tasks/{task_id}')
def delete_task(task_id:int):
	for i, task in enumerate(tasks):
		if task['id'] == task_id:
			del tasks[i]
			return {'message':'Tarefa deletada'}
	
	raise HTTPException(status_code=404, detail='Tarefa não encontrada')
