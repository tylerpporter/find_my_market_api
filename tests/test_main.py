from IPython import embed
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.main import app, get_db
import pytest
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from typing import Dict, Generator
from app.database import SessionLocal

from app import crud
from app.schemas import UserCreate
from os import getenv
engine = create_engine(getenv("DATABASE_URL"))
# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

@pytest.fixture(scope="session")
def db() -> Generator:
    yield SessionLocal()
#
# @pytest.fixture(scope="session", autouse=True)
# def clean_up():
#     Base.metadata.create_all(bind=engine)
#     yield
#     Base.metadata.drop_all(bind=engine)

def test_create_user(db: Session):
    email = "dan@example.com"
    user_in = UserCreate(email=email)
    user = crud.create_user(db, user=user_in)
    assert user.email == email

def test_create_user_again(db: Session):
    email = "dan@example.com"
    user_in = UserCreate(email=email)
    user = crud.create_user(db, user=user_in)
    assert user.email == email
