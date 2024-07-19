# Dependencies
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Models
class User(BaseModel):
	id:int
	name: str
	email:str

class UserUpdated(BaseModel):
	name:Optional[str] = None
	email:Optional[str] = None


# mock db
users_db:List[User] = [
	User(id=1, name='João', email='joao@email.com'),
	User(id=2, name='Maria', email='maria@email.com'),
	User(id=3, name='José', email='jose@email.com'),
]

next_id = len(users_db)+1 # contador para ids

# Routes

## GET
### rota raiz
@app.get('/', status_code=200) 
def root ():
	return JSONResponse(status_code=200, content={'message':'Bem vindos a nossa API'})

### listagem de usuarios
@app.get('/users', response_model=List[User])
async def read_users():
	return users_db

### usuario especifico
@app.get('/users/{user_id}', response_model=User)
async def read_user(user_id:int):
	for user in users_db:
		if user.id == user_id:
			return user
	
	raise HTTPException(status_code=404, detail='Usuário não encontrado')

### POST
@app.post('/users', response_model=User)
async def create_user (user:User):
	global next_id
	
	for u in users_db:
		if u.email == user.email:
			raise HTTPException(status_code=400, detail="Email já cadastrado")
	
	user.id = next_id
	# print(user.id)
	next_id += 1
	# print(next_id)
	users_db.append(user)
	return user

### PUT
@app.put('/users/{user_id}', response_model=User)
async def update_user(user_id:int, user_update:UserUpdated):
	for i, u in enumerate(users_db):
		
		if u.id == user_id:
			if user_update.name is not None:
				users_db[i].name = user_update.name
			
			if user_update.email is not None:
				users_db[i].email = user_update.email

			return users_db[i]

	raise HTTPException(status_code=404, detail='Usuário não encontrado')

### DELETE
@app.delete('/users/{user_id}', status_code=200)
async def delete_user(user_id:int):
	for i, u in enumerate(users_db):
		if u.id == user_id:
			del users_db[i]
			return JSONResponse(status_code=200, content={'message':'Usuário deletado com sucesso'})
	
	raise HTTPException(status_code=404, detail='Usuário não encontrado')
