from src.dal.database import db
from src.data.models import Question


class QuestionDAL:
    @staticmethod
    def create_question(question_text):
        new_question = Question(question=question_text)
        db.session.add(new_question)
        db.session.commit()
        return new_question.id
