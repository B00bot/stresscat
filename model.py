from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgres://kdbqihrelkjdyh:5703c7cbdcbb12d999e210368936b8b734940f07d4b6357ff3d5eed99d6e3b91@ec2-54-247-85-251.eu-west-1.compute.amazonaws.com:5432/d6lcrvpadm6o79")
Session = sessionmaker(bind=engine)
base = declarative_base(engine)
session = Session()

class dbm:
    def __enter__
  
class users(base):
  
