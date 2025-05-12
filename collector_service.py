from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/collect")
def collect_temperature():
    try:
        res = requests.get("http://temperature:8000/temperature")
        data = res.json()
        with open("log.txt", "a") as f:
            f.write(f"{data}\n")
        return {"received": data}
    except Exception as e:
        return {"error": str(e)}
