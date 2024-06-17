from app.extensions import db
from .BaseModel import BaseModel
from .ProfessorModel import ProfessorModel
from .UserModel import UserModel
from .CollegeClassModel import CollegeClassModel
from ..extensions import db
from sqlalchemy import event



class ProfessorEvaluationModel(BaseModel):
    __tablename__='professor_evaluations'
    id = db.Column(db.Integer, primary_key=True)
    
    semester = db.Column(db.Integer, nullable=False)
    
    attendance = db.Column(db.Boolean, default=False, nullable=False)

    punctuality = db.Column(db.Integer, nullable=False)
    availability_questions = db.Column(db.Integer, nullable=False)
    student_relationship = db.Column(db.Integer, nullable=False)
    professor_methodology = db.Column(db.Integer, nullable=False)

    individual_rating = db.Column(db.Integer, nullable=False)
   
    class_code = db.Column(db.String(10), db.ForeignKey('college_classes.class_code'), nullable=False, index=True)
    college_class = db.Relationship(CollegeClassModel, backref='professor_evaluations') 
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    user = db.Relationship(UserModel, backref='professor_evaluations')
    
    professor_id = db.Column(db.Integer, db.ForeignKey('professors.id'), nullable=False, index=True)
    professor = db.Relationship(ProfessorModel, backref='professor_evaluations')

    def update_prof(self):
        """
        Update professor model after an insert or update
        """

        evaluations = ProfessorEvaluationModel.query.filter_by(professor_id=self.professor_id).all()
        total_scores = 0
        if evaluations:
            # Extract ratings using zip and calculate the total sum using map and sum
            total_scores = sum(
                            map(
                                sum, zip(
                                    *[(eval.punctuality, eval.availability_questions,
                                            eval.student_relationship, eval.professor_methodology,
                                            eval.individual_rating*3 if eval.individual_rating else 0)
                                                for eval in evaluations
                                    ]
                                )
                            )
                        )
        

        last_eval = ProfessorEvaluationModel.query.filter_by(professor_id=self.professor_id).order_by(ProfessorEvaluationModel.update_time.desc()).first()
        if last_eval:
            total_possible = len(evaluations) * (4*5 +3*5)
            new_rating = total_scores / total_possible
            self.professor.rating = round(new_rating, 2)
            self.professor.attendance = last_eval.attendance
            db.session.commit()
            return

    