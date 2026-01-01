from fastapi import FastAPI
from app.core.config import settings
from app.core.database import database
from app.models.profile import Profile
from app.api import profile, project

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(profile.router)
app.include_router(project.router)

@app.get("/health")
async def health_check():
  await database.command("ping")
  return {
    "status": "ok",
    "environment": settings.ENVIRONMENT,
    "database": "connected"
  }

@app.get("/profile", response_model=Profile)
def get_profile():
  return {
    "name": "Badarul Alam",
    "role": "Python Developer",
    "bio": "Learning day by day to be a better developer.",
    "tech_stack": ["Python", "FastAPI", "Django", "MongoDB"]
  }