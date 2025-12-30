# services/libro_service.py
# Capa de servicios encargada de la lógica relacionada con libros.

from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from models.libro import Libro
from schemas import LibroCreate, LibroUpdate


def listar_libros(db: Session):
    return db.query(Libro).all()


def obtener_libro_por_id(db: Session, libro_id: int):
    libro = db.query(Libro).filter(Libro.id == libro_id).first()

    if not libro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Libro no encontrado"
        )

    return libro


def crear_libro(db: Session, libro_data: LibroCreate):
    nuevo_libro = Libro(
        titulo=libro_data.titulo,
        autor=libro_data.autor,
        rating=libro_data.rating
    )

    db.add(nuevo_libro)
    db.commit()
    db.refresh(nuevo_libro)

    return nuevo_libro


def actualizar_libro(db: Session, libro_id: int, libro_data: LibroUpdate):
    libro = obtener_libro_por_id(db, libro_id)

    if libro_data.titulo is not None:
        libro.titulo = libro_data.titulo

    if libro_data.autor is not None:
        libro.autor = libro_data.autor

    if libro_data.rating is not None:
        libro.rating = libro_data.rating

    db.commit()
    db.refresh(libro)

    return libro


def eliminar_libro(db: Session, libro_id: int):
    """
    Elimina un libro existente.
    """
    libro = obtener_libro_por_id(db, libro_id)

    db.delete(libro)
    db.commit()

    return None
