# api/libros.py
# Router encargado de exponer las rutas relacionadas con libros.


from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from schemas import LibroRead, LibroCreate, LibroUpdate
from services.libro_service import (
    listar_libros,
    crear_libro,
    obtener_libro_por_id,
    actualizar_libro,
    eliminar_libro
)

router = APIRouter(
    prefix="/api/libros",
    tags=["Libros"]
)


@router.get("/", response_model=List[LibroRead])
def obtener_libros(db: Session = Depends(get_db)):
    return listar_libros(db)


@router.get("/{libro_id}", response_model=LibroRead)
def obtener_libro(libro_id: int, db: Session = Depends(get_db)):
    return obtener_libro_por_id(db, libro_id)


@router.post(
    "/",
    response_model=LibroRead,
    status_code=status.HTTP_201_CREATED
)
def crear_nuevo_libro(
    libro: LibroCreate,
    db: Session = Depends(get_db)
):
    return crear_libro(db, libro)


@router.put(
    "/{libro_id}",
    response_model=LibroRead
)
def actualizar_libro_endpoint(
    libro_id: int,
    libro: LibroUpdate,
    db: Session = Depends(get_db)
):
    return actualizar_libro(db, libro_id, libro)


@router.delete(
    "/{libro_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def eliminar_libro_endpoint(
    libro_id: int,
    db: Session = Depends(get_db)
):
    """
    Endpoint para eliminar un libro.
    """
    eliminar_libro(db, libro_id)
    return None
