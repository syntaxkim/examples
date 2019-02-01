import os
from models import *
from datetime import datetime, timedelta
from functools import wraps
import uuid

from flask import Flask, request, jsonify, make_response
from passlib.hash import pbkdf2_sha256
import jwt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL_REST')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# pylint: disable=no-member
db.init_app(app)

def verify_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        
        if not token:
            return jsonify({"message": "Token is missing"}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({"message": "Token is invalid"}), 401

        return f(user, *args, **kwargs)

    return decorated

'''User-related routes'''
@app.route('/users', methods=['GET'])
@verify_token
def get_users(user):
    if not user.admin:  
        return jsonify({"message": "Not authorized"}), 401
    
    users = User.query.all()

    data = []
    for user in users:
        data.append(parse_user(user))

    return jsonify({"users": data})
    
@app.route('/users/<public_id>', methods=['GET'])
@verify_token
def get_user(user, public_id):
    if not user.admin:  
        return jsonify({"message": "Not authorized"}), 401

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({"message": "No user found"})

    data = parse_user(user)
    return jsonify(data)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    public_id = str(uuid.uuid4())
    name = data['name']
    password = pbkdf2_sha256.hash(data['password'])
    user = User(public_id=public_id, name=name, password=password) # Transient state

    db.session.add(user) # Pending state
    db.session.commit() # Persistent state
    
    return jsonify({"message": "New user created"})

@app.route('/users/<public_id>', methods=['PUT'])
@verify_token
def update_user(user, public_id):
    if not user.admin:  
        return jsonify({"message": "Not authorized"}), 401

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({"message": "No user found"})

    if user.admin:
        return jsonify({"message": "Already updated"})

    user.admin = True
    db.session.commit()

    return jsonify({"message": "User updated"})

@app.route('/users/<public_id>', methods=['DELETE'])
@verify_token
def delete_user(user, public_id):
    if not user.admin:  
        return jsonify({"message": "Not authorized"}), 401

    user = User.query.filter_by(public_id=public_id).first()
    
    if not user:
        return jsonify({"message": "No user found"})

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted"})

# Authenticate with HTTP Basic Auth
@app.route('/login')
def login():
    # Get authorization information
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})

    user = User.query.filter_by(name=auth.username).first()

    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})

    if pbkdf2_sha256.verify(auth.password, user.password):
        # Generate a token
        token = jwt.encode({"public_id": user.public_id,
                            "exp": datetime.utcnow() + timedelta(minutes=30)},
                            app.config["SECRET_KEY"])
        return jsonify({"token": token.decode('UTF-8')})
    else:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})

    return make_response('Server error', 500)


'''Task-related routes'''
@app.route('/tasks', methods=['GET'])
@verify_token
def get_tasks(user):
    tasks = Task.query.filter_by(user_id=user.public_id).all()

    if not tasks:
        return jsonify({"message": "No task to do"})

    data = []
    for task in tasks:
        data.append({"id": task.id, "task": task.task, "complete": task.complete})

    return jsonify({'tasks': data})

@app.route('/tasks/<task_id>', methods=['GET'])
@verify_token
def get_task(user, task_id):
    task = Task.query.filter_by(id=task_id, user_id=user.public_id).first()

    if not task:
        return jsonify({"message": "No task found"})

    data = {"id": task.id, "task": task.task, "complete": task.complete}

    return jsonify(data)

@app.route('/tasks', methods=['POST'])
@verify_token
def create_task(user):
    data = request.get_json()

    task = Task(task=data['task'], user_id=user.public_id)
    db.session.add(task)
    db.session.commit()

    return jsonify({"message": "New task created"})

@app.route('/tasks/<task_id>', methods=['PUT'])
@verify_token
def complete_task(user, task_id):
    task = Task.query.filter_by(id=task_id, user_id=user.public_id).first()

    if not task:
        return jsonify({"message": "No task found"})
    
    if task.complete:
        return jsonify({"message": "Already completed"})

    task.complete = True
    db.session.commit()

    return jsonify({"message": "Task completed"})

@app.route('/tasks/<task_id>', methods=['DELETE'])
@verify_token
def delete_task(user, task_id):
    task = Task.query.filter_by(id=task_id, user_id=user.public_id).first()

    if not task:
        return jsonify({"message": "No task found"})

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": "Task deleted"})

def parse_user(user):
    return {"public_id": user.public_id,
            "name": user.name,
            "password": user.password,
            "admin": user.admin}

if __name__ == "__main__":
    with app.app_context():
        app.run()