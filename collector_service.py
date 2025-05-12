from fastapi import FastAPI
import requests
from database import get_connection

app = FastAPI()

@app.get("/collect")
def collect_temperature():
    try:
        res = requests.get("http://temperature:8000/temperature")
        data = res.json()

        conn = get_connection()
        conn.execute("INSERT INTO readings (temperature) VALUES (?)", (data['temperature'],))
        conn.commit()
        conn.close()

        return {"stored": data}
    except Exception as e:
        return {"error": str(e)}
