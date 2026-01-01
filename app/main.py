from fastapi import FastAPI
from app.core.config import settings
from app.core.database import database

app = FastAPI(title=settings.PROJECT_NAME)

@app.get("/health")
async def health_check():
  await database.command("ping")
  return {
    "status": "ok",
    "environment": settings.ENVIRONMENT,
    "database": "connected"
  }
