from flask import Blueprint, request
from flask_restx import Api, Resource

from app.models.ProfessorModel import ProfessorModel
from ..schemas.ProfessorSchema import ProfessorSchema

from app.models.ProfessorEvaluationModel import ProfessorEvaluationModel
from ..schemas.ProfessorEvaluationSchema import ProfessorEvaluationSchema


professor_api = Blueprint('professor_api', __name__)
api = Api(professor_api)

# ----------------- PROFESSOR -----------------

@api.route('/professors')
class ProfessorListResource(Resource):
    def get(self):
        professors = ProfessorModel.query.all()
        return ProfessorSchema(many=True).dump(professors)

# ----------------- EVALUATION -----------------

@api.route('/professor/<int:id>/evaluation/list')
class ProfessorEvaluationListResource(Resource):
    def get(self, id):
        professor_evaluations = ProfessorEvaluationModel.query.filter(ProfessorEvaluationModel.professor_id == id).all()
        return ProfessorEvaluationSchema(many=True).dump(professor_evaluations), 200
    
@api.route('/professor/<int:id>/evaluation/')
class ProfessorEvaluationCreateResource(Resource):
    def post(self):
        data = request.get_json()
        professor_evaluation = ProfessorEvaluationSchema().load(data)
        professor_evaluation.save()
        return ProfessorEvaluationSchema().dump(professor_evaluation), 201

@api.route('/professor/<int:id>/evaluation/<int:evaluation_id>')
class ProfessorEvaluationResource(Resource):
    def get(self, id, evaluation_id):
        professor_evaluation = ProfessorEvaluationModel.query.get_or_404(evaluation_id)
        return ProfessorEvaluationSchema().dump(professor_evaluation), 200
    
    def put(self, id, evaluation_id):
        data = request.get_json()
        professor_evaluation = ProfessorEvaluationModel.query.get_or_404(evaluation_id)
        professor_evaluation.update(data)
        return ProfessorEvaluationSchema().dump(professor_evaluation), 200

    def delete(self, id, evaluation_id):
        professor_evaluation = ProfessorEvaluationModel.query.get_or_404(evaluation_id)
        professor_evaluation.delete()
        return None, 204


