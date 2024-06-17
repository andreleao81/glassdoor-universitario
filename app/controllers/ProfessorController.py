from flask import Blueprint, request
from flask_restx import Api, Resource

from app.models.ProfessorModel import ProfessorModel
from ..schemas.ProfessorSchema import ProfessorSchema

from app.models.ProfessorEvaluationModel import ProfessorEvaluationModel
from ..schemas.ProfessorEvaluationSchema import ProfessorEvaluationSchema, ProfessorEvaluationPostSchema

from app.services.ProfessorServices import *


# ----------------- API -----------------


professor_api = Blueprint('professor_api', __name__)
api = Api(professor_api)

# ----------------- PROFESSOR -----------------

@api.route('/professors')
class ProfessorListResource(Resource):
    def get(self):
        professors = ProfessorModel.query.order_by(ProfessorModel.name).all()
        return ProfessorSchema(many=True, exclude=(['professor_evaluations'])).dump(professors)

# ----------------- EVALUATION -----------------

@api.route('/professor/<int:prof_id>/evaluations')
class ProfessorEvaluationListResource(Resource):
    def get(self, prof_id):
        professor_evaluations = ProfessorEvaluationModel.query.filter(ProfessorEvaluationModel.professor_id == prof_id).all()
        return ProfessorEvaluationSchema(many=True).dump(professor_evaluations), 200
    
@api.route('/professor/evaluation')
class ProfessorEvaluationCreateResource(Resource):
    def post(self):
        data = request.get_json()
        professor_evaluation = ProfessorEvaluationPostSchema().load(data)
        professor_evaluation.save()
        return ProfessorEvaluationSchema().dump(professor_evaluation), 201

@api.route('/professor/<int:prof_id>/evaluation/<string:class_id>/<int:user_id>')
class ProfessorEvaluationResource(Resource):

    def get(self, prof_id, user_id ,class_id):
        professor_evaluation = get_professor_eval(prof_id, user_id, class_id)

        if professor_evaluation is None:
            return None, 404
        
        response = ProfessorEvaluationSchema().dump(professor_evaluation)
        return response, 200
    
    # def put(self, id, evaluation_id):
    #     data = request.get_json()
    #     professor_evaluation = ProfessorEvaluationModel.query.get_or_404(evaluation_id)
    #     professor_evaluation.update(data)
    #     return ProfessorEvaluationSchema().dump(professor_evaluation), 200

    # def delete(self, id, evaluation_id):
    #     professor_evaluation = ProfessorEvaluationModel.query.get_or_404(evaluation_id)
    #     professor_evaluation.delete()
    #     return None, 204


