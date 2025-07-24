from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column, Integer
from app.model.base import Base

class Entity:
    @declared_attr
    def id(cls):
        return Column(Integer, primary_key=True, autoincrement=True)