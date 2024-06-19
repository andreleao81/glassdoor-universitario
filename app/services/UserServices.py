from ..models.CurriculumModel import CurriculumModel
from ..extensions import ma
from ..schemas.CurriculumSchema import CurriculumSchema, CompleteHistorySchema
from ..models.UserModel import UserModel
from ..models.CollegeClassModel import CollegeClassModel
from flask import request, jsonify, json
from flask_restx import Api, Resource
from sqlalchemy import and_
from ..extensions import db

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



#endregion

# region Auxiliary


def get_complete_history(userId, conclusion=None):
    # Perform a left join between CurriculumModel and CollegeClassModel
    complete_history = db.session.query(
        CurriculumModel.user_id,
        CollegeClassModel.class_code,
        CurriculumModel.conclusion_semester,
        CollegeClassModel.default_semester,
        CurriculumModel.conclusion,
        CollegeClassModel.name,
        CollegeClassModel.rating
    ).outerjoin(
        CollegeClassModel,
        CurriculumModel.class_code == CollegeClassModel.class_code
    ).filter(CurriculumModel.user_id == userId
    ).order_by(CollegeClassModel.default_semester
    ).all()

    # print('complete_history:', complete_history)
    # print('user_id:', user_id)
    # print('\n\n')

    # Format the result as a list of dictionaries for easier manipulation
    complete_history = [
        {
            'user_id': record[0],
            'class_code': record[1],
            'conclusion_semester': record[2],
            'default_semester': record[3],
            'conclusion': record[4],
            'name': record[5],
            'rating': record[6]
        }
        for record in complete_history
    ]

    schema = CompleteHistorySchema()
    complete_history = schema.dump(complete_history, many=True)
    # Separate the complete history into historyDone and historyNotDone
    historyDone = [record for record in complete_history if record['conclusion'] is True]
    historyNotDone = [record for record in complete_history if record['conclusion'] is False]

    historyDone = sorted(historyDone, key=lambda x: x['conclusion_semester'])

    return historyDone, historyNotDone

# endregion