from fastapi import FastAPI
from app.db.database import engine, Base
from app.api.router import user, subscription

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Подключаем маршруты
app.include_router(user.router, prefix="/users")
app.include_router(subscription.router, prefix="/subscriptions")

@app.get("/")
def read_root():
    return {"message": "Subscription service is running!"}
