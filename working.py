from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"data": "testing"}



@app.get("/about")
def home():
    return {"data": "about"}