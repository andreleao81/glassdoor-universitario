from ..extensions import db
from ..utils.DateTime import dateTime
from ..models import BaseModel


class CollegeClassModel(BaseModel):
    __tablename__='class_evaluations'
    id = db.Column(db.Integer, primary_key=True)
    semester = db.Column(db.Integer, nullable=False)

    lesson_exam_alingment = db.Column(db.Integer, nullable=False)
    curriculum_exam_alingment = db.Column(db.Integer, nullable=False)
    difficulty = db.Column(db.Integer, nullable=False)

    class_code = db.Relationsip('CollegeClass', backref='class_evaluations')
    user_id = db.Relationship('User', backref='class_evaluations')
    professor_id = db.Relationship('Professor', backref='class_evaluations')