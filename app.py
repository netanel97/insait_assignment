from flask import Flask
from dal.database import db  # Import SQLAlchemySingleton instance
from controllers.question_controller import question_bp
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:123123@db/postgres'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)  # Initialize SQLAlchemy with the app
    migrate = Migrate(app, db)

    with app.app_context():
        # Register blueprints
        app.register_blueprint(question_bp, url_prefix='/ask')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host="0.0.0.0")
