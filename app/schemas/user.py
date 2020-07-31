from typing import List
from pydantic import BaseModel
from .market import Market

class UserBase(BaseModel):
    email: str

class User(UserBase):
    id: int
    favorites: List[Market] = []
    class Config:
        orm_mode = True

class UserCreate(UserBase):
    email: str
    password: str
