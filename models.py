from sqlalchemy import Column, Integer, String
from database import Base

class Categorias(Base):
    __tablename__='categorias'
    id = Column(serial, primary_key=True)
    nm_categoria = Column(String(25),nullable=False, unique=True)

    def __init__(self, name=None, categoria=None):
        self.id = id,
        self.categoria = categoria

    def __repr__(self):
        return '<categoria %r>' %(self.name)