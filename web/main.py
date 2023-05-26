from fastapi import FastAPI

app = FastAPI()

@app.get("/index/{user_name}")
async def print_name(user_name):
    return {"message":"Hello  there."+user_name}