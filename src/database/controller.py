from sqlalchemy.orm import Session

from src.database.models import Question


def add_question(db: Session, question: Question, commit: bool = True):
    db.add(question)
    if commit:
        db.commit()
    return question

def get_question(db: Session, question_type: str):
    questions = db.query(Question).filter(Question.q_type == question_type).all()
    # if len(questions) == 0:
    #     raise HTTPException(status_code=404, detail="이건 없는데;;")
    # questions = [q for q in question] # ????
    return questions