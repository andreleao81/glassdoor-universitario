from app.extensions import db
from .BaseModel import BaseModel
from .ProfessorModel import ProfessorModel
from .UserModel import UserModel
from .CollegeClassModel import CollegeClassModel



class CollegeClassEvaluationModel(BaseModel):
    __tablename__='class_evaluations'
    
    id = db.Column(db.Integer, primary_key=True)
    
    semester_concluded = db.Column(db.Integer, nullable=True)

    lesson_exam_alingment = db.Column(db.Integer, nullable=False)
    curriculum_exam_alingment = db.Column(db.Integer, nullable=False)
    difficulty = db.Column(db.Integer, nullable=False)

    class_code = db.Column(db.String(10), db.ForeignKey('college_classes.class_code'), nullable=False, index=True)
    college_class = db.Relationship(CollegeClassModel, backref='class_evaluations') 
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    user = db.Relationship(UserModel, backref='class_evaluations')
    
    professor_id = db.Column(db.Integer, db.ForeignKey('professors.id'), nullable=False, index=True)
    professor = db.Relationship(ProfessorModel, backref='class_evaluations')

    @classmethod
    def update_rating_after_insert_or_update(cls):
        """
        Update the rating after an insert or update
        """

        evaluations = CollegeClassEvaluationModel.query.filter_by(class_code=cls.class_code).all()
        if evaluations:
            # Extract ratings using zip and calculate the total sum using map and sum
            total_scores = sum(
                            map(
                                sum, zip(
                                    *[(eval.lesson_exam_alingment, 
                                       eval.curriculum_exam_alingment, 
                                       eval.difficulty)
                                                    for eval in evaluations
                                        ]
                                    )
                                )
                            )

        total_possible = len(evaluations) * 5
        new_rating = total_scores / total_possible
        cls.college_class.rating = new_rating

        db.session.commit()
