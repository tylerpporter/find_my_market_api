import pytest
from IPython import embed
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.main import app, get_db
from app.schemas import UserCreate
from app.crud import create_user
# import app.models

SQLALCHEMY_DATABASE_URL = "postgresql://postgres@localhost/market_api_test"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

@pytest.fixture
def clean_db():
    yield
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_and_get_user(clean_db):
    response = client.post(
        "/users/",
        json={"email": "tod@example.com"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "tod@example.com"
    assert "id" in data
    user_id = data["id"]
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "tod@example.com"
    assert data["id"] == user_id


def test_user_favorite_a_market(clean_db):
    response = client.post(
        "/users/",
        json={"email": "tod@example.com"},
    )
    id = response.json()['id']
    market_response = client.post(
      f"/users/{id}/markets/",
      json={"fmid": 10008999}
    )
    assert market_response.status_code == 200

    market = market_response.json()
    assert market['owner_id'] == id

    user_resp = client.get(
      f"/users/{id}/"
    )

    user = user_resp.json()
    assert len(user['markets']) == 1
    assert user['markets'][0]['fmid'] == 10008999


