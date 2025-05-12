from fastapi import FastAPI
from database import get_connection

app = FastAPI()

@app.get("/readings")
def get_readings():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, temperature, timestamp FROM readings ORDER BY id DESC LIMIT 10")
    rows = cursor.fetchall()
    conn.close()

    return [
        {"id": row[0], "temperature": row[1], "timestamp": row[2]}
        for row in rows
    ]
