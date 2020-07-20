
from fastapi import FastAPI
from fastapi.testclient import TestClient
from IPython import embed
from ..main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/api/v1")
    assert response.status_code == 200
    resp = response.json()
    assert resp == 'Welcome to API'