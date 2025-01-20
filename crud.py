from models import book, book_review
from database import book_collection, review_collection
from datetime import datetime
from bson import ObjectId

def book_helper(book) - > dict:
  return {
    "Id": str(book["_id"]),
    "Title": book["Title"]
    "Author": book["Author"]
    "Publication_date": book["Publication_date"]
  }

# CRUD function

async def add_book(book_data: dict) -> dict:
    book = await book_collection.insert_one(book_data)
    new_book = await book_collection.find_one({"_id": book.inserted_id})
    return book_helper(new_book)

async def get_book(id: str) -> dict:
    book = await book_collection.find_one({"_id": ObjectId(id)})
    if book:
        return book_helper(book)
