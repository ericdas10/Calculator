from app.repository.db import init_db, SessionLocal
from app.model.user import User

init_db()

db = SessionLocal()
user = User(username="admin", password="secret")
db.add(user)
db.commit()
db.close()
