from typing import List, Optional
from pydantic import BaseModel
from pydantic import EmailStr
from .market import Market

class UserBase(BaseModel):
    email: EmailStr

class User(UserBase):
    id: int
    favorites: List[Market] = []
    image: Optional[str]
    username: Optional[str]
    class Config:
        orm_mode = True

class UserCreate(UserBase):
    email: EmailStr
    password: str
    image: Optional[str]
    username: Optional[str]

class UserUpdate(UserBase):
    email: Optional[EmailStr]
    password: Optional[str]
    image: Optional[str]
    username: Optional[str]
    
