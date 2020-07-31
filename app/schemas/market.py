from pydantic import BaseModel

class MarketBase(BaseModel):
    market_id: int

class Market(MarketBase):
    id: int
    class Config:
        orm_mode = True

class MarketCreate(MarketBase):
    pass