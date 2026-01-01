import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGODB_URI = os.getenv("MONGODB_URI")

if not MONGODB_URI:
  raise RuntimeError("MONGODB_URI masih belum disetting di .env")

client = AsyncIOMotorClient(MONGODB_URI)
database = client["personal_dev_hub"]