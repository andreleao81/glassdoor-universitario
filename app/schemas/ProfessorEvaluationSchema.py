from ..models.ProfessorEvaluationModel import ProfessorEvaluationModel
from ..extensions import ma
from marshmallow import ValidationError, validates, post_load, validates_schema, validates


class ProfessorEvaluationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProfessorEvaluationModel
        load_instance = True
        include_fk = True
        load_instance = True
        ordered = True
        exclude = ['create_time', 'update_time']

    id = ma.Integer(dump_only=True)
    
    semester = ma.Integer(required=True)
    
    attendance = ma.Boolean(required=True)
    punctuality = ma.Integer(required=True)
    availability_questions = ma.Integer(required=True)
    student_relationship = ma.Integer(required=True)
    professor_methodology = ma.Integer(required=True)

    class_code = ma.String(required=True)
    user_id = ma.Integer(required=True)
    professor_id = ma.Integer(required=True)

    #forces class_code when creating or updating a new evaluation to be a string upper
    @post_load
    def make_upper(self, data):
        data['class_code'] = data['class_code'].upper()
        return data
    
    @validates('class_code')
    def validate_class_code(self, value):
        if len(value) != 6:
            raise ValidationError('Class code must have 6 characters')
    
    @validates('semester')
    def validate_semester(self, value):
        if value < 1 or value > 5:
            raise ValidationError('Semester must be a number between 1 and 5')
        return value
    
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