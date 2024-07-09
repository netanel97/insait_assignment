import os

from flask import jsonify

from src.dal.question_dal import QuestionDAL
from src.dal.answer_dal import AnswerDAL
import openai


class QuestionService:
    def __init__(self):
        self.question = QuestionDAL()
        self.answer = AnswerDAL()

    @staticmethod
    def get_gpt_response(question):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": question}],
                max_tokens=50
            )
            answer_text = response.choices[0].message['content'].strip()
            return {'answer': answer_text}
        except Exception as e:
            return {'error': f"Failed to get a response from OpenAI: {str(e)}"}

    def handle_question(self, question, answer_text):
        question_id = self.question.create_question(question)
        if isinstance(question_id, dict) and 'error' in question_id:
            return question_id

        answer_result = self.answer.create_answer(question_id, answer_text)
        if isinstance(answer_result, dict) and 'error' in answer_result:
            # If creating the answer fails, delete the created question to maintain consistency
            self.question.delete_question(question_id)
            return jsonify({'error': 'Internal Server Error'}), 500
        return {'answer': answer_text}

    def ask_question(self, question):
        gpt_response = self.get_gpt_response(question)
        if 'error' in gpt_response:
            return gpt_response, 500
        handle_response = self.handle_question(question, gpt_response['answer'])
        if 'error' in handle_response:
            return handle_response, 500

        return handle_response, 200
