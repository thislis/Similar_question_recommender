from typing import List

from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from src.database import models


class Q_req(BaseModel):
    q_type: str
    question: str
    q_ans: str

class Question(BaseModel):
    q_type: str
    question: str
    q_ans: str

class Q_res(BaseModel):
    questions: List[Question]

# Controllers
class Question_Controller:
    def __init__(self, db: Session):
        self.db = db

    def set_question(self, request: Q_req):
        for q in request.questions:
            question = models.Question(question_type=request.q_type, question=request.question, answer=request.q_ans)
            self.db.add(question)
        self.db.commit()

    def get_question(self, Q_type: str):
        question = self.db.query(models.Question).filter(models.Question.q_type == Q_type).all()
        if not question:
            raise HTTPException(status_code=404, detail="이건 없는데;;")
        Questions = [q for q in question]
        return Q_res(question=Questions)