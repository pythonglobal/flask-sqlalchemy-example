import logging

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import relationship

from models.database_handler import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    # Establish one-to-one relationship with UserToken
    token = relationship('UserToken', uselist=False, back_populates='user')

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"

    @classmethod
    def get_user_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def create_user(cls, username, password):
        try:
            user = cls(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return user
        except IntegrityError:
            db.session.rollback()
            logging.error(f'User with username {username} already exists')
            return None
        except Exception as e:
            logging.exception(f'Error creating user: {e}')
            db.session.rollback()
            raise e
