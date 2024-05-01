from flask import request, jsonify
from flask.views import MethodView
from flask_restx import Api, Resource

from app.models.UserModel import UserModel
from ..schemas.UserSchema import UserSchema
from flask import Blueprint

user_api = Blueprint('user_api', __name__)
api = Api(user_api)

@api.route('/user')
class CreateUser(Resource):
    def post(self):
        data = request.json
        user = UserSchema(**data)
        user.save()
        return jsonify(user), 201

@api.route('/users')
class GetUsers(Resource):
    def get(self):
        users = UserModel.query.all()
        users = UserSchema(many=True).dump(users)
        return users, 200