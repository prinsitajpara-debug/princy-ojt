"""
test_employee.py

Contains Employee API test cases.
"""


def test_create_employee(client):
    """
    Test employee creation.
    """

    response = client.post(
        "/employees",
        json={
            "name": "prinsi",
            "email": "prinsi@test.com",
            "department": "IT"
        }
    )

    assert response.status_code == 201


def test_get_all_employees(client):
    """
    Test get all employees.
    """

    client.post(
        "/employees",
        json={
            "name": "prinsi",
            "email": "prinsi@test.com",
            "department": "IT"
        }
    )

    response = client.get(
        "/employees"
    )

    assert response.status_code == 200
    assert len(response.json) == 1


def test_get_employee_by_id(client):
    """
    Test get employee by id.
    """

    create_response = client.post(
        "/employees",
        json={
            "name": "prinsi",
            "email": "prinsi@test.com",
            "department": "IT"
        }
    )

    employee_id = create_response.json["id"]

    response = client.get(
        f"/employees/{employee_id}"
    )

    assert response.status_code == 200


def test_update_employee(client):
    """
    Test update employee.
    """

    create_response = client.post(
        "/employees",
        json={
            "name": "prinsi",
            "email": "prinsi@test.com",
            "department": "IT"
        }
    )

    employee_id = create_response.json["id"]

    response = client.put(
        f"/employees/{employee_id}",
        json={
            "name": "Updated User"
        }
    )

    assert response.status_code == 200


def test_delete_employee(client):
    """
    Test delete employee.
    """

    create_response = client.post(
        "/employees",
        json={
            "name": "prinsi",
            "email": "prinsi@test.com",
            "department": "IT"
        }
    )

    employee_id = create_response.json["id"]

    response = client.delete(
        f"/employees/{employee_id}"
    )

    assert response.status_code == 200


def test_employee_not_found(client):
    """
    Test invalid employee id.
    """

    response = client.get(
        "/employees/999"
    )

    assert response.status_code == 404