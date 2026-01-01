from fastapi import APIRouter
from app.core.database import database
from app.models.profile import Profile

router = APIRouter(prefix="/profile", tags=["Profile"])

COLLECTION = "profile"

@router.post("/", response_model=Profile)
async def create_profile(profile: Profile):
  await database[COLLECTION].delete_many({})
  await database[COLLECTION].insert_one(profile.dict())
  return profile

@router.get("/", response_model=Profile)
async def get_profile():
  data = await database[COLLECTION].find_one({})
  return data