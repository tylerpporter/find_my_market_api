from typing import Any

from fastapi import Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api.deps import get_db
from app.config import settings
from IPython import embed
from app.security import create_access_token
from app.api.deps import get_current_user



router = APIRouter()

@router.post("/login/token", response_model=schemas.Token)
def login_access_token(
  db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
  ):
  user = crud.authenticate_user(
    db, email=form_data.username, password=form_data.password
  )
  if not user:
    raise HTTPException(status_code=400, detail="Incorrect email or password")
  # Maybe add expiration to token here if deemed necessary
  return {
    "access_token": create_access_token(
      user.id
    ),
    "token_type": "bearer"
  }

@router.post("/login/token_check", response_model=schemas.User)
def check_token(current_user: models.User = Depends(get_current_user)) -> Any:
  return current_user