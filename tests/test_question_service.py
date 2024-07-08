import pytest
from app import create_app
from src.dal.database import db
from src.logic.question_service import QuestionService
from src.data.answer import Question
from datetime import datetime


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # Use the PostgreSQL database URI for testing
    database_uri = 'postgresql+psycopg2://postgres:123123@db/postgres'
    app = create_app(database_uri=database_uri)
    with app.app_context():
        db.create_all()  # Create all tables
        yield app
        db.drop_all()  # Drop all tables after test


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture
def question_service():
    """Provide a QuestionService instance for testing."""
    return QuestionService()


def test_ask_question(client, question_service):
    """Test asking a question through the /ask endpoint."""

    # Prepare test data
    question_data = {
        'question': 'How can I use SQLAlchemy with Flask?'
    }

    # Send POST request to /ask endpoint
    response = client.post('/ask/', json=question_data)

    # Assert the response status code is 200 OK
    assert response.status_code == 200

    # Assert the response contains 'question_id' if your endpoint returns it
    # assert 'question_id' in response.json
    #
    # # Optionally, you can assert more specific details about the response
    # # For example, if your endpoint returns a message
    # assert response.json['message'] == 'Question submitted successfully'
    #
    # # Optionally, you can also assert database state if needed
    # # For example, query the database using SQLAlchemy
    # questions = Question.query.all()
    # assert len(questions) == 1
