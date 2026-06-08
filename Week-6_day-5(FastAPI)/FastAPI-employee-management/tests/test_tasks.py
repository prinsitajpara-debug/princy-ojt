def test_create_task(client):

    client.post(
        "/employees/",
        json={
            "name": "Amit",
            "email": "amit@test.com"
        }
    )

    response = client.post(
        "/tasks/",
        json={
            "title": "Build API",
            "status": "Pending",
            "employee_id": 1
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Build API"


def test_get_tasks(client):

    response = client.get("/tasks/")

    assert response.status_code == 200