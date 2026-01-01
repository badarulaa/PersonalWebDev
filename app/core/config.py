import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
  PROJECT_NAME = os.getenv("PROJECT_NAME", "Personal Website")
  ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

settings = Settings()