class User(BaseModel):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.LargeBinary(128), nullable=False)
    pin_hash = db.Column(db.LargeBinary(128))
    create_time = db.Column(db.DateTime)
    modify_time = db.Column(db.DateTime)