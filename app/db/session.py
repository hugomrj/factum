from sqlalchemy.orm import sessionmaker, Session
from app.db.manager import get_engine


def get_session(cliente_id: str) -> Session:
    """
    Devuelve una sesión SQLAlchemy para un cliente.
    """
    engine = get_engine(cliente_id)
    SessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    )
    return SessionLocal()
