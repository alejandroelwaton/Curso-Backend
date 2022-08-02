#Python
from doctest import master
from typing import Optional
from enum import Enum

#Pydantic
from pydantic import BaseModel
from pydantic import Field

#Fast api
from fastapi import FastAPI
from fastapi import Body
from fastapi import Query
from fastapi import Path

#Program
app = FastAPI()

#Models
class Types_of_items(Enum):
    food = 'food'
    drink = 'drink'
    materials = 'materials'
    electronics = 'electronics'
    misc = 'misc'


class Item(BaseModel):
    name: str = Field(
        ...,
        description="Name of the item",
        max_length=100,
        min_length=2,
    )
    price: float
    description: str
    type: Optional[Types_of_items] = Field(default='misc')
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
    name: Optional[str] = Query
    (
        None,
        min_length=2,
        max_length=30,
        title='Item Name',
        description= 'This is the item name'
    ),

    price: Optional[float] = Query
    (
        0.00,
        gt=0.00,
        title='Item Price',
        description= 'This is the item price'
    )

) -> Item:
    return {'name': name, 'price': price}


#Validations Path Params
@app.get("/item/detail/{item_id}")
def show_item(
    item_id: int = Path
    (...,
    gte=10, 
    lte=100
    )
) -> Item:
    return {'item_id': item_id}

#Validation Body requests
@app.put('/item/{item_id}')
def update_item(
    item_id: int = Path(
        ...,
        title= 'Item ID',
        description= 'This is the item ID',
        gte=10, 
        lte=100
    ),
    item: Item = Body(...)
):
    return item