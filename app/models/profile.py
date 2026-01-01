from pydantic import BaseModel
from typing import List

class Profile(BaseModel):
  name: str
  role: str
  bio: str
  tech_stack: List[str]