from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship

from app.database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

    salaries = relationship("Salary", back_populates="employee")
    tasks = relationship("Task", back_populates="employee")


class Salary(Base):
    __tablename__ = "salaries"

    id = Column(Integer, primary_key=True)

    amount = Column(Float)

    employee_id = Column(
        Integer,
        ForeignKey("employees.id")
    )

    employee = relationship(
        "Employee",
        back_populates="salaries"
    )


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)

    title = Column(String)

    status = Column(String)

    employee_id = Column(
        Integer,
        ForeignKey("employees.id")
    )

    employee = relationship(
        "Employee",
        back_populates="tasks"
    )