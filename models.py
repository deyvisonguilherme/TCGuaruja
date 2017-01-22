from sqlalchemy import Column, Integer, String
from database import Base


class ModelCategoria(Base):
    __tablename__ = 'categorias'
    id = Column(Integer, primary_key=True, nullable=False)
    nm_categoria = Column(String(25), unique=True, nullable=False)

    def __init__(self, nm_categoria=None):
        self.nm_categoria = nm_categoria

    def __repr__(self):
        return "<Categorias (nm_categoria='%s'>" % self.nm_categoria