from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class SubscriptionLevel(Base):
    __tablename__ = "subscription_levels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(String)

    subscriptions = relationship("Subscription", back_populates="level")


class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    level_id = Column(Integer, ForeignKey("subscription_levels.id"))

    user = relationship("User", back_populates="subscriptions")
    level = relationship("SubscriptionLevel", back_populates="subscriptions")
