from typing import List
from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api.deps import get_db

router = APIRouter()

@router.get("/", response_model=List[schemas.Market])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    markets = crud.get_markets(db, skip=skip, limit=limit)
    return markets
