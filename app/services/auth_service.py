# app/services/auth_service.py

from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import Session
from app.model.user import User
from app.repository import repository
from app.model.schemas import UserCreate

def register_user(user_data: UserCreate, db: Session):
    existing_user = repository.get_user_by_username(db, user_data.username)
    if existing_user:
        raise ValueError("Username already exists")

    hashed_password = generate_password_hash(user_data.password)
    new_user = User(username=user_data.username, password=hashed_password)
    print(f"New user created: {new_user.username}")
    return repository.create_user(db, new_user)


def login_user(user_data: UserCreate, db: Session):
    user = repository.get_user_by_username(db, user_data.username)
    if not user or not check_password_hash(user.password, user_data.password):
        raise ValueError("Invalid username or password")

    return user  # pentru integrare cu autentificare, poți returna și token
