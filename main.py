from app import create_app
from app.repository.db import init_db

app = create_app()

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
