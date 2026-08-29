from fastapi.testclient import TestClient

from app import app

client = TestClient(app)

def test_home():
    response = client.get("/hello-world/")

    assert response.status_code == 200
    assert response.json() == "Hello World"