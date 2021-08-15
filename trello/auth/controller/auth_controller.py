from flask_restful import Resource

class AuthController(Resource):
    def __init__(self):
        pass

    def get(self):
        return "hi trello auth"