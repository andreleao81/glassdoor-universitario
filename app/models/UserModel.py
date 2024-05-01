from app.extensions import db 
from .BaseModel import BaseModel

class UserModel(BaseModel):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False, index=True)
    password = db.Column(db.String(128), nullable=False)