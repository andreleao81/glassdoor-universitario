# from ..extensions import db
# from ..utils.DateTime import dateTime
# from ..models import BaseModel


# class CollegeClassModel(BaseModel):
#     __tablename__='class_evaluations'
#     id = db.Column(db.Integer, primary_key=True)
#     semester = db.Column(db.Integer, nullable=False)

#     lesson_exam_alingment = db.Column(db.Integer, nullable=False)
#     curriculum_exam_alingment = db.Column(db.Integer, nullable=False)
#     difficulty = db.Column(db.Integer, nullable=False)

#     class_code = db.Relationsip('CollegeClass', backref='class_evaluations')
#     user_id = db.Relationship('User', backref='class_evaluations')
#     professor_id = db.Relationship('Professor', backref='class_evaluations')


from ..models.ClassEvaluation import CollegeClassEvaluationModel
from ..extensions import ma

class CollegeClassEvaluationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CollegeClassEvaluationModel
        load_instance = True
        include_fk = True
        include_relationships = True
        load_instance = True
        ordered = True

    id = ma.Integer(load_only=True)
    
    semester = ma.Integer(required=True) # add further validation
    lesson_exam_alingment = ma.Integer(required=True)
    curriculum_exam_alingment = ma.Integer(required=True)
    difficulty = ma.Integer(required=True)
   
    class_code = ma.String(required=True)
    user_id = ma.Integer(required=True)
    professor_id = ma.Integer(required=True)    


