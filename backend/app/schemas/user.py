from pydantic import BaseModel

# Схема для регистрации пользователя
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

# Схема для логина
class UserLogin(BaseModel):
    email: str
    password: str

# Схема для ответа (информация о пользователе)
class UserOut(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True  # Позволяет Pydantic работать с SQLAlchemy моделями
