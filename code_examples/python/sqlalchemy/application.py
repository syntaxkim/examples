import os

from flask import Flask
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def relationship():
    user = User.query.filter_by(name='user5').first()    
    for checkin in user.checkins:
        print(f"{checkin.name}: {checkin.comment:20} - {checkin.time}")

    print()

    location = Location.query.filter_by(zipcode=55555).first()
    for checkin in location.checkins:
        print(f"{checkin.name}: {checkin.comment:20} - {checkin.time}")
    
    # new_checkin = Checkin(name='user4', comment='Let\'ts do this.', location_id=location.id)
    # Checkin.add_checkin(new_checkin)

def backref():
    checkin = Checkin.query.filter_by(name='user4').first()
    print(f"{checkin.name}: {checkin.comment:20} - {checkin.time}")

    # Here comes the new properties that are not in class Checkin but declared by backref
    print(checkin.user)
    print(checkin.location)


if __name__ == "__main__":
    with app.app_context():
        # relationship()
        backref()