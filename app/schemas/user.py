from typing import List
from pydantic import BaseModel
from pydantic import EmailStr
from .market import Market

class UserBase(BaseModel):
    email: EmailStr

class User(UserBase):
    id: int
    favorites: List[Market] = []
    class Config:
        orm_mode = True

class UserCreate(UserBase):
    email: EmailStr
    password: str
