from app.extensions import db
from .BaseModel import BaseModel


class CollegeClassModel(BaseModel):
    __tablename__='college_classes'
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(60), nullable=False)
    code = db.Column(db.String(60), nullable=False, index=True)
    semester = db.Column(db.Integer, nullable=False)
