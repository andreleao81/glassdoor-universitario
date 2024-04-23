@app.route('/users')
class CreateUser(Resource):
    def post(self):
        data = request.json
        user = User(**data)
        user.save()
        return user.to_json(), 201

@app.route('/users/<int:user_id>')
class GetUser(Resource):
    def get(self, user_id):
        user = User.objects.get(id=user_id)
        return user.to_json()