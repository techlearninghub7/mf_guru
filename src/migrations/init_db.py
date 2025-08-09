# run this script to create tables locally or on Supabase DB
import sys
from pathlib import Path
from sqlalchemy import create_engine
from ..config import DATABASE_URL
from ..db import metadata

def main():
    # Use SQLAlchemy create_all via sync engine
    engine = create_engine(DATABASE_URL, future=True)
    metadata.create_all(engine)
    print("✅ Tables created (if not existing).")

if __name__ == "__main__":
    main()
