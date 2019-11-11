from sqlalchemy import Column, Integer, String, Boolean, MetaData, Table, create_engine
from sqlalchemy.orm import mapper, sessionmaker
from model import engine, session, base
meta = MetaData()
Botusers = Table(
   'botusers', meta,
   Column('id', Integer, primary_key = True),
   Column('name', String),
)
meta.create_all(engine)
