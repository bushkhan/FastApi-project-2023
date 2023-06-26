from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel



app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None
    
    
# @app.get("/")
# def home():
#     return {"data": "testing"}



# @app.get("/about")
# def home():
#     return {"data": "testing"}


inventory = {}

#path-parameters
@app.get("/get-item/{item_id}") 
def get_item(item_id: int =  Path(description="An id of the item you'd like to view.")):
    if item_id not in inventory:
        return {"Error": "Item does not exists!"}
    return inventory[item_id]

#example - http://127.0.0.1:8000/get-item/1


#query-parameters
@app.get("/get-by-name")
def get_item(name: str = Query(description="name of the item")):
    for item_id in inventory:
        print("id is",item_id)
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"Data": "Not found"}

#example - http://127.0.0.1:8000/get-by-name?name=Cheese


@app.post('/create-item/{item_id}')
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item already exists!"}

    inventory[item_id] = item
    return inventory[item_id]


@app.put('/update-item/{item_id}')
def update_item(item_id: int, item: UpdateItem):
    if item_id not  in inventory:
        return {"Error": "Item does not exist!"}

    if item.name != None:
        inventory[item_id].name = item.name
    if item.price != None:
        inventory[item_id].price = item.price
    if item.brand != None:
        inventory[item_id].brand = item.brand
        
        
    return inventory[item_id]



@app.delete('/delete-item')
def create_item(item_id: int = Query(description= "id of an ite to delete!")):
    if item_id not in inventory:
        return {"Error": "Item does not exists!"}
    
    del inventory[item_id]
    return {"Success": "Item deleted successfully!"}