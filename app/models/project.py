from pydantic import BaseModel, HttpUrl
from typing import List
from datetime import datetime

class Project(BaseModel):
  title: str
  description: str
  tech_stack: List[str]
  github_url: HttpUrl
  created_at: datetime
  