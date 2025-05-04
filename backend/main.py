from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Event
from typing import List

app = FastAPI()

origins = [
    'http://localhost:5173',
    'http://127.0.0.1:5173'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'OPTIONS'],
    allow_headers=['*']
)


@app.get("/")
async def root():
    return {"message": "siemanko"}


@app.post("/api/cpm")
def post_cpm(events: List[Event]):
    print(events)
    return {"status": "ok"}
