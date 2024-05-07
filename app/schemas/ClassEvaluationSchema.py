from ..models.ClassEvaluationModel import CollegeClassEvaluationModel
from ..extensions import ma

class CollegeClassEvaluationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CollegeClassEvaluationModel
        load_instance = True
        include_fk = True
        include_relationships = True
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only=True)
    
    semester_concluded = ma.Integer(required=True) # add further validation
    lesson_exam_alingment = ma.Integer(required=True)
    curriculum_exam_alingment = ma.Integer(required=True)
    difficulty = ma.Integer(required=True)
   
    class_code = ma.String(required=True)
    user_id = ma.Integer(required=True)
    professor_id = ma.Integer(required=True)    


