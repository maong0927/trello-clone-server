from flask import Flask

from trello.auth import trello_auth_blueprint
from trello.main import trello_blueprint

def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    return app

def register_blueprints(app: Flask) -> None:
    apis = (trello_blueprint, trello_auth_blueprint)

    for _api in apis:
        app.register_blueprint(_api)


