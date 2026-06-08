from pydantic import BaseModel


class EmployeeCreate(BaseModel):
    name: str
    email: str


class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True


class DocumentResponse(BaseModel):
    id: int
    employee_id: int
    file_name: str
    document_type: str

    class Config:
        from_attributes = True