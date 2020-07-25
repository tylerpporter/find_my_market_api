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
from app.schemas import MarketCreate
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

def test_can_get_all_markets(db, cleanup):
    market_id = 123456
    market_in = MarketCreate(market_id=market_id)
    market = crud.create_market(db, market=market_in)
    market_id2 = 234567
    market_in2 = MarketCreate(market_id=market_id2)
    market2 = crud.create_market(db, market=market_in2)
    response = client.get("/markets")
    assert response.status_code == 200
    resp = response.json()
    assert resp == [{'market_id': 123456, 'id': 1}, {'market_id': 234567, 'id': 2}]

# def test_create_market(db, cleanup):
#   market_id = 1
#   market_in = MarketCreate(market_id=market_id)
#   market = crud.create_market(db, market=market_in)
#   assert market.market_id == 1
