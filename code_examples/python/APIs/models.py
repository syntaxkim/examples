from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import false

db = SQLAlchemy()

# pylint: disable=no-member
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False, server_default=false())

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(50), nullable=False)
    complete = db.Column(db.Boolean, nullable=False, default=False, server_default=false())
    user_id = db.Column(db.String(50), db.ForeignKey('users.public_id'), nullable=False)
    

''' Python
from application import *
with app.app_context():
    db.create_all()
'''