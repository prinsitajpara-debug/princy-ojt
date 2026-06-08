"""
routes.py

Contains all Employee CRUD API endpoints.
"""

from flask import Blueprint
from flask import jsonify
from flask import request

from app.database import db
from app.models import Employee

employee_bp = Blueprint(
    "employee",
    __name__
)


@employee_bp.route("/", methods=["GET"])
def index():
    """
    API root endpoint.

    Returns:
        JSON response indicating the API is running.
    """

    return jsonify({"message": "Employee API is running"})


@employee_bp.route("/employees", methods=["POST"])
def create_employee():
    """
    Create a new employee.

    Returns:
        JSON response with created employee.
    """

    data = request.get_json()

    employee = Employee(
        name=data["name"],
        email=data["email"],
        department=data["department"]
    )

    db.session.add(employee)
    db.session.commit()

    return jsonify(employee.to_dict()), 201


@employee_bp.route("/employees", methods=["GET"])
def get_all_employees():
    """
    Get all employees.

    Returns:
        List of employees.
    """

    employees = Employee.query.all()

    return jsonify(
        [emp.to_dict() for emp in employees]
    )


@employee_bp.route("/employees/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):
    """
    Get employee by ID.

    Args:
        employee_id (int)

    Returns:
        Employee data.
    """

    employee = db.session.get(Employee, employee_id)

    if not employee:
        return jsonify(
            {"message": "Employee not found"}
        ), 404

    return jsonify(employee.to_dict())


@employee_bp.route("/employees/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):
    """
    Update employee details.

    Args:
        employee_id (int)

    Returns:
        Success message.
    """

    employee = db.session.get(Employee, employee_id)

    if not employee:
        return jsonify(
            {"message": "Employee not found"}
        ), 404

    data = request.get_json()

    employee.name = data.get(
        "name",
        employee.name
    )

    employee.department = data.get(
        "department",
        employee.department
    )

    db.session.commit()

    return jsonify(
        {"message": "Employee updated"}
    )


@employee_bp.route("/employees/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    """
    Delete employee.

    Args:
        employee_id (int)

    Returns:
        Success message.
    """

    employee = db.session.get(Employee, employee_id)

    if not employee:
        return jsonify(
            {"message": "Employee not found"}
        ), 404

    db.session.delete(employee)
    db.session.commit()

    return jsonify(
        {"message": "Employee deleted"}
    )