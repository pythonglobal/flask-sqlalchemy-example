import logging
from models.database_handler import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"

    @classmethod
    def create_user(cls, username, password):
        try:
            user = cls(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return user
        except Exception as e:
            logging.exception(f'Error creating user: {e}')
            db.session.rollback()
            raise e
