from fastapi import APIRouter
from app.api.endpoints import users, markets, login

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users")
api_router.include_router(markets.router, prefix="/markets")
api_router.include_router(login.router)
