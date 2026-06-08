from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Employee
from app.schemas import (
    EmployeeCreate,
    EmployeeResponse
)

router = APIRouter(
    prefix="/api/v1/employees",
    tags=["Employees"]
)


@router.post(
    "",
    response_model=EmployeeResponse
)
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):

    new_employee = Employee(
        name=employee.name,
        email=employee.email
    )

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return new_employee