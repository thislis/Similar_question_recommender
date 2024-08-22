from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.ext.declarative import declarative_base

from src.database.database import engine

Base = declarative_base()

class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True, index=True)
    question_type = Column(String, index=True)
    question = Column(String, index=True)
    answer = Column(String, index=True)
    created_at = Column(DateTime, default=current_timestamp())

Base.metadata.create_all(bind=engine)
