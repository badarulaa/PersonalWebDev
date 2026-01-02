from pydantic import BaseModel, HttpUrl
from typing import List
from datetime import datetime

class ProjectCreate(BaseModel):
  title: str
  description: str
  tech_stack: List[str]
  github_url: HttpUrl

class Project(ProjectCreate):
  created_at: datetime
