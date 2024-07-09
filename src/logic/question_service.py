import os

from flask import jsonify

from src.dal.question_dal import QuestionDAL
from src.dal.answer_dal import AnswerDAL
import openai
import logging


class QuestionService:
    def __init__(self):
        self.question = QuestionDAL()
        self.answer = AnswerDAL()
        self.logger = logging.getLogger(__name__)

    def get_gpt_response(self, question):
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
            self.logger.error(f"Failed to get a response from OpenAI: {str(e)}")
            return {'error': f"Failed to get a response from OpenAI: {str(e)}"}

    def handle_question(self, question, answer_text):
        question_id = self.question.create_question(question)
        if isinstance(question_id, dict) and 'error' in question_id:
            self.logger.error(f"Error creating question: {question_id['error']}")

            return question_id

        answer_result = self.answer.create_answer(question_id, answer_text)
        if isinstance(answer_result, dict) and 'error' in answer_result:
            self.logger.error(f"Error creating answer: {answer_result['error']}")
            self.question.delete_question(question_id)
            return jsonify({'error': 'Internal Server Error'}), 500
        return {'answer': answer_text}

    def ask_question(self, question):
        self.logger.info(f"Received question in ask_question function: {question}")

        gpt_response = self.get_gpt_response(question)
        if 'error' in gpt_response:
            return gpt_response, 500
        handle_response = self.handle_question(question, gpt_response['answer'])
        if 'error' in handle_response:
            return handle_response, 500
        self.logger.info(f"Question handled successfully: {question}")
        return handle_response, 200
