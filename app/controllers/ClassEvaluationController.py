
from flask import Blueprint, jsonify, request
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
    print("Hello")

    def post(self):
        print("Hello2")
        data = request.get_json()
        college_class_evaluation = CollegeClassEvaluationSchema().load(data)
        college_class_evaluation.save()
        return CollegeClassEvaluationSchema().dump(college_class_evaluation), 201