from typing import Union 
from models import  book
from fastapi import FastAPI, HTTPexception
from CRUD import add_book, get_book
import logging

app = FastAPI

logging.basicConfig(level=logging.INFO)

@app.post("/books", response_model = book

async def create_book(book: Book):
  book_dict = Book.dict()
  new_book = await add_book(book_dict)
  return new_book


@app.get("/")

def read_root():
  return {"Hello" : "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q : Union[str, None] = None):
  return {"item_id": item_id, "q": q}
