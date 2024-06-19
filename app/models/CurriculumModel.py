
from app import db

from .CollegeClassModel import CollegeClassModel
from .BaseModel import BaseModel

#later curriculum can be a job running at each new insertion of a class_evaluation

class CurriculumModel(BaseModel):
    __tablename__ = 'classes_history'

    id = db.Column(db.Integer, primary_key=True)
    conclusion_semester = db.Column(db.Integer, nullable=True)
    conclusion = db.Column(db.Boolean, nullable=False)
    class_code = db.Column(db.String(10), db.ForeignKey('college_classes.class_code'), nullable=False, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    
    college_class = db.relationship(CollegeClassModel, backref='history')

    @property
    def user(self):
        from .UserModel import UserModel
        return db.relationship(UserModel, backref='history')

   
    def validate_semester(self):
        if self.semester != None:
            if self.semester < 1:
                raise ValueError('Semester must be greater than 0')
            if self.semester > 20:
                raise ValueError('Semester must be less than 20')
            
