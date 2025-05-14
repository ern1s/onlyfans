from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Строка подключения для асинхронного PostgreSQL
SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}/{settings.DATABASE_NAME}"

# Создаём асинхронный движок
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Создаём асинхронный sessionmaker
SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False
)

# Функция для получения сессии базы данных
async def get_db():
    async with SessionLocal() as db:
        yield db
