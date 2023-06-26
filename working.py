from fastapi import FastAPI, Path
from typing import Optional
app = FastAPI()


# @app.get("/")
# def home():
#     return {"data": "testing"}



# @app.get("/about")
# def home():
#     return {"data": "testing"}


inventory = {
    1:{
        "name": "Cheese",
        "price": 3.45,
        "brand": "Amul"
    }
}



#path-parameters
@app.get("/get-item/{item_id}") 
def get_item(item_id: int =  Path( description="An id of the item you'd like to view.")):
    return inventory[item_id]

#example - http://127.0.0.1:8000/get-item/1



#query-parameters
@app.get("/get-by-name")
def get_item(name: Optional[str] = None):
    for item_id in inventory:
        if inventory[item_id]['name'] == name:
            return inventory[item_id]
    return {"Data": "Not found"}

#example - http://127.0.0.1:8000/get-by-name?name=Cheese


#path param iwth query param
@app.get("/get-by-name/{item_id}")
def get_item(item_id: int, name: Optional[str] = None):
    for item_id in inventory:
        if inventory[item_id]['name'] == name:
            return inventory[item_id]
    return {"Data": "Not found"}

#example - http://127.0.0.1:8000/get-by-name/1?name=Cheese
