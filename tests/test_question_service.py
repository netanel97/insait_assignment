import unittest
import requests_mock
from app import app


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_question_service(self):
        with requests_mock.mock() as mock:
            question_data = {
                'question': 'How can I use SQLAlchemy with Flask?'
            }
            mock.post('/ask', json=question_data)


if __name__ == '__main__':
    unittest.main()
