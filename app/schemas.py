from typing import List, Optional
from pydantic import BaseModel

class MarketBase(BaseModel):
    market_id: int

class Market(MarketBase):
    id: int
    class Config:
        orm_mode = True

class MarketCreate(MarketBase):
    pass

class UserBase(BaseModel):
    email: str

class User(UserBase):
    id: int
    # favorites: List[Favorite] = []
    class Config:
        orm_mode = True

class UserCreate(UserBase):
    pass

class FavoriteBase(BaseModel):
    market_id: int
    user_id: int

class Favorite(FavoriteBase):
    id: int

class FavoriteCreate(FavoriteBase):
    pass
