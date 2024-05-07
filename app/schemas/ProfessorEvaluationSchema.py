from ..models.ProfessorEvaluationModel import ProfessorEvaluationModel
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

class ProfessorEvaluationPostSchema(ProfessorEvaluationSchema):
    # remove id from post schema
    class Meta:
        model = ProfessorEvaluationModel
        load_instance = True
        include_fk = True
        include_relationships = True
        load_instance = True
        ordered = True
        exclude = ('id',)