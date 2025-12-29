import sqlite3

def get_db(emisor: str):
    return sqlite3.connect(f"data/{emisor}.db")
