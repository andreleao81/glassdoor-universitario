from flask import Blueprint
from flask_restx import Api, Resource

from app.models.ProfessorEvaluation import ProfessorEvaluationModel
from ..schemas.ProfessorEvaluationSchema import ProfessorEvaluationSchema


professor_evaluation_api = Blueprint('professor_evaluation_api', __name__)
api = Api(professor_evaluation_api)

@api.route('/professor_evaluations')
class ProfessorEvaluationListResource(Resource):
    def get(self):
        professor_evaluations = ProfessorEvaluationModel.query.all()
        return ProfessorEvaluationSchema(many=True).dump(professor_evaluations)


