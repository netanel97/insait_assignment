# from sqlalchemy import Column, Integer, Text, DateTime
#
# from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.sql import func
# Base = declarative_base()
#
#
# class Question(Base):
#     __tablename__ = 'questions'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     question = Column(Text, nullable=False)
#     created_at = Column(DateTime, server_default=func.now())
#     answers = relationship("Answer", back_populates="question")
#
#
#
