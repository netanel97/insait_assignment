from flask import Flask
from dal.database import db  # Import SQLAlchemySingleton instance



def create_app():
    app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123123@host.docker.internal:5432/postgres'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123123@postgres:5432/postgres'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)  # Initialize SQLAlchemy with the app
    with app.app_context():
        # Create database tables based on models
        db.create_all()
        # Register blueprints
        # app.register_blueprint(user_bp, url_prefix='/users')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host="0.0.0.0")
