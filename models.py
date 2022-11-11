import sqlalchemy
from db import base

import time

class Student(base):
    __tablename__ = "student"
    id = sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, unique=True, default=int(time.time()))
    name = sqlalchemy.Column("name", sqlalchemy.String(50))

class Subject(base):
    __tablename__ = "subject"
    id = sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, unique=True, default=int(time.time()))
    name = sqlalchemy.Column("name", sqlalchemy.String(50))