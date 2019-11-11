from sqlalchemy import Column, Integer, String, Boolean, MetaData, Table, create_engine
from sqlalchemy.orm import mapper, sessionmaker
engine = create_engine("postgres://kdbqihrelkjdyh:5703c7cbdcbb12d999e210368936b8b734940f07d4b6357ff3d5eed99d6e3b91@ec2-54-247-85-251.eu-west-1.compute.amazonaws.com:5432/d6lcrvpadm6o79")
meta = MetaData()
user = Table(
   'users', meta,
   Column('id', Integer, primary_key = True),
   Column('name', String),
)
meta.create_all(engine)
