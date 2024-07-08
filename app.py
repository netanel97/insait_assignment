# app.py

import os
from flask import Flask
from src.dal.database import db  # Import SQLAlchemySingleton instance
from src.controllers.question_controller import question_bp
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


def create_app(database_uri=None):
    if database_uri:
        app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    else:
        postgres_user = os.getenv('POSTGRES_USER')
        postgres_password = os.getenv('POSTGRES_PASSWORD')
        postgres_db = os.getenv('POSTGRES_DB')
        postgres_host = os.getenv('POSTGRES_HOST')
        postgres_port = os.getenv('POSTGRES_PORT')
        app.config[
            'SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}"

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)  # Initialize SQLAlchemy with the app

    # Register blueprints if not already registered
    if not app.blueprints.get('question_controller'):
        app.register_blueprint(question_bp, url_prefix='/ask')

    migrate = Migrate(app, db)

    return app


if __name__ == '__main__':
    flask_app = create_app()
    flask_app.run(debug=True, host="0.0.0.0")
