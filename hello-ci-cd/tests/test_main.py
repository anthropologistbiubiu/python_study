from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    r = client.get("/hello")
    assert r.status_code == 200
    assert r.json() == {"msg": "Hello, CI/CD"}
