from sqlalchemy import Column, Integer, BigInteger, Float, PrimaryKeyConstraint, String
from app.model.base import Base

class FibonacciCache(Base):
    __tablename__ = 'fibonacci_cache'

    n = Column(Integer, primary_key=True)
    result = Column(String, nullable=False)


class FactorialCache(Base):
    __tablename__ = 'factorial_cache'

    n = Column(Integer, primary_key=True)
    result = Column(String, nullable=False)


class PowCache(Base):
    __tablename__ = 'pow_cache'

    base = Column(Float, nullable=False)
    exponent = Column(Float, nullable=False)
    result = Column(String, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('base', 'exponent', name='pk_pow_cache'),
    )
