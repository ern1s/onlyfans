from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.session import get_db
from app.models.subscription import Subscription, SubscriptionLevel
from app.schemas.subscription import SubscriptionCreate, SubscriptionOut, SubscriptionLevelOut

router = APIRouter()

# Получение всех подписок
@router.get("/subscriptions", response_model=list[SubscriptionOut])
async def get_subscriptions(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Subscription))
    subscriptions = result.scalars().all()
    return subscriptions

# Получение подписок для конкретного пользователя
@router.get("/users/{user_id}/subscriptions", response_model=list[SubscriptionOut])
async def get_user_subscriptions(user_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Subscription).filter(Subscription.user_id == user_id))
    subscriptions = result.scalars().all()
    return subscriptions

# Получение всех уровней подписки
@router.get("/subscription-levels", response_model=list[SubscriptionLevelOut])
async def get_subscription_levels(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(SubscriptionLevel))
    levels = result.scalars().all()
    return levels

# Подписка пользователя на уровень
@router.post("/subscriptions", response_model=SubscriptionOut)
async def create_subscription(subscription: SubscriptionCreate, db: AsyncSession = Depends(get_db)):
    level = await db.execute(select(SubscriptionLevel).filter(SubscriptionLevel.id == subscription.level_id))
    level = level.scalars().first()
    if not level:
        raise HTTPException(status_code=404, detail="Subscription level not found")
    
    new_subscription = Subscription(user_id=subscription.user_id, level_id=subscription.level_id)
    db.add(new_subscription)
    await db.commit()
    await db.refresh(new_subscription)
    return new_subscription
