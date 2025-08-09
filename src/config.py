import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")  # e.g. postgresql+psycopg2://...
APP_ENV = os.getenv("APP_ENV", "development")

# If no DATABASE_URL provided, use SQLite local fallback
if not DATABASE_URL or DATABASE_URL.strip() == "":
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    DB_FILE = os.path.join(BASE_DIR, "data", "mf_guru.db")
    os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)
    DATABASE_URL = f"sqlite:///{DB_FILE}"
