from ..models.CurriculumModel import CurriculumModel
from ..extensions import ma

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
    class_code = ma.String(required=True)
    user_id = ma.Integer(required=True)

    def validate_attending_concluded(self):
        if self.attending and self.concluded:
            raise ValueError('A class cannot be both attending and concluded')
        
    def validate_semester(self):
        if self.semester not in (lambda s: s in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']):
            raise ValueError('Semester must be greater than 0')