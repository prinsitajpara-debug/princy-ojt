from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

DATABASE_URL = "postgresql://postgres:Prinsi%401318@localhost:5432/employee_db"

#database connection object


engine = create_engine(DATABASE_URL)

#create session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

#database dependency function
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()