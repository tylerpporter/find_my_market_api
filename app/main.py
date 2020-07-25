# from typing import List
from fastapi import FastAPI
from . import crud, models, schemas
from .database import SessionLocal, engine
from app.api.routes import api_router
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(api_router)

#  WAITING FOR O-AUTH TO IMPLEMENT CREATE USER
# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)
