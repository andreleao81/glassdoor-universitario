from flask import request, jsonify
from flask.views import MethodView

from app.models.UserModel import UserModel
from flask import Blueprint


#@app.route('/users')
class CreateUser(MethodView):
    def post(self):
        data = request.json
        user = UserModel(**data)
        user.save()
        return jsonify(user), 201

#@app.route('/users/<int:user_id>')
class GetUser(MethodView):
    def get(self, user_id):
        user = UserModel.objects.get(id=user_id)
        return jsonify(user), 200
    
#@app.route('/users/mengao')
class GetMengao(MethodView):
    def get(self):
        return jsonify({'mengao': 'mengao'}), 200  



user_api = Blueprint('user_api', __name__)

user_api.add_url_rule(
    '/users/<int:user_id>', view_func=GetUser.as_view('get_user'), methods=['GET']
)

user_api.add_url_rule(
    '/users', view_func=CreateUser.as_view('create_user'), methods=['POST']
)

user_api.add_url_rule(
    '/users/mengao', view_func=GetMengao.as_view('get_mengao'), methods=['GET']
)