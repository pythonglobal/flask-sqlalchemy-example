import uuid

from flask import request, jsonify
from models.User import User
from models.UserToken import UserToken
from app import flask_app


@flask_app.route('/generate_token', methods=['POST'])
def generate_token():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.get_by_username_and_password(username=username, password=password)
    if user:
        new_token = str(uuid.uuid4())

        existing_token = UserToken.get_by_user_id(user_id=user.id)
        if existing_token:
            existing_token.update_token(new_token)
        else:
            UserToken.create_token(token=new_token, user_id=user.id)

        return jsonify({'token': new_token}), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401


@flask_app.route('/check_token', methods=['POST'])
def check_token():
    data = request.get_json()
    token_str = data.get('token')
    user_token = UserToken.get_by_token(token=token_str)
    if user_token:
        return jsonify({'username': user_token.user.username}), 200
    else:
        return jsonify({'error': 'Invalid token'}), 401
