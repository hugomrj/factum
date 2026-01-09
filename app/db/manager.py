from sqlalchemy import create_engine

from threading import Lock
from app.db.config import (
    DB_USER, DB_PASSWORD, DB_HOST, DB_PORT,
    POOL_SIZE, MAX_OVERFLOW, POOL_RECYCLE, POOL_PRE_PING
)

_engines: dict[str, any] = {}
_lock = Lock()


def build_db_url(cliente_id: str) -> str:
    db_name = f"factum_{cliente_id}"
    return (
        f"postgresql+psycopg2://"
        f"{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{db_name}"
    )


def get_engine(cliente_id: str):
    with _lock:
        if cliente_id not in _engines:
            _engines[cliente_id] = create_engine(
                build_db_url(cliente_id),
                pool_size=POOL_SIZE,
                max_overflow=MAX_OVERFLOW,
                pool_recycle=POOL_RECYCLE,
                pool_pre_ping=POOL_PRE_PING,
            )

        return _engines[cliente_id]
