from fastapi import FastAPI
import json

app = FastAPI()
data = json.load(open('udemyCourse.json'))

@app.get("/")
async def get_api():
    return data