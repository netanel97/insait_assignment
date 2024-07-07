from dal.question_dal import QuestionDAL
from dal.answer_dal import AnswerDAL
# import openai
import os
class QuestionService:
    @staticmethod
    def ask_question(question_text):
        # Save the question to the database
        question_id = QuestionDAL.create_question(question_text)

        # Send the question to OpenAI API and get the answer

        # openai.api_key = os.getenv('OPENAI_API_KEY')
        # response = openai.Completion.create(
        #     engine="text-davinci-003",
        #     prompt=question_text,
        #     max_tokens=50
        # )
        # answer_text = response.choices[0].text.strip()

        # Save the answer to the database
        # AnswerDAL.create_answer(question_id, answer_text)
        return ""
        # return {'question': question_text, 'answer': answer_text}



