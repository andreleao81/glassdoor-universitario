import datetime
import json

from ..extensions import db
from ..utils.DateTime import dateTime
from BaseModel import BaseModel


class ProfessorEvaluationModel(BaseModel):
    __tablename__='teacher_evaluations'
    id = db.Column(db.Integer, primary_key=True)
    semester = db.Column(db.Integer, nullable=False)
    attendance = db.Column(db.Integer, nullable=False)
    punctuality = db.Column(db.Integer, nullable=False)
    availability_questions = db.Column(db.Integer, nullable=False)
    student_relationship = db.Column(db.Integer, nullable=False)
    professor_methodology = db.Column(db.Integer, nullable=False)
   
    class_code = db.Relationship('CollegeClass', backref='teacher_evaluations')





    