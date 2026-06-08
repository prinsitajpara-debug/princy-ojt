from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Salary
from app.schemas import SalaryCreate

router = APIRouter(
    prefix="/salaries",
    tags=["Salary"]
)

@router.post("/")
def create_salary(
    salary: SalaryCreate,
    db: Session = Depends(get_db)
):
    db_salary = Salary(**salary.model_dump())

    db.add(db_salary)
    db.commit()
    db.refresh(db_salary)

    return db_salary


@router.get("/")
def get_salaries(
    db: Session = Depends(get_db)
):
    return db.query(Salary).all()