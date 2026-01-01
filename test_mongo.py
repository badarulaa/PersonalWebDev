import os
import asyncio
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

async def test_connection():
    mongo_uri = os.getenv("MONGODB_URI")
    if not mongo_uri:
        raise RuntimeError("MONGODB_URI tidak ditemukan di .env")

    client = AsyncIOMotorClient(mongo_uri)
    await client.admin.command("ping")
    print("✅ MongoDB CONNECTED")

if __name__ == "__main__":
    asyncio.run(test_connection())
