from fastapi import FastAPI, Depends
import json
from sqlalchemy.orm import Session
from pydantic import BaseModel

from src.database.database import SessionLocal, engine
from src.database import models
import src.database.controller as C

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
    return json.dumps({'message':'살려주세요, 분류 부분은 나중에 본가 가면 모델 학습 여러가지 돌려보고 만들게요'})

@app.post('/api/set/question')
def set_Q(request: C.Q_req, db: Session = Depends(get_db)):
    controller = C.Question_Controller(db)
    controller.set_question(request)

@app.get('/api/get/question/{q_type}', response_model=C.Q_res)
def get_Q(q_type: str, db: Session = Depends(get_db)):
    controller = C.Question_Controller(db)
    return controller.get_question(q_type)
