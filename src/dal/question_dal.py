from src.dal.database import db
from src.data.models import Question


class QuestionDAL:
    @staticmethod
    def create_question(question_text):
        try:
            new_question = Question(question=question_text)
            db.session.add(new_question)
            db.session.commit()
            return new_question.id
        except Exception as e:
            db.session.rollback()
            return {'error': f"Failed to create question: {str(e)}"}

    @staticmethod
    def delete_question(question_id):
        try:
            question = db.session.query(Question).get(question_id)
            if question:
                db.session.delete(question)
                db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {'error': f"Failed to delete question: {str(e)}"}
