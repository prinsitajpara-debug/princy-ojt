from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Employee
from app.schemas import EmployeeCreate

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)

@router.post("/")
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):
    db_employee = Employee(
        name=employee.name,
        email=employee.email
    )

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)

    return db_employee


@router.get("/")
def get_employees(
    db: Session = Depends(get_db)
):
    return db.query(Employee).all()