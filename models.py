import typing import optional 
from pydantic import BaseModel, Field
from datetime import datetime

class book(BaseModel):
  id: Optional[str]
  Title: str
  Author: str
  Publication_date: datetime
  
