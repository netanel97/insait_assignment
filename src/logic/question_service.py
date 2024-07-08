import os

from src.dal.question_dal import QuestionDAL
from src.dal.answer_dal import AnswerDAL
import openai


class QuestionService:
    def __init__(self):
        self.question = QuestionDAL()
        self.answer = AnswerDAL()

    def ask_question(self, question):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}],
            max_tokens=50
        )
        question_id = self.question.create_question(question)

        answer_text = response.choices[0].message['content'].strip()
        self.answer.create_answer(question_id, answer_text)
        return {'answer': answer_text}
