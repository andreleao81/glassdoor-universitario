from flask import request, jsonify, json
from flask_restx import Api, Resource
from flask import Blueprint

from app.models.UserModel import UserModel
from ..schemas.UserSchema import UserSchema
from ..schemas.CurriculumSchema import CurriculumSchema
from ..services.UserServices import *

from app.models.UserModel import UserModel
from ..schemas.UserSchema import UserSchema

user_api = Blueprint('user_api', __name__)
api = Api(user_api)


#region Cadastro e Login

@api.route('/cadastro')
class UserCreateResource(Resource):
    def post(self):
        print('inside post')
        data = request.get_json()
        user = UserSchema().load(data)
        user.save()
        user_schema = UserSchema().dump(user)
        return user_schema, 201
    
@api.route('/login')
class UserLoginResource(Resource):
    def post(self):
        data = request.get_json()
        user = UserModel.query.filter_by(username=data['username']).first()
        if user and user.check_password(data['password']):
            #né segredo
            return {'message': "Ceci n'est pas un token",
                    "user_id": user.id
                    }, 200 
        return {'message': 'Invalid credentials'}, 401
    
# endregion
    

# region User

@api.route('/user/<int:user_id>')
class UserResource(Resource):
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        user_schema = UserSchema().dump(user)
        return user_schema, 200

    # def put(self, user_id): 
    #     user = UserModel.query.get_or_404(id=user_id)
    #     data = request.json
    #     user.update(data)
    #     user_schema = UserSchema().dump(user)
    #     return user_schema, 200

    # not on swagger
    def delete(self, user_id):
        print('inside delete')
        user = UserModel.query.get_or_404(user_id)
        print(user)
        user.delete(user)
        return '', 204

@api.route('/users')
class UserListResource(Resource):
    def get(self):
        users = UserModel.query.all()
        users_schema = UserSchema(many=True).dump(users)
        return users_schema, 200

# endregion


# region User History
@api.route('/user/<int:user_id>/history')
class UserHistoricResource(Resource):
    def post(self):
        data = request.get_json()
        history = create_history(data)

        if not history:
            return jsonify({"message": "Curriculum not found"}), 404
        
        return history, 200

    def get(self, user_id):
        done_arg = request.args.get('done', '')

        try:
            concluded = validate_bool_arg(done_arg)
            if concluded is None: #get all
                history = get_history_by_user_id(user_id, concluded)

                if not history:
                    return None, 404
                
                response ={'Done': CurriculumSchema(many=True).dump(history[0]),
                           'NotDone': CurriculumSchema(many=True).dump(history[1])}
                return response, 200
            
            history = get_history_by_user_id(user_id, concluded)

            if not history:
                return None, 404
            
            response = CurriculumSchema(many=True).dump(history)
        except Exception as e:
            return jsonify({"message": str(e)}), 400

        return response, 200
    
    def put(self, user_id):
        data = request.get_json()
        response = update_history(user_id, data)

        if not response:
            return jsonify({"message": "Curriculum not found"}), 404
        
        return response, 200
        

# endregion


#region Validation
def validate_bool_arg(arg, **kwargs):
    param = arg.lower()
    
    if param == 'true':
        return True
    if param == 'false':
        return False
    if param == '':
        return None
    if not param:
        return None
    
    return TypeError('Invalid boolean argument')

#endregion