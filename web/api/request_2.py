from fastapi import Body, FastAPI
from pydantic import BaseModel, Schema


app = FastAPI()


class Item(BaseModel):
    name: str 
    description: str = Schema(None, title = "a description of this item",max_length = 500,regex = r"^\d{3}-\d{3,8}$")
    price: float = Schema(...,gt = 0, description = "the price must surpass 0")
    tax: float = None


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = 23423,
    item: Item = Body(..., example = {"name" : "foo","description" : "A good item.", "price" : 29.34}, embed = True)
):
    results = {"item_id" : item_id, "item" : item}
    return results 