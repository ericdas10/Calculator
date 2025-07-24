import os
from dotenv import load_dotenv

load_dotenv()  # dacă folosești un .env file

class Settings:
    DB_URL = os.getenv("DATABASE_URL",
        "mssql+pyodbc://sa:yourStrong(!)Password@localhost:1433/calculatorDB?driver=ODBC+Driver+17+for+SQL+Server")

settings = Settings()
