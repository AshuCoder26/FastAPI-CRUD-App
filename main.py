from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() #creating app

db = []

# @app.get("/{name}")
# def root(name: str):
#     return{"Greetings":"Welcome to Enterprise64" + name}

class items(BaseModel):
    name: str
    description: str

@app.post("/")
def create (item: items):
    db[item.name] = item.description
    return {"item": item}

              
@app.get("/")
def get_all_data():
    return   db 

@app.delete("/")
def delete_data(name: str):
    del db[name]
    return db


         


