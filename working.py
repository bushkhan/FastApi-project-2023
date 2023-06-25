from fastapi import FastAPI, Path

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

@app.get("/get-item/{item_id}") #path-parameters
def get_item(item_id: int =  Path( description="An id of the item you'd like to view.")):
    return inventory[item_id]

#example - http://127.0.0.1:8000/get-item/1



    