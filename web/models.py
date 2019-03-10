from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

db = SQLAlchemy()

Base = declarative_base()

class Account(db.Model):
    __tablename__ = 'account'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(255))
    telephone = db.Column(db.String(50),unique = True)

    def __repr__(self):
        return '<Account %s>'% self.username

class Class(Base):
    __tablename__ = 'class'
    student_id = Column(Integer,primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    gender = Column(String(10))
    address = Column(String(50))



