import logging
from sqlalchemy import event

from models.database_handler import db


class UserToken(db.Model):
    __tablename__ = 'user_tokens'

    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(128), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Establish relationship back to User
    user = db.relationship('User', back_populates='token')

    def __repr__(self):
        return f"<UserToken(id={self.id}, token='{self.token}')>"

    @classmethod
    def create_token(cls, token, user_id):
        try:
            user_token = cls(token=token, user_id=user_id)
            db.session.add(user_token)
            db.session.commit()
            return user_token
        except Exception as e:
            logging.exception(f'Error creating token: {e}')
            db.session.rollback()
            raise e

    def update_token(self, new_token):
        try:
            self.token = new_token
            db.session.commit()
            return self
        except Exception as e:
            logging.exception(f'Error updating token: {e}')
            db.session.rollback()
            raise e

    @classmethod
    def __declare_last__(cls):
        event.listen(cls, 'after_insert', cls.token_added)
        event.listen(cls, 'after_update', cls.token_updated)

    @staticmethod
    def token_updated(mapper, connection, target):
        logging.debug(f"Token for user {target.user.username} has been updated to {target.token}")

    @staticmethod
    def token_added(mapper, connection, target):
        logging.debug(f"New token '{target.token}' added for user_id {target.user_id}")
