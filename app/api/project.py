from fastapi import APIRouter
from datetime import datetime
from app.core.database import database
from app.models.project import Project, ProjectCreate
from typing import List

router = APIRouter(prefix="/projects", tags=["Projects"])

COLLECTION = "projects"

@router.post("/", response_model=Project)
async def create_project(project: ProjectCreate):
  data = project.dict()
  data["created_at"] = datetime.utcnow()
  await database[COLLECTION].insert_one(data)
  return data

@router.get("/", response_model=list[Project])
async def list_projects():
  projects = []
  cursor = database[COLLECTION].find().sort("created_at", -1)

  async for doc in cursor:
    doc.pop("_id", None)
    projects.append(doc)

  return projects