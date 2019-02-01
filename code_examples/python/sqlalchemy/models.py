from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import pbkdf2_sha256

db = SQLAlchemy()

# pylint: disable=no-member

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    checkins = db.relationship("Checkin", backref="user", lazy=True)

    def add_user(self):
        try:
            user = User(name=self.name, password=pbkdf2_sha256.hash(self.password))
            db.session.add(user)
            db.session.commit()
        except:
            raise Exception

class Location(db.Model):
    __tablename__ = "locations"
    id = db.Column(db.Integer, primary_key=True)
    zipcode = db.Column(db.Integer, unique=True, nullable=False)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    lat = db.Column(db.Float, nullable=False)
    long = db.Column(db.Float, nullable=False)
    population = db.Column(db.Integer, nullable=True)
    checkins = db.relationship("Checkin", backref="location", lazy=True)

    def add_location(self):
        try:
            location = Location(zipcode=self.zipcode, city=self.city, state=self.state, lat=self.lat, long=self.long, population=self.population)
            db.session.add(location)
            db.session.commit()
        except:
            raise Exception

class Checkin(db.Model):
    __tablename__ = "checkins"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, db.ForeignKey("users.name"), nullable=False)
    comment = db.Column(db.String(100), nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"), nullable=False)

    def add_checkin(self):
        try:
            checkin = Checkin(name=self.name, comment=self.comment, location_id=self.location_id)
            db.session.add(checkin)
            db.session.commit()
        except:
            raise Exception

