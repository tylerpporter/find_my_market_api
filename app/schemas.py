from typing import List, Optional
from pydantic import BaseModel

class MarketBase(BaseModel):
    fmid: int

class MarketCreate(MarketBase):
    pass

class Market(MarketBase):
    id: int
    owner_id: int
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    markets: List[Market] = []
    class Config:
        orm_mode = True