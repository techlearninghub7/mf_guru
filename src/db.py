from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from .config import DATABASE_URL

# Create synchronous engine
# If using Supabase Postgres with psycopg2, DATABASE_URL should be:
# postgresql+psycopg2://user:pass@host:5432/dbname?sslmode=require
engine = create_engine(DATABASE_URL, future=True, echo=False)

# Session factory
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# SQLAlchemy metadata container (for table creation)
metadata = MetaData()
