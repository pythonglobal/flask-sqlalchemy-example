import logging

from flask import Flask

from models.database_handler import db

logging.basicConfig(level=logging.DEBUG)

flask_app = Flask(__name__)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/postgres'
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(flask_app)
