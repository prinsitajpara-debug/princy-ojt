"""
models.py

This module contains all database models.

Employee:
    Stores employee information.
"""

from app.database import db


class Employee(db.Model):
    """
    Employee database model.

    Attributes:
        id (int): Primary key.
        name (str): Employee name.
        email (str): Employee email.
        department (str): Employee department.
    """

    __tablename__ = "employees"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    department = db.Column(
        db.String(100),
        nullable=False
    )

    def to_dict(self):
        """
        Convert model object to dictionary.

        Returns:
            dict
        """
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "department": self.department
        }