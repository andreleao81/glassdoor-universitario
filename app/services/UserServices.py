from ..models.CurriculumModel import CurriculumModel
from ..extensions import ma
from ..schemas.CurriculumSchema import CurriculumSchema
from ..models.UserModel import UserModel
from ..models.CollegeClassModel import CollegeClassModel
from flask import request, jsonify, json
from flask_restx import Api, Resource


def get_history_by_user_id(userid) -> CurriculumModel:
    """
    Get a user's history
    """
    history = CurriculumModel.query.filter(
        CurriculumModel.user_id == userid
    ).order_by(CurriculumModel.semester).all()

    return history

def create_history(data):
        history = CurriculumSchema().load(data)
        history.save()
        history_schema = CurriculumSchema().dump(history)
        return history_schema


def edit_history(userid, data):
    
    classCode = data['class_code']
    curriculum = CurriculumModel.query.filter(
        CurriculumModel.user_id == userid,
        CurriculumModel.class_code == classCode
    ).first()

    if not curriculum:
        return False

    
    schema = CurriculumSchema()
    curriculum = schema().load(data, instance=curriculum, partial=True)
    curriculum.save()


    response = schema().dump(curriculum)


    return response


# def get_history_by_user_id_done(user_id) -> CurriculumModel:
#     """
#     Get a user's done history
#     """
#     history = CurriculumModel.query.filter(
#         CurriculumModel.user_id == user_id,
#         CurriculumModel.conclusion == True
#     ).all().order_by(CurriculumModel.semester).asc()

#     return history

# def get_history_by_user_id_attending(user_id) -> CurriculumModel:
#     """
#     Get a user's attending history
#     """
#     history = CurriculumModel.query.filter(
#         CurriculumModel.user_id == user_id,
#         CurriculumModel.attending == True
#     ).all().order_by(CurriculumModel.semester).asc()

#     return history

