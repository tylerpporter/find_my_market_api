from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    # favorites = relationship(
    #     "Market",
    #     secondary="favorites",
    #     backref="users"
    # )

class Market(Base):
    __tablename__ = "markets"
    id = Column(Integer, primary_key=True, index=True)
    market_id = Column(Integer, index=True)
    # favorites = relationship(
    #     "User",
    #     secondary="favorites",
    #     backref="markets"
    # )

# class Favorite(Base):
#     __tablename__ = "favorites"
#     id = Column(Integer, primary_key=True, index=True)
#     market_id = Column(Integer, foreign_key=True)
#     user_id = Column(Integer, foreign_key=True)
