from sqlalchemy.orm import Session
from . import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_market(db: Session, market: schemas.MarketCreate):
    db_market = models.Market(market_id=market.market_id)
    db.add(db_market)
    db.commit()
    db.refresh(db_market)
    return db_market

def get_markets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Market).offset(skip).limit(limit).all()

def get_market_by_fmid(db: Session, fmid: int):
    return db.query(models.Market).filter(models.Market.market_id == fmid).first()

def favorite_market(db: Session, favorite: schemas.FavoriteCreate):
    db_favorite = models.Favorite(user_id=favorite.user_id, market_id=favorite.market_id)
    db.add(db_favorite)
    db.commit()
    db.refresh(db_favorite)
    return db_favorite
