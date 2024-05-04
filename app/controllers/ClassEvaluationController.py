
from flask import Blueprint, jsonify
from flask_restx import Api, Resource

from app.models.ClassEvaluation import CollegeClassEvaluationModel
from ..schemas.ClassEvaluationSchema import CollegeClassEvaluationSchema


college_class_evaluation_api = Blueprint('college_class_evaluation_api', __name__)
api = Api(college_class_evaluation_api)

@api.route('/college_class_evaluations')
class CollegeClassEvaluationListResource(Resource):
    def get(self): # add pagination later
        college_class_evaluations = CollegeClassEvaluationModel.query.all()
        return CollegeClassEvaluationSchema(many=True).dump(college_class_evaluations)
    
@api.route('/college_class_evaluation')
class CollegeClassEvaluationResource(Resource):
    def post(self, request):
        data = request.json
        college_class_evaluation = CollegeClassEvaluationSchema(**data)
        college_class_evaluation.save()
        return jsonify(college_class_evaluation), 201