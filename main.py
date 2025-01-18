from typing import Union 
from models import  book
from fastapi import FastAPI, HTTPexception
from CRUD import add_book, get_book
import logging

app = FastAPI

logging.basicConfig(level=logging.INFO)


@app.get("/")

def read_root():
  return {"Hello" : "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q : Union[str, None] = None):
  return {"item_id": item_id, "q": q}
