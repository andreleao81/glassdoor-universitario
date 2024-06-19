from app.extensions import db 
from flask import abort, jsonify, make_response
from sqlalchemy.exc import IntegrityError

from .BaseModel import BaseModel
from .CollegeClassModel import CollegeClassModel
from .CurriculumModel import CurriculumModel

class UserModel(BaseModel):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False, index=True)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
    
    def check_password(self, password): 
        #sim é isso mesmo, "né segredo"
        return self.password == password 
    
    def create_all_history(self):
        from .CurriculumModel import CurriculumModel

        #query ClassesModel for all classes
        #query only the ids, not the whole object
        class_codes = CollegeClassModel.query.with_entities(CollegeClassModel.class_code).all()

        data = [
                {'conclusion': False, 'class_code': class_code[0], 'user_id': self.id}
                for class_code in class_codes
                ]

        # Bulk insert the data
        try:
            db.session.bulk_insert_mappings(CurriculumModel, data)
            db.session.commit()
        except IntegrityError as err:
            db.session.rollback()
            abort(make_response(
                jsonify({'errors': str(err.orig)}), 400))
        
            