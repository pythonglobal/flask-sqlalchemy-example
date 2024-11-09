import logging
import uuid

from models.UserToken import UserToken
from utils import add_src_to_path

add_src_to_path()

from app import flask_app
from models.User import User

if __name__ == '__main__':
    logging.info("Create users")

    with flask_app.app_context():
        # Add a new user
        new_user = User.create_user(username='user1', password='user1')

        if not new_user:
            new_user = User.get_user_by_username(username='user1')

        # Add a token for the new user
        user_token = UserToken.create_token(token=str(uuid.uuid4()), user_id=new_user.id)

        # Add another user
        another_user = User.create_user(username='user2', password='user2')

        if not another_user:
            another_user = User.get_user_by_username(username='user2')

        another_token = UserToken.create_token(token="token", user_id=another_user.id)
        another_token.update_token(new_token=str(uuid.uuid4()))
