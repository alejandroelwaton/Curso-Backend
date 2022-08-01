#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#Fast api
from fastapi import FastAPI
from fastapi import Body
from fastapi import Query

#Program
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

#Request and Response Body
@app.post('/item/new')
def new_item(item: Item = Body(...)):
    return item

#Validation Query Params
@app.get('/item/detail')
def show_item(
    name: Optional[str] = Query(None, min_length=2, max_length=30),
    price: Optional[float] = Query(0.00)
) -> Item:
    return {'name': name, 'price': price}