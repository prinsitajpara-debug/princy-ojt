def test_create_salary(client):

    client.post(
        "/employees/",
        json={
            "name": "Raj",
            "email": "raj@test.com"
        }
    )

    response = client.post(
        "/salaries/",
        json={
            "amount": 50000,
            "employee_id": 1
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["amount"] == 50000


def test_get_salaries(client):

    response = client.get("/salaries/")

    assert response.status_code == 200