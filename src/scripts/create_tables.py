from app import flask_app
from models.database_handler import db


if __name__ == '__main__':
    with flask_app.app_context():
        db.create_all()
