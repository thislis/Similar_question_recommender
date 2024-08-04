from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from datetime import datetime

from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()


# Models
class Q_req(BaseModel):
    q_type: str
    question: str
    q_ans: str

class Question(BaseModel):
    q_type: str
    question: str
    q_ans: str

class Q_res(BaseModel):
    menus: List[Question]

# Controllers
class Question_Controller:
    def __init__(self, db: Session):
        self.db = db

    def set_question(self, request: Q_req):
        for menu_name in request.menus:
            question = models.Question(question_type=request.q_type, question=request.question, answer=request.q_ans)
            self.db.add(question)
        self.db.commit()

    def get_question(self):
