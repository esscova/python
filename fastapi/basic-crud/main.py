from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

items:Dict[int,'Item'] = {}

class Item(BaseModel):
    name: str
    price: float

@app.get("/")
def root():
    return {"message": "Bem vindo a nossa API"}

@app.get('/items')
def read_items():
    return items

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return items.get(item_id)

@app.post("/items/")
def create_item(item: Item):
    item_id = len(items) + 1
    items[item_id] = item
    return item

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    items[item_id] = item
    return item

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return items.pop(item_id, None)