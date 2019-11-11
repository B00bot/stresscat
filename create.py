from sqlalchemy import Column, Integer, String, Boolean, MetaData, Table, create_engine
from sqlalchemy.orm import mapper, sessionmaker
import model
meta = MetaData()
user = Table(
   'users', meta,
   Column('id', Integer, primary_key = True),
   Column('name', String),
)
meta.create_all(engine)
