from app.extensions import db
from .BaseModel import BaseModel


class ProfessorModel(BaseModel):
    __tablename__='professors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    rating = db.Column(db.Float)
    
    
