from ..models.ClassEvaluationModel import CollegeClassEvaluationModel
from ..extensions import ma
from marshmallow import ValidationError, validates, post_load, validates_schema, validates

class CollegeClassEvaluationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CollegeClassEvaluationModel
        load_instance = True
        include_fk = True
        include_relationships = False
        ordered = True
        exclude = ['create_time', 'update_time']


    id = ma.Integer(dump_only=True)
    
    semester_concluded = ma.Integer(required=True) # add further validation
    
    lesson_exam_alingment = ma.Integer(required=True)
    curriculum_exam_alingment = ma.Integer(required=True)
    difficulty = ma.Integer(required=True)
   
    class_code = ma.String(required=True)
    user_id = ma.Integer(required=True)
    professor_id = ma.Integer(required=True)    

    @post_load
    def make_upper(self, data, **kwargs):
        data.class_code = data.class_code.upper()
        return data
    
    @validates('class_code')
    def validate_class_code(self, value, **kwargs):
        if len(value) != 6:
            raise ValidationError('Class code must have 6 characters')
        
    
    @validates_schema
    def validates_score(self, data, **kwargs):
        for field in ['lesson_exam_alingment', 'curriculum_exam_alingment', 'difficulty']:
            value = data.get(field)
            if value is not None and (value < 1 or value > 5):
                raise ValidationError('Rating must be a number among (1,2,3,4,5)', field)

