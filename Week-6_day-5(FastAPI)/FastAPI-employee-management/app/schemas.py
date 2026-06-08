from pydantic import BaseModel, ConfigDict


class EmployeeCreate(BaseModel):
    name: str
    email: str


class EmployeeResponse(EmployeeCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


class SalaryCreate(BaseModel):
    amount: float
    employee_id: int


class SalaryResponse(SalaryCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


class TaskCreate(BaseModel):
    title: str
    status: str
    employee_id: int


class TaskResponse(TaskCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)