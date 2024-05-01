from flask import abort, jsonify, make_response
from sqlalchemy.exc import IntegrityError
from app.extensions import db

class BaseModel(db.Model):

    __abstract__ = True

    create_time = db.Column(db.DateTime(timezone=True),
                            server_default=db.func.now())
    update_time = db.Column(db.DateTime(timezone=True),
                            onupdate=db.func.now())

    @classmethod
    def create(cls, **data) -> object:
        return cls(**data)

    @staticmethod
    def delete(obj):
        db.session.delete(obj)
        db.session.commit()

    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
        except IntegrityError as err:
            db.session.rollback()
            abort(make_response(
                jsonify({'errors': str(err.orig)}), 400))