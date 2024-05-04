from ..models.UserModel import UserModel
from ..extensions import ma

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = UserModel
        load_instance = True
        ordered = True
    
    id = ma.Integer(dump_only=True)
    username = ma.String(required=True)
    email = ma.Email(required=True)
    password = ma.String(load_only=True, required=True)

# class UsersSchemas(ma.SQLAlchemySchema):
#     class Meta:
#         model = UserModel
#         load_instance = True
#         ordered = True
#     id = ma.Integer(dump_only=True)
#     username = ma.String(required=True)
#     email = ma.Email(required=True)
#     password = ma.String(load_only=True, required=True)
    