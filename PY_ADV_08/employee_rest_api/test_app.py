import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200


def test_get_employees(client):
    response = client.get("/employees")
    assert response.status_code == 200


def test_get_employee_by_id(client):
    response = client.get("/employees/1")
    assert response.status_code in [200, 404]


def test_create_employee_validation(client):
    response = client.post("/employees", json={})
    assert response.status_code == 400


def test_update_employee_not_found(client):
    response = client.put(
        "/employees/999999",
        json={
            "employee_name": "Test User",
            "email": "testuser@example.com",
            "department": "IT",
            "salary": 50000,
            "department_id": 1
        }
    )
    assert response.status_code == 404


def test_delete_employee_not_found(client):
    response = client.delete("/employees/999999")
    assert response.status_code == 404