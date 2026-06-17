from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL =  "postgresql://postgres:Prinsi%401318@localhost:5433/alembic_demo"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)