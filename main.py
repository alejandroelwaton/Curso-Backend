#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#Fast api
from fastapi import FastAPI
from fastapi import Body

app = FastAPI()

#Models

class Item(BaseModel):
    name: str
    price: float
    description: str
    time_in_stock: int
    in_existence: Optional[bool] = False

whatever = 'Random Value'

@app.get('/')
def home():
    return {'message': whatever}


@app.post('/item/new')
def new_item(item: Item = Body(...)):
    return item
