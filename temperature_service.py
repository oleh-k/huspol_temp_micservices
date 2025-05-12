# temperature_service.py
from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/temperature")
def read_temperature():
    return {"temperature": round(random.uniform(15.0, 30.0), 2)}
