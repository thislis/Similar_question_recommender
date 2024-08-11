from sqlalchemy import Column, Integer, String
from src.database.database import Base

class Menu(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True, index=True)
    question_type = Column(String, index=True)
    question = Column(String, index=True)
    answer = Column(String, index=True)