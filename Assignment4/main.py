from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_root(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/")
async def post():
    return {"message": "hello from the post route"}


@app.put(f"/")
async def put():
    return {"message": "hello from the put route"}
