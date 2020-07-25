from typing import List
from fastapi import Depends, FastAPI, HTTPException, APIRouter, Body
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api.deps import get_db
from IPython import embed
# from app.core.config import settings

router = APIRouter()

@router.get("/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.post("/{user_id}/favorites", response_model=schemas.Favorite)
def favorite_a_market(
    user_id: int, market_id: int = Body(..., embed=True), db: Session = Depends(get_db)):
    favorite_in = schemas.FavoriteCreate(user_id=user_id, market_id=market_id)
    favorite = crud.favorite_market(db, favorite=favorite_in)
    return favorite
