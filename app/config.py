from pydantic import BaseSettings
from os import getenv

class Settings(BaseSettings):
  database_url: str = "postgresql://postgres@localhost/market_api"
  
settings = Settings()
