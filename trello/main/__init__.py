from flask import Blueprint
from flask_restful import Api

from trello.main.controller import MainController

trello_blueprint = Blueprint('trello', __name__, url_prefix='/')
trello_auth = Api(trello_blueprint)

trello_auth.add_resource(MainController, '')
