# app/db/admin.py
from sqlalchemy import create_engine, text
from app.db.config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

ADMIN_DB_URL = (
    f"postgresql+psycopg2://"
    f"{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/postgres"
)

admin_engine = create_engine(
    ADMIN_DB_URL,
    isolation_level="AUTOCOMMIT"
)


def create_emisor_database(cliente_id: str) -> dict:
    db_name = f"factum_{cliente_id}"

    with admin_engine.connect() as conn:
        existe = conn.execute(
            text(
                "SELECT 1 FROM pg_database WHERE datname = :dbname"
            ),
            {"dbname": db_name}
        ).scalar()

        if existe:
            return {
                "created": False,
                "message": f"La base de datos '{db_name}' ya existe"
            }

        conn.execute(text(f'CREATE DATABASE "{db_name}"'))

        return {
            "created": True,
            "message": f"Base de datos '{db_name}' creada correctamente"
        }
