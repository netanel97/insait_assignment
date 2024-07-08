from src.dal.question_dal import QuestionDAL
from src.dal.answer_dal import AnswerDAL


class QuestionService:
    def __init__(self):
        self.question = QuestionDAL()
        self.answer = AnswerDAL()

    def ask_question(self, question):
        #  Save the question to the database and return it
        question_id = self.question.create_question(question)
        self.answer.create_answer(question_id, "hello world")
        return "hello world"


