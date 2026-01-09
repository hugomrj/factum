import os

DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

POOL_SIZE = int(os.getenv("DB_POOL_SIZE", 5))
MAX_OVERFLOW = int(os.getenv("DB_MAX_OVERFLOW", 10))
POOL_RECYCLE = int(os.getenv("DB_POOL_RECYCLE", 1800))
POOL_PRE_PING = True
