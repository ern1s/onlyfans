from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin, UserOut
from app.db.session import get_db
from app.auth.jwt_handler import create_access_token
from app.auth.jwt_bearer import jwt_bearer  # Зависимость для проверки токена
from passlib.context import CryptContext

router = APIRouter(prefix="/users", tags=["users"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Регистрация нового пользователя
@router.post("/register", response_model=UserOut)
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    # Проверяем, существует ли уже пользователь с таким email
    result = await db.execute(select(User).where(User.email == user.email))
    existing_user = result.scalars().first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Хешируем пароль
    hashed_password = pwd_context.hash(user.password)
    
    # Создаем нового пользователя
    new_user = User(username=user.username, email=user.email, password=hashed_password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    
    return {"id": new_user.id, "email": new_user.email}

# Логин пользователя
@router.post("/login")
async def login(user: UserLogin, db: AsyncSession = Depends(get_db)):
    # Проверяем, существует ли пользователь с таким email
    result = await db.execute(select(User).where(User.email == user.email))
    db_user = result.scalars().first()
    if not db_user or not pwd_context.verify(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Создаем токен для авторизованного пользователя
    token = create_access_token({"sub": db_user.id})
    return {"access_token": token, "token_type": "bearer"}

# Получение информации о текущем пользователе
@router.get("/me", response_model=UserOut)
async def get_user_me(db: AsyncSession = Depends(get_db), token: dict = Depends(jwt_bearer)):
    # Получаем пользователя по ID из токена
    result = await db.execute(select(User).where(User.id == token["sub"]))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
