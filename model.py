from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgres://wzyikgbuzredqk:d378505fe38ff6c1d9adab45e6a05774c20693d524fb8a2a4c13fd6a034fe751@ec2-46-137-120-243.eu-west-1.compute.amazonaws.com:5432/d57dh43iuefimi")
Session = sessionmaker(bind=engine)
base = declarative_base(engine)
session = Session()

class Botusers(base):
    __tablename__ = "botusers"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    def __init__(self, tgid, name):
        self.id = tgid
        self.name = name

    
    def __repr__(self):
        return "'%s', '%s'" % \
               (self.id, self.name)
