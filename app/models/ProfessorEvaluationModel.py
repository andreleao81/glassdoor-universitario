from app.extensions import db
from .BaseModel import BaseModel
from .ProfessorModel import ProfessorModel
from .UserModel import UserModel
from .CollegeClassModel import CollegeClassModel



class ProfessorEvaluationModel(BaseModel):
    __tablename__='professor_evaluations'
    id = db.Column(db.Integer, primary_key=True)
    
    semester = db.Column(db.Integer, nullable=False)
    
    attendance = db.Column(db.Integer, nullable=False)
    punctuality = db.Column(db.Integer, nullable=False)
    availability_questions = db.Column(db.Integer, nullable=False)
    student_relationship = db.Column(db.Integer, nullable=False)
    professor_methodology = db.Column(db.Integer, nullable=False)
   
    class_code = db.Column(db.String(10), db.ForeignKey('college_classes.class_code'), nullable=False, index=True)
    college_class = db.Relationship(CollegeClassModel, backref='professor_evaluations') 
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    user = db.Relationship(UserModel, backref='professor_evaluations')
    
    professor_id = db.Column(db.Integer, db.ForeignKey('professors.id'), nullable=False, index=True)
    professor = db.Relationship(ProfessorModel, backref='professor_evaluations')




    