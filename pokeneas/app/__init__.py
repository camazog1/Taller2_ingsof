# app/__init__.py
import os
from flask import Flask
from app.routes import register_routes
from app.config import Config  

def create_app():
    template_dir = os.path.join(os.path.dirname(__file__), 'templates')
    app = Flask(__name__, template_folder=template_dir)

    app.config.from_object(Config)  

    register_routes(app)
    return app
