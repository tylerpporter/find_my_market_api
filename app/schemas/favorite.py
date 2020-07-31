from typing import List
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
