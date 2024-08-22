from sqlalchemy.orm import Session

from src.database.models import Question


def add_question(db: Session, question: Question, commit: bool = True):
    db.add(question)
    if commit:
        db.commit()
    return question

def get_questions(db: Session, question_type: str):
    questions = db.query(Question).filter(Question.question_type == question_type).all()
    return questions