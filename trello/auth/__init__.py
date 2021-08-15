from flask import Blueprint
from flask_restful import Api

from trello.auth.controller.auth_controller import AuthController

trello_auth_blueprint = Blueprint('trello_auth', __name__, url_prefix='/auth')
trello_auth = Api(trello_auth_blueprint)

trello_auth.add_resource(AuthController, '')
