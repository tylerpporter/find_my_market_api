# from typing import List
from fastapi import FastAPI
from . import crud, models, schemas
from .database import SessionLocal, engine, Base
from app.api.routes import api_router
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(api_router)

