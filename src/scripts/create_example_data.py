import logging

from utils import add_src_to_path

add_src_to_path()

from app import flask_app
from models.User import User

if __name__ == '__main__':
    logging.info("Create users")

    with flask_app.app_context():
        # Add a new user
        new_user = User.create_user(username='user1', password='user1')

        # Add another user
        another_user = User.create_user(username='user2', password='user2')
