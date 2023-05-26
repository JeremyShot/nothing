from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

class Item(BaseModel):
    user_name:str
    user_id:str
    tax:float = None


class Roieee_class_name(str,Enum):
    name = 'Child Prodigy'
    age = 18
    id = '234jv24o562345'
    gender = 'gunship'

app = FastAPI()

@app.get("/index/login/{user_man}")
async def print_name(user_man:Roieee_class_name):
    return {"status": "your gender: "+user_man.gender}

@app.get("/index/file/{file_path:path}")
async def print_file_path(file_path:str):
    return file_path

@app.post("/index/items/")
async def create_item(item:Item):
    return item
