from flask import Blueprint, request, jsonify
from src.logic.question_service import QuestionService

question_bp = Blueprint('question_controller', __name__)
question_service = QuestionService()


@question_bp.route('', methods=['POST'])
def ask_question():
    data = request.get_json()
    question_text = data.get('question')
    if not question_text:
        return jsonify({'error': 'Question text is required'}), 400

    response = question_service.ask_question(question_text)
    return jsonify(response), 200
