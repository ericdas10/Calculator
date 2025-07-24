from sqlalchemy.orm import Session
from app.model.user import User
from app.model.request_log import RequestLog

def save_request_log(db: Session, log: RequestLog):
    db.add(log)
    db.commit()
    db.refresh(log)
    return log

def get_all_logs(db: Session):
    return db.query(RequestLog).all()

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
