from pydantic import BaseSettings

class Settings(BaseSettings):
  database_url: str = "postgresql://postgres@localhost/market_api"

settings = Settings()