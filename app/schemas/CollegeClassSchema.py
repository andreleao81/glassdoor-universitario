from ..models.CollegeClassModel import CollegeClassModel
from ..extensions import ma


class CollegeClassSchema(ma.SQLAlchemySchema):
    class Meta:
        model = CollegeClassModel
        load_instance = True
        ordered = True
    
    id = ma.Integer(dump_only=True)
    name = ma.String(required=True)
    class_code = ma.String(required=True)
    semester = ma.String(required=True)
