from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from datetime import datetime
from app.model.entity import Entity
from app.model.user import User
from app.model.base import Base

class RequestLog(Entity, Base):
    __tablename__ = 'request_logs'

    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    operation = Column(String(20), nullable=False)        # 'fibonacci', 'pow', 'factorial'
    input_data = Column(String, nullable=False)           # JSON stringified
    result = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow())

    user = relationship("User")
