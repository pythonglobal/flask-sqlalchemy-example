# GET endpoint to return a simple login HTML
from flask import render_template, request, jsonify

from app import flask_app
from models.UserToken import UserToken


# Simulated user data endpoint
@flask_app.route('/user', methods=['GET'])
def user():
    return render_template('user.html')


@flask_app.route('/user_data', methods=['GET'])
def user_data():
    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header.startswith('Bearer '):
        token = auth_header.split(' ')[1]
        user_token = UserToken.get_by_token(token=token)
        if user_token:
            return jsonify({'user': user_token.user.username})
    return jsonify({'error': 'Invalid or missing token'}), 401
