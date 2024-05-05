# from ..extensions import db
# from ..models import BaseModel


# class ProfessorModel(BaseModel):
#     __tablename__='professors'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(60), nullable=False)
    
from ..models.ProfessorModel import ProfessorModel
from ..extensions import ma

class ProfessorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProfessorModel
        load_instance = True
        include_fk = True
        load_only = ['id']
        include_relationships = True

    id = ma.Integer(dump_only=True)
    name = ma.String(required=True)
    professor_evaluations = ma.Nested('ProfessorEvaluationSchema', many=True, exclude=('professor_id',))
    

