from typing import Optional
import os
import json
from pathlib import Path
from random import choice

from fastapi import FastAPI

app = FastAPI()

FOLDER_PATH = Path(__file__).parent

with open(FOLDER_PATH / "movies.json", "r") as f:
    MOVIES = json.loads(f.read())

@app.get("/movie")
async def get_movie():
    return {"movie": choice(MOVIES)}
