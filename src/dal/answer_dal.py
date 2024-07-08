from src.dal.database import db
from src.data.answer import Answer


class AnswerDAL:
    @staticmethod
    def create_answer(question_id, answer_text):
        new_answer = Answer(question_id=question_id, answer=answer_text)
        db.session.add(new_answer)
        db.session.commit()
        return new_answer.id
