from ..models.CurriculumModel import CurriculumModel
from ..extensions import ma
from marshmallow import ValidationError, validates, post_load, validates_schema, validates

class CurriculumSchema(ma.SQLAlchemySchema):
    class Meta:
        model = CurriculumModel
        load_instance = True
        ordered = True
    
    id = ma.Integer(dump_only=True)
    class_code = ma.String(required=True)
    semester = ma.String(required=True)
    conclusion = ma.Boolean(required=True, default=False)
    attending = ma.Boolean(required=True, default=True)
    user_id = ma.Integer(required=True)

    @validates_schema
    def validate_attending_concluded(self, **kwargs):
        if self.attending and self.conclusion:
            raise ValueError('A class cannot be both attending and concluded')
        
    @validates('semester')
    def validate_semester(self, value, **kwargs):
        if not 1 <= int(value) <= 20:
            raise ValidationError('Semester must be greater than 0')
    
    @post_load
    def make_upper(self, data, **kwargs):
        data.class_code = data.class_code.upper()
        return data
    
    
