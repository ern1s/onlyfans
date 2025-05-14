from pydantic import BaseModel
from typing import Optional

# Уровень подписки (для чтения и создания)
class SubscriptionLevelBase(BaseModel):
    name: str
    price: int
    description: Optional[str] = None

class SubscriptionLevelCreate(SubscriptionLevelBase):
    pass

class SubscriptionLevelOut(SubscriptionLevelBase):
    id: int

    class Config:
        orm_mode = True

# Подписка пользователя
class SubscriptionBase(BaseModel):
    user_id: int
    level_id: int

class SubscriptionCreate(SubscriptionBase):
    pass

class SubscriptionOut(SubscriptionBase):
    id: int

    class Config:
        orm_mode = True
