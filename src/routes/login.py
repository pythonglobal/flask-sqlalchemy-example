# GET endpoint to return a simple login HTML
from flask import render_template

from app import flask_app


@flask_app.route('/', methods=['GET'])
@flask_app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')
