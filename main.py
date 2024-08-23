# TODO : import의 순서는 다음과 같이 하면 좋아요.
# 1. 표준 라이브러리
# 2. 서드파티 라이브러리
# 3. 내가 만든 라이브러리

# TODO : endpoint가 엄청많이 늘어나면 이 파일이 복잡해질거에요.
# endpoint를 그룹별로 어떻게 묶을까요?

import json
from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database.database import get_db
from src.schema.schema import QuestionRequestDto, QuestionDto
from src.database.controller import add_question, get_questions
from src.database.models import Question


app = FastAPI()

@app.get('/')
def hello():
    # TODO : 헉
    return json.dumps({'message':'살려주세요, 분류 부분은 나중에 본가 가면 모델 학습 여러가지 돌려보고 만들게요'})


@app.post('/api/set/question')
def set_question(request: QuestionRequestDto, db: Session = Depends(get_db)):
    # TODO : 이 model 객체는 controller안에서 만드는게 좋을까요? 아니면 여기다가 만드는게 좋을까요?
    question = Question(question_type=request.question_type, question=request.question, answer=request.question_answer)
    add_question(db=db, question=question)

@app.get('/api/get/question/{question_type}', response_model=List[QuestionDto])
def get_question(question_type: str, db: Session = Depends(get_db)):
    questions =  get_questions(db=db, question_type=question_type)
    if len(questions) == 0:
        raise HTTPException(status_code=404, detail="이건 없는데;;")
    
    # # unserialize
    # # TODO : unserialize은 controller에서 하는게 좋을까요? 아니면 여기서 하는게 좋을까요?
    questions = [QuestionDto(question_type=question.question_type, question=question.question, question_answer=question.answer) for question in questions]
    return questions


if __name__ == "__main__":
    app.debug = True
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)