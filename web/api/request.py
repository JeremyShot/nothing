from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, schema
from enum import Enum
import re


app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float = None
    tax: float = None

class User(BaseModel):
    user_name: str = "Jeremy"
    user_age: int
    user_gender: str = "gunship"

@app.get("/index")
async def read_items(
    q :str = Query(
    None,
    min_lentg = 5, 
    max_lenth = 50,
    regex = r"^\d{3}-\d{3,8}$"    )
):
    results = {
        "items": "Big project"
    }
    if q :
        results.update({"q":q}) 

    return results 

@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(..., title = "The ID of the item to fetch",ge = 0, le = 1000),
    q: str = None,
    item: Item = Body(None,embed = True),
    user: User = None,
    importance: int = Body(None)
    ):
    
    results = {"item_id" : item_id}
    if q:
        results.update({"q" : q})
    if item:
        results.update({"item" : item})
    if user:
        results.update({"user" : user})    
    if importance:
        results.update({"importance" : importance})
    return results    