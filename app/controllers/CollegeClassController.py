from flask_restx import Api, Resource
from flask import Blueprint, request

from app.models.CollegeClassModel import CollegeClassModel
from ..schemas.CollegeClassSchema import CollegeClassSchema

from app.models.ClassEvaluationModel import CollegeClassEvaluationModel
from ..schemas.ClassEvaluationSchema import CollegeClassEvaluationSchema
from app.services.ClassEvaluationServices import *


college_class_api = Blueprint('college_class_api', __name__)
api = Api(college_class_api)

@api.route('/college_class/list')
class CollegeClassListResource(Resource):
    def get(self):
        college_classes = CollegeClassModel.query.all()
        return CollegeClassSchema(many=True).dump(college_classes), 200
    

    
# ----------------- EVALUATION -----------------


@api.route('/college_class/<int:class_id>/evaluation/list')
class CollegeClassEvaluationListResource(Resource):

    def get(self, class_id): # add pagination later
        response = get_class_evals(class_id)
        return response, 200
    

@api.route('/college_class/<int:class_id>/evaluation/<int:user_id>')
class CollegeClassEvaluationResource(Resource):

    def post(self, user_id, class_id, professor_id):
        response = create_class_eval(request.get_json(), class_id, user_id, professor_id)
        return response, 201
    
    def get(self, class_id, user_id, professor_id):
        response = get_class_eval(class_id, user_id, professor_id) 
        
        if response is None:
            return None, 404
        
        return response, 200
        
    def put(self, id, evaluation_id):
        data = request.get_json()
        college_class_evaluation = CollegeClassEvaluationModel.query.get_or_404(evaluation_id)
        college_class_evaluation.update(data)
        return CollegeClassEvaluationSchema().dump(college_class_evaluation), 200

    def delete(self, id, evaluation_id):
        college_class_evaluation = CollegeClassEvaluationModel.query.get_or_404(evaluation_id)
        college_class_evaluation.delete()
        return None, 204