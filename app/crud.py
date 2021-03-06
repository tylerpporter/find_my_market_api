from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from typing import Any, Dict, Union
from . import models, schemas
from app.security import get_hashed_password, verify_password
from IPython import embed

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email=email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        email=user.email,
        hashed_password=get_hashed_password(user.password),
        image=(user.image),
        username=(user.username)
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, db_obj: models.User, obj_in: Union[schemas.UserUpdate, Dict[str, Any]]):
    user_data = jsonable_encoder(db_obj)
    if isinstance(obj_in, dict):
        update_data = obj_in
    else:
        update_data = obj_in.dict(exclude_unset=True)
    if update_data.get("password"):
        hashed_password=get_hashed_password(update_data['password'])
        del update_data['password']
        update_data['hashed_password'] = hashed_password
    for field in user_data:
        if field in update_data:
            setattr(db_obj, field, update_data[field])
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

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

def delete_user_favorite(db: Session, user_id: int, market_id: int):
    db_fav = get_favorite(db, user_id=user_id, market_id=market_id)
    db.delete(db_fav)
    db.commit()
    user = get_user(db, user_id=user_id)
    return user

def get_favorite(db: Session, user_id: int, market_id: int):
    db_market = db.query(models.Market).filter(models.Market.market_id == market_id).first().id
    db_fav = db.query(models.Favorite).filter(models.Favorite.user_id == user_id).filter(models.Favorite.market_id == db_market).first()
    return db_fav