from app.extensions import db
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import check_password_hash

class User(db.Model, UserMixin):
    
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    @classmethod
    def get_by_id(cls, user_id):
        return cls.query.get(int(user_id))
    
    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
    
    def verify_password(self, raw_password):
        return check_password_hash(self.password, raw_password)