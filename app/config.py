import secrets
from pydantic import BaseSettings
from os import getenv

class Settings(BaseSettings):
  DATABASE_URL: str = "postgresql://postgres@localhost/market_api"
  SECRET_KEY: str = secrets.token_urlsafe(32)

settings = Settings()
