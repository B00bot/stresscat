from sqlalchemy import Column, Integer, String, Boolean, MetaData, Table
from sqlalchemy.orm import mapper, sessionmaker
meta = MetaData()
user = Table(
   'users', meta,
   Column('id', Integer, primary_key = True),
   Column('name', String),
)
meta.create_all(engine)
