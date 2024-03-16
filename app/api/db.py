from sqlalchemy import (Column, DateTime, Integer, MetaData, String, Table, create_engine, ARRAY)
from databases import Database

DATABASE_URI = 'postgresql://secUREusER:StrongEnoughPassword)@51.250.26.59:5432/postgres'

#движок для взаимодейтсвия с бд
engine = create_engine(DATABASE_URI)
# контейнер для определения таблиц базы данных
metadata = MetaData()

companies = Table(
    'companies',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('description', String(250)),
    Column('industry', Integer),
    Column('age', Integer)
)

database = Database(DATABASE_URI)