from dal.question_dal import QuestionDAL
from dal.answer_dal import AnswerDAL
import openai

import os


class QuestionService:
    def __init__(self):
        self.question = QuestionDAL()
        self.answer = AnswerDAL()

    def ask_question(self, question):
        #  Save the question to the database and return it
        question_id = self.question.create_question(question)
        self.answer.create_answer(question_id, "hello world")
        return "hello world"


