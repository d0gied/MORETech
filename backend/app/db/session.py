from functools import lru_cache
from typing import Generator
from ..config import get_settings
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import scoped_session, sessionmaker

@lru_cache
def get_engine() -> Engine:
    engine = create_engine(get_settings().database_url, pool_pre_ping=True)
    return engine


@lru_cache
def create_session() -> scoped_session:
    Session = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=get_engine())
    )
    return Session

def get_session() -> Generator[scoped_session, None, None]:
    Session = create_session()
    try:
        yield Session
    finally:
        Session.remove()
