# import datetime
# import json

# from ..extensions import db
# from ..utils.DateTime import dateTime
# from BaseModel import BaseModel


# class ProfessorEvaluationModel(BaseModel):
#     __tablename__='teacher_evaluations'
#     id = db.Column(db.Integer, primary_key=True)
#     semester = db.Column(db.Integer, nullable=False)
#     attendance = db.Column(db.Integer, nullable=False)
#     punctuality = db.Column(db.Integer, nullable=False)
#     availability_questions = db.Column(db.Integer, nullable=False)
#     student_relationship = db.Column(db.Integer, nullable=False)
#     professor_methodology = db.Column(db.Integer, nullable=False)
   
#     class_code = db.Relationship('CollegeClass', backref='teacher_evaluations')

from ..models.ProfessorEvaluation import ProfessorEvaluationModel
from ..extensions import ma

class ProfessorEvaluationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProfessorEvaluationModel
        load_instance = True
        include_fk = True
        include_relationships = True
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only=True)
    
    semester = ma.Integer(required=True)
    
    attendance = ma.Integer(required=True)
    punctuality = ma.Integer(required=True)
    availability_questions = ma.Integer(required=True)
    student_relationship = ma.Integer(required=True)
    professor_methodology = ma.Integer(required=True)

    class_code = ma.String(required=True)
    user_id = ma.Integer(required=True)
    professor_id = ma.Integer(required=True)






    