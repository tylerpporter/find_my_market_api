from fastapi import FastAPI
from fastapi.testclient import TestClient

from IPython import embed
from sqlalchemy import create_engine
from app.database import Base
from app.main import app
import pytest
from fastapi.encoders import jsonable_encoder
from app.database import SessionLocal
from app import crud
from app.schemas import UserCreate
from os import getenv

engine = create_engine(getenv("DATABASE_URL"))
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

@pytest.fixture
def db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    yield db
    db.close()

@pytest.fixture
def cleanup():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

client = TestClient(app)

def test_it_can_login_a_user(db, cleanup):
  email = "zach@example.com"
  password = "123456"
  user_in = UserCreate(email=email, password=password)
  user = crud.create_user(db, user=user_in)
  response = client.post("/login/token",
  data={"username": email, "password": password})
  resp = response.json()
  
  assert response.status_code == 200
  assert "access_token" in resp
  assert resp["access_token"]


def test_access_token_works(db, cleanup):
    email = "zach@example.com"
    password = "123456"
    user_in = UserCreate(email=email, password=password)
    user = crud.create_user(db, user=user_in)
    response = client.post("/login/token",
    data={"username": email, "password": password})
    token = response.json()
    a_token = token["access_token"]
    headers = {"Authorization": f"Bearer {a_token}"}
    response2 =  client.post("/login/token_check", headers=headers)
    assert response2.status_code == 200
