from flask_restx import Api, Resource, reqparse
from flask import Blueprint, request, abort


from app.models.CollegeClassModel import CollegeClassModel
from ..schemas.CollegeClassSchema import CollegeClassSchema

from app.models.ClassEvaluationModel import CollegeClassEvaluationModel
from ..schemas.ClassEvaluationSchema import CollegeClassEvaluationSchema
from app.services.ClassEvaluationServices import *


college_class_api = Blueprint('college_class_api', __name__)
api = Api(college_class_api)

# ----------------- CLASS -----------------

@api.route('/college_classes')
class CollegeClassListResource(Resource): #ok
    def get(self):
        college_classes = CollegeClassModel.query.order_by(CollegeClassModel.semester).all()
        return CollegeClassSchema(many=True).dump(college_classes), 200
    

    
# ----------------- EVALUATION -----------------


@api.route('/college_class/<string:class_id>/evaluations')
class CollegeClassEvaluationListResource(Resource): #ok 

    def get(self , class_id): 
        response = get_class_evals(class_id)
        return response, 200
    
@api.route('/college_class/evaluation')
class CollegeClassEvaluationCreateResource(Resource): #ok
    def post(self):
        data = request.get_json()

        if data is None:
            return data, 400
        try:
            schema = CollegeClassEvaluationSchema()
            eval = schema.load(data)
            eval.save()
            print('saved')
            eval.update_class()
            response = CollegeClassEvaluationSchema().dump(eval)
        except Exception as e:
            return {"Error": str(e)}, 400

        return response, 201
    
@api.route('/college_class/<string:class_id>/evaluation/<int:user_id>/<int:professor_id>') #ok
class CollegeClassEvaluationResource(Resource): #ok
    def get(self, class_id, user_id, professor_id):

        try:
            class_eval = get_class_eval(class_id, user_id, professor_id) 
            
            if class_eval is None:
                return None, 404
        except Exception as e:
            return {"Error": str(e)}, 400
        
        response = CollegeClassEvaluationSchema().dump(class_eval)
        return response, 200
        
    # def put(self,  class_id, user_id, professor_id):
    #     data = request.get_json()
    #     college_class_evaluation = CollegeClassEvaluationModel.query.get_or_404(evaluation_id)
    #     college_class_evaluation.update(data)
    #     return CollegeClassEvaluationSchema().dump(college_class_evaluation), 200

    # def delete(self, id, evaluation_id):
    #     college_class_evaluation = CollegeClassEvaluationModel.query.get_or_404(evaluation_id)
    #     college_class_evaluation.delete()
    #     return None, 204