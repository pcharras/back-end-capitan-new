from app import db
import uuid

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)

    def __init__(self, public_id, username, password):
        self.public_id = public_id
        self.username = username
        self.password = password

    def __repr__(self):
        return f"<User {self.username}>"
