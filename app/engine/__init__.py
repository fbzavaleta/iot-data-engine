from flask import Flask
from engine.routes_config import load_routes

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    load_routes(app)
    return app
