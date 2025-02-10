import typing import optional 
from pydantic import BaseModel, Field
from datetime import datetime


class book(BaseModel):
  id: Optional[str]
  Title: str
  Author: str
  Publication_date: datetime
  
class book_review(BaseModel):
  id = Optional[str]
  book_id: int
  reviewer: str
  rating: int
  comments: Optional[str]
  review_date: datetime
