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

def test_create_user_favorites(db, cleanup):
  email = "bob@example.com"
  market_id = 1
  user_in = UserCreate(email=email)
  market_in = MarketCreate(market_id=market_id)
  user = crud.create_user(db, user=user_in)
  market = crud.create_market(db, market= market_in)
  favorite_in = FavoriteCreate(user_id=user.id, market_id=market.id)
  favorite = crud.favorite_market(db, favorite=favorite_in)

  assert favorite.user_id == user.id
  assert favorite.market_id == market.id
  assert user.favorites[0] == market