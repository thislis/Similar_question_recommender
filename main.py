from fastapi import FastAPI
import json
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel

from src.database.database import SessionLocal, engine
from src.database import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()

@app.get('/')
def hello():
    return json.dumps({'message':'살려줘요'})