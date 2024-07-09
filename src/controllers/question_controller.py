from flask import Blueprint, request, jsonify
from src.logic.question_service import QuestionService
import logging

question_bp = Blueprint('question_controller', __name__)
question_service = QuestionService()

# Create a logger for the question_controller module
logger = logging.getLogger(__name__)


@question_bp.route('', methods=['POST'])
async def ask_question():
    data = request.get_json()
    question_text = data.get('question')
    if not question_text:
        logger.error('No question text provided in the request')
        return jsonify({'error': 'Question text is required'}), 400
    logger.info(f"Received question: {question_text}")
    response, status_code = await question_service.ask_question(question_text)
    logger.info(f"Response: {response}, Status Code: {status_code}")
    return jsonify(response), status_code
