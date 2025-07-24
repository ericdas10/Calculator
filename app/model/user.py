from sqlalchemy import Column, String
from app.model.entity import Entity
from app.model.base import Base

class User(Entity, Base):
    __tablename__ = 'users'

    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(256), nullable=False)
