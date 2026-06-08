def test_create_employee(client):

    response = client.post(
        "/employees/",
        json={
            "name": "John",
            "email": "john@test.com"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "John"


def test_get_employees(client):

    response = client.get("/employees/")

    assert response.status_code == 200