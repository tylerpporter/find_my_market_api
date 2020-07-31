from sqlalchemy import Integer, ForeignKey, Column
from app.database import Base

class Favorite(Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key=True, index=True)
    market_id = Column(Integer, ForeignKey("markets.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
