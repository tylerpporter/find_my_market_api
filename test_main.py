
from fastapi import FastAPI
from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/api/v1/books")
    assert response.status_code == 200
    resp = response.JSON()
    assert resp == {"msg": "Hello World"}
