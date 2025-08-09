from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert "MF Guru API" in resp.json().get("message", "") or "running" in resp.json().get("message", "")
