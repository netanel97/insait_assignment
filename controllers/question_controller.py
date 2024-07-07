from flask import Blueprint, request, jsonify
from logic.question_service import QuestionService

question_bp = Blueprint('question_controller', __name__)


@question_bp.route('/', methods=['POST'])
def ask_question():
    pass
