# models/libro.py
# Definición del modelo Libro para la base de datos.

from sqlalchemy import Column, Integer, String
from database import Base

class Libro(Base):
    """
    Modelo SQLAlchemy para la tabla 'libros'.
    Representa un libro en la biblioteca personal.
    """
    __tablename__ = "libros"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String(255), nullable=False, index=True)
    autor = Column(String(255), nullable=False, index=True)
    rating = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Libro(id={self.id}, titulo='{self.titulo}', autor='{self.autor}', rating={self.rating})>"
