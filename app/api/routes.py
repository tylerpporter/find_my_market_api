from fastapi import APIRouter
from app.api.endpoints import users, markets

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users")
api_router.include_router(markets.router, prefix="/markets")
