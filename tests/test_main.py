from IPython import embed
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
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

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

def test_create_user():
    db = SessionLocal()
    email = "dan@example.com"
    user_in = UserCreate(email=email)
    user = crud.create_user(db, user=user_in)
    assert user.email == email
    engine.dispose()
    db.rollback()
    db.close()
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def test_create_user_again():
    db = SessionLocal()
    email = "dan@example.com"
    user_in = UserCreate(email=email)
    user = crud.create_user(db, user=user_in)
    assert user.email == email
    engine.dispose()
    db.rollback()
    db.close()
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
