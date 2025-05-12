import sqlite3
import os

DB_PATH = "data/data.db"

def get_connection():
    os.makedirs("data", exist_ok=True)  # на всяк випадок
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temperature REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    return conn
