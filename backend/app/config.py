from functools import lru_cache
from os import getenv
from pydantic import BaseSettings, PostgresDsn

class Settings(BaseSettings):
    database_url: PostgresDsn

@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    settings.database_url = getenv("DATABASE_URL")
    return settings