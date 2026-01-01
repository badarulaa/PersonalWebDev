from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class BlogPost(BaseModel):
  title: str
  content: str
  tags: List[str]
  is_published: bool = False
  published_at: Optional[datetime] = None