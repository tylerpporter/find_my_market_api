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

def test_can_get_all_users(db, cleanup):
    email = "dan@example.com"
    user_in = UserCreate(email=email)
    user = crud.create_user(db, user=user_in)
    email2 = "bob@example.com"
    user_in2 = UserCreate(email=email2)
    user2 = crud.create_user(db, user=user_in2)
    response = client.get("/users/")
    assert response.status_code == 200
    resp = response.json()
    assert resp == [{'email': 'dan@example.com', 'id': 1},
                    {'email': 'bob@example.com', 'id': 2}]
    assert len(resp) == 2

def test_can_get_a_single_user(db, cleanup):
    email = "dan@example.com"
    user_in = UserCreate(email=email)
    user = crud.create_user(db, user=user_in)
    response = client.get("/users/1")
    assert response.status_code == 200
    resp = response.json()
    assert resp == {'email': 'dan@example.com', 'id': 1}
