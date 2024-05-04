# from flask import request, jsonify
# from flask.views import MethodView

from flask_restx import Api, Resource
from app.models.CollegeClassModel import CollegeClassModel
from ..schemas.CollegeClassSchema import CollegeClassSchema
from flask import Blueprint

college_class_api = Blueprint('college_class_api', __name__)
api = Api(college_class_api)

@api.route('/college_classes')
class CollegeClassListResource(Resource):
    def get(self):
        college_classes = CollegeClassModel.query.all()
        return CollegeClassSchema(many=True).dump(college_classes)