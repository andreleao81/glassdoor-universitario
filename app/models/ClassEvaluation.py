from app.extensions import db
from ..utils.DateTime import dateTime
from .BaseModel import BaseModel


class CollegeClassEvaluationModel(BaseModel):
    __tablename__='class_evaluations'
    
    id = db.Column(db.Integer, primary_key=True)
    
    semester = db.Column(db.Integer, nullable=False)

    lesson_exam_alingment = db.Column(db.Integer, nullable=False)
    curriculum_exam_alingment = db.Column(db.Integer, nullable=False)
    difficulty = db.Column(db.Integer, nullable=False)

    class_code = db.Column(db.String(10), db.ForeignKey('college_classes.class_code'), nullable=False)
    college_class = db.Relationship('CollegeClassModel', backref='class_evaluations') 
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.Relationship('UserModel', backref='class_evaluations')
    
    professor_id = db.Column(db.Integer, db.ForeignKey('professors.id'), nullable=False)
    professor = db.Relationship('ProfessorModel', backref='class_evaluations')