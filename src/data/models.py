from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

Base = declarative_base()


class Answer(Base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(Integer, ForeignKey('questions.id', ondelete='CASCADE'), nullable=False)
    answer = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    question = relationship("Question", back_populates="answers")


class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    question = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    answers = relationship("Answer", back_populates="question")
