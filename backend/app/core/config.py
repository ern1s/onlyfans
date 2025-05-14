import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/postgres")

settings = Settings()

import os

class Settings:
    DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
    DATABASE_NAME = os.getenv("DATABASE_NAME", "subscription_db")
    DATABASE_USER = os.getenv("DATABASE_USER", "user")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "password")

settings = Settings()
