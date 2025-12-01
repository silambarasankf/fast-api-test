from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/items")
def create_item(item: Item):
    return {"message": "Item created", "item": item}
