from sqlalchemy.orm import declarative_base, DeclarativeBase
from functools import lru_cache


@lru_cache
def get_base() -> DeclarativeBase:
    base = declarative_base()
    return base
