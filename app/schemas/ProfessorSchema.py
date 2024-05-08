from ..models.ProfessorModel import ProfessorModel
from ..extensions import ma

class ProfessorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProfessorModel
        load_instance = True
        include_fk = True
        include_relationships = True
        # exclude = 'create_time', 'update_time'

    id = ma.Integer(dump_only=True)
    name = ma.String(required=True)
    professor_evaluations = ma.Nested('ProfessorEvaluationSchema', many=True, exclude=('professor_id',))
    

