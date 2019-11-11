from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgres://kdbqihrelkjdyh:5703c7cbdcbb12d999e210368936b8b734940f07d4b6357ff3d5eed99d6e3b91@ec2-54-247-85-251.eu-west-1.compute.amazonaws.com:5432/d6lcrvpadm6o79")
Session = sessionmaker(bind=engine)
base = declarative_base(engine)
session = Session()

class dbm:
    __slots__ = ['session']
    def __enter__(self):
        self.session = session()
        return self.session
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.commit()
        self.session.close()

class Users(base):
    __tablename__ = "Users"
    tgid = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
def __str__(self, tgid, name):
    self.tgid = tgid
    self.name = name

    
def __repr__(self):
    return "'%s', '%s'" % \
           (self.tgid, self.name)
