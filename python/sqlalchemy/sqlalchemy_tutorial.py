''' This example code is based on the tutorial
https://docs.sqlalchemy.org/en/latest/orm/tutorial.html '''

import os

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Connecting to the Database
engine = create_engine(os.getenv('DATABASE_URL_TEST'))
# Create a global scope Session to handle the Database
Session = sessionmaker(bind=engine)

# Declare a Mapping
Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)

    def __repr__(self):
        return f"<User(name={self.name}, password={self.password})>"

# Create a Schema (CREATE TABLE)
# Base.metadata.create_all(engine)

def add_user():
    # Create an Instance of the Mapped Class (transient state)
    user = User(name='Ed', password='password')

    # Create a local scope Session
    session = Session()

    # Add an Object to the Session (pending state)
    session.add(user)

    # Commit the Transaction (persistent state)
    session.commit()

''' About State Management
https://docs.sqlalchemy.org/en/latest/orm/session_state_management.html '''

if __name__ == "__main__":
    session = Session()
    our_user = session.query(User).filter_by(name='Ed').first()
    print(our_user.password)

    our_user.password = 'password' # (pending state)
    print(our_user.password)

    session.rollback() # Roll back Changes made
    print(our_user.password)
