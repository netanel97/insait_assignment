# app.py

import os
from flask import Flask
from src.dal.database import db  # Import SQLAlchemySingleton instance
from src.controllers.question_controller import question_bp
from flask_migrate import Migrate
from dotenv import load_dotenv
import logging

load_dotenv()
app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_app():
    postgres_user = os.getenv('POSTGRES_USER')
    postgres_password = os.getenv('POSTGRES_PASSWORD')
    postgres_db = os.getenv('POSTGRES_DB')
    postgres_host = os.getenv('POSTGRES_HOST')
    postgres_port = os.getenv('POSTGRES_PORT')
    url = f"postgresql+psycopg2://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}"
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = url
    logger.info(f"Using database URI from environment variables")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)  # Initialize SQLAlchemy with the app
    logger.info("SQLAlchemy initialized with the Flask app")

    # Register blueprints if not already registered
    if not app.blueprints.get('question_controller'):
        app.register_blueprint(question_bp, url_prefix='/ask')
        logger.info("Blueprint 'question_controller' registered with prefix '/ask'")

    migrate = Migrate(app, db)

    return app


if __name__ == '__main__':
    flask_app = create_app()
    logger.info("Starting Flask app")
    flask_app.run(debug=True, host="0.0.0.0")
