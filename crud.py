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

