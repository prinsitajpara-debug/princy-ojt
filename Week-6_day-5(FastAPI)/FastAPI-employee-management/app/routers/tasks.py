from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Task
from app.schemas import TaskCreate

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

@router.post("/")
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db)
):
    db_task = Task(**task.model_dump())

    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task


@router.get("/")
def get_tasks(
    db: Session = Depends(get_db)
):
    return db.query(Task).all()