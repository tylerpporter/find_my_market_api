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
from app.schemas import MarketCreate, UserCreate, FavoriteCreate
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

def test_can_create_a_favorite_with_existing_market_in_db(db, cleanup):
    market_id = 123456
    market_in = MarketCreate(market_id=market_id)
    market = crud.create_market(db, market=market_in)
    email = "dan@example.com"
    password = "123456"
    user_in = UserCreate(email=email, password=password)
    user = crud.create_user(db, user=user_in)
    response = client.post(f"/users/{user.id}/favorites",
    json={"fmid": market_id})
    assert response.status_code == 200
    resp = response.json()
    assert resp['favorites'] == [{'market_id': 123456, 'id': 1}]
    assert user.favorites[0].market_id == 123456

def test_can_create_a_favorite_with_no_existing_market(db, cleanup):
    market_id = 123
    email = "dan@example.com"
    password = "123456"
    user_in = UserCreate(email=email, password=password)
    user = crud.create_user(db, user=user_in)
    response = client.post(f"/users/{user.id}/favorites",
    json={"fmid": market_id})
    assert response.status_code == 200

def test_it_cant_create_a_favorite_if_user_already_has_one(db, cleanup):
    market_id = 123
    email = "dan@example.com"
    password = "123456"
    user_in = UserCreate(email=email, password=password)
    user = crud.create_user(db, user=user_in)
    market_in = MarketCreate(market_id=market_id)
    market = crud.create_market(db, market=market_in)
    favorite_in = FavoriteCreate(user_id= user.id, market_id=market.id)
    favorite = crud.favorite_market(db, favorite=favorite_in)
    response = client.post(f"/users/{user.id}/favorites",
    json={"fmid": market_id})
    assert response.status_code == 400
    resp = response.json()
    assert resp['detail'] == 'That market is already favorited!'

def test_it_can_get_all_user_favorites(db, cleanup):
    market_id = 123456
    market_in = MarketCreate(market_id=market_id)
    market = crud.create_market(db, market=market_in)
    email = "dan@example.com"
    password = "123456"
    user_in = UserCreate(email=email, password=password)
    user = crud.create_user(db, user=user_in)
    client.post(f"/users/{user.id}/favorites",
    json={"fmid": market_id})
    response = client.get(f"/users/{user.id}/favorites")

    assert response.status_code == 200
    resp = response.json()
    assert resp['favorites'] == [{'market_id': 123456, 'id': 1}]

def test_it_can_delete_user_favorites(db, cleanup):
    market_id = 123456
    market_in = MarketCreate(market_id=market_id)
    market = crud.create_market(db, market=market_in)
    email = "dan@example.com"
    password = "123456"
    user_in = UserCreate(email=email, password=password)
    user = crud.create_user(db, user=user_in)
    client.post(f"/users/{user.id}/favorites",
    json={"fmid": market_id})
    response = client.get(f"/users/{user.id}")
    user_resp = response.json()

    assert len(user_resp['favorites']) == 1

    response2 = client.delete(f"/users/{user.id}/favorites",
    json={"fmid": market_id})
    user_resp2 = response2.json()
    assert response2.status_code == 200

    assert user_resp2['favorites'] == []
    assert len(user_resp2['favorites']) == 0
