from flask import Blueprint

from flask_restx import Api, Resource

from app.models.Professor import ProfessorModel
from ..schemas.ProfessorSchema import ProfessorSchema

professor_api = Blueprint('professor_api', __name__)
api = Api(professor_api)

@api.route('/professors')
class ProfessorListResource(Resource):
    def get(self):
        professors = ProfessorModel.query.all()
        return ProfessorSchema(many=True).dump(professors)
    

