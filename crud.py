from models import book, book_review
from database import book_collection, review_collection
from datetime import datetime
from bson import ObjectId

def book_helper(book) - > dict:
  return {
    "id": str(book["_id"]),
    "title"
    "author"
    "



  }

