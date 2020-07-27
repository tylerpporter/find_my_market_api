from typing import List, Optional
from pydantic import BaseModel

class FavoriteBase(BaseModel):
    market_id: int
    user_id: int

class Favorite(FavoriteBase):
    id: int
    class Config:
        orm_mode = True
        
class FavoriteCreate(FavoriteBase):
    pass

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
    favorites: List[Favorite] = []
    class Config:
        orm_mode = True

class UserCreate(UserBase):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenPayload(BaseModel):
    sub: Optional[int] = None
