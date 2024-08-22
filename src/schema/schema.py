from typing import List, Any

from pydantic import BaseModel

class QuestionDto(BaseModel):
    question_type: str
    question: str
    question_answer: str

class QuestionRequestDto(BaseModel):
    question_type: str
    question: str
    question_answer: str

