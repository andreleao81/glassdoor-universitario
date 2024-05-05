from flask import request, jsonify
from flask_restx import Api, Resource
from flask import Blueprint


from app.models.UserModel import UserModel
from ..schemas.UserSchema import UserSchema
from ..schemas.CurriculumSchema import CurriculumSchema
from ..services.UserServices import *

user_api = Blueprint('user_api', __name__)
api = Api(user_api)

@api.route('/user')
class UserCreateResource(Resource):
    def post(self):
        data = request.json
        user = UserSchema(**data)
        user.save()
        return jsonify(user), 201

@api.route('/user/<int:user_id>') 
class UserResource(Resource):
    def get(self, id):
        user = UserModel.query.get_or_404(id)
        user_schema = UserSchema().dump(user)
        return user_schema, 200

    def put(self, id):
        user = UserModel.query.get_or_404(id)
        data = request.json
        user.update(data)
        return jsonify(user), 200
    
    def delete(self, id):
        user = UserModel.query.get_or_404(id)
        user.delete()
        return '', 204

@api.route('/users')
class UserListResource(Resource):
    def get(self):
        users = UserModel.query.all()
        users_schema = UserSchema(many=True).dump(users)
        return users_schema, 200
    
@api.route('/user/<int:user_id>/history')
class UserHistoricResource(Resource):
    def get(self, id):
        history = get_history_by_user_id(id)

        if not history:
            return None, 404
        
        response = CurriculumSchema(many=True).dump(history)

        return response, 200