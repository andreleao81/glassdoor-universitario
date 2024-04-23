import datetime
import json
from pytz import timezone
from flask import jsonify
import bcrypt

import flask_jwt_extended as jwt
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request, decode_token

from ..extensions import db
from ..utils.dateTime import dateTime
from ..models import BaseModel


class CollegeClass(BaseModel):
    __tablename__='college_classes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    code = db.Column(db.String(6), unique=True, nullable=False, index=True)
    semester = db.Column(db.Integer, nullable=False)
