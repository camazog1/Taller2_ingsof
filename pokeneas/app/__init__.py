from flask import Flask
from .routes import register_routes
import os

def create_app():
    template_dir = os.path.join(os.path.dirname(__file__), 'templates')
    app = Flask(__name__, template_folder=template_dir)

    app.config.from_object('app.config.Config')

    register_routes(app)
    return app
