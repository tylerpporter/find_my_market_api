from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

import uvicorn
import json

models.Base.metadata.create_all(bind = engine) # Creates all DB tables at once

# Creates dependancy for db session/connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI(debug=True)

with open("books.json") as f:
    books = json.load(f)
    
@app.get('/api/v1')
async def root():
    return 'Welcome to API'

@app.get('/api/v1/books')
async def get_books():
    return books  

if __name__ == '__main__':
    uvicorn.run(app, post='127.0.0.1', port='8000')
