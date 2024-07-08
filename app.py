import os
from flask import Flask
from dal.database import db  # Import SQLAlchemySingleton instance
from controllers.question_controller import question_bp
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)  # Initialize SQLAlchemy with the app
    migrate = Migrate(app, db)

    with app.app_context():
        # Register blueprints
        app.register_blueprint(question_bp, url_prefix='/ask')

    return app


if __name__ == '__main__':
    flask_app = create_app()
    flask_app.run(debug=True, host="0.0.0.0")
