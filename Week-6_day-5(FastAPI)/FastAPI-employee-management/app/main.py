from fastapi import FastAPI

from app.database import Base
from app.database import engine

from app.routers import employees
from app.routers import salaries
from app.routers import tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Employee Management API",
    version="1.0.0"
)

app.include_router(employees.router)
app.include_router(salaries.router)
app.include_router(tasks.router)