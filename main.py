from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def home():
    return {"message": "GamerVault API is Running! 🚀"}

@app.get("/check")
def check_id(id: str):
    url = f"https://id.freefireinfo.site/api/info/{id}"
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            data = r.json()
            return {"status": "success", "nickname": data.get('nickname'), "id": id}
        return {"status": "error", "message": "ID not found"}
    except:
        return {"status": "error", "message": "Timeout"}
