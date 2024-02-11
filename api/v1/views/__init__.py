#!/usr/bin/python3
from flask import Flask
from config import Config
from flask_cors import CORS
from api.v1.views.states import app_views as states_app_views

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    app.register_blueprint(states_app_views)
    return app
