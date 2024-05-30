from ..models.CurriculumModel import CurriculumModel
from ..extensions import ma
from ..schemas.CurriculumSchema import CurriculumSchema
from ..models.UserModel import UserModel
from ..models.CollegeClassModel import CollegeClassModel
from flask import request, jsonify, json
from flask_restx import Api, Resource

#region Curriculum

def create_history(data):
        history = CurriculumSchema().load(data)
        history.save()
        history_schema = CurriculumSchema().dump(history)
        return history_schema

def update_history(userid, data):
    
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

def get_history_by_user_id(user_id, concluded, attending) -> CurriculumModel:
    """
    Get a user's history
    """
    
    if not concluded and not attending:
        history = CurriculumModel.query.filter(
            CurriculumModel.user_id == user_id
        ).order_by(CurriculumModel.semester).all()

    if concluded:
        history = CurriculumModel.query.filter(
            CurriculumModel.user_id == user_id,
            CurriculumModel.conclusion == concluded
        ).order_by(CurriculumModel.semester).all()

    if attending:
        history = CurriculumModel.query.filter(
            CurriculumModel.user_id == user_id,
            CurriculumModel.attending == attending
        ).order_by(CurriculumModel.semester).all()

    # if not attending and not concluded:
    #     history = CurriculumModel.query.filter(
    #         CurriculumModel.user_id == user_id,
    #     ).order_by(CurriculumModel.semester).all()
        

    return history

#endregion