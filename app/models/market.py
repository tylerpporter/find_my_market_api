from sqlalchemy import Integer, Column
from sqlalchemy.orm import relationship
from app.database import Base

class Market(Base):
    __tablename__ = "markets"
    id = Column(Integer, primary_key=True, index=True)
    market_id = Column(Integer, index=True)
    favorites = relationship(
        "User",
        secondary="favorites",
        backref="markets"
    )