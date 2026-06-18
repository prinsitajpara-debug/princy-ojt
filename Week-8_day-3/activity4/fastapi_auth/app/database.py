import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Use DATABASE_URL from environment if provided, otherwise fallback to local PostgreSQL.
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:Prinsi%401318@localhost:5433/auth_demo"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()