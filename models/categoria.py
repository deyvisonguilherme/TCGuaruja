from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper
from dal.database import metadata, db_session


class Categoria(object):
    query = db_session.query_property()

    def __init__(self, nm_categoria=None):
        self.nm_categoria = nm_categoria

    def __repr__(self):
        return '<Categoria %r>' % (self.nm_categoria)


categorias = Table('categorias', metadata,
                   Column('id', Integer, primary_key=True, nullable=False),
                   Column('nm_categoria', String(50), unique=True, nullable=False),
                   )
mapper(Categoria, categorias)
