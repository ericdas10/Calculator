from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.model.base import Base  # declarative_base()
from app.config.settings import settings
from app.model.user import User
from app.model.request_log import RequestLog
from app.model.cache_entities import FibonacciCache, FactorialCache, PowCache 

engine = create_engine(settings.DB_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#creaza tabelele o singura data la pornire
def init_db():
    Base.metadata.create_all(bind=engine)
