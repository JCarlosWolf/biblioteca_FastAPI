# schemas.py
# Esquemas Pydantic para validación de datos y respuestas.

from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class LibroBase(BaseModel):
    """
    Esquema base compartido por creación y actualización.
    Define los campos comunes y sus validaciones.
    """
    titulo: str = Field(
        ...,
        min_length=1,
        description="Título del libro (no puede estar vacío)"
    )
    autor: str = Field(
        ...,
        min_length=1,
        description="Autor del libro (no puede estar vacío)"
    )
    rating: int = Field(
        ...,
        ge=1,
        le=5,
        description="Calificación del libro (entre 1 y 5)"
    )


class LibroCreate(LibroBase):
    """
    Esquema para crear un libro.
    Hereda todas las validaciones de LibroBase.
    """
    pass


class LibroUpdate(BaseModel):
    """
    Esquema para actualizar un libro.
    Todos los campos son opcionales para permitir
    actualizaciones parciales.
    """
    titulo: Optional[str] = Field(
        None,
        min_length=1,
        description="Nuevo título del libro"
    )
    autor: Optional[str] = Field(
        None,
        min_length=1,
        description="Nuevo autor del libro"
    )
    rating: Optional[int] = Field(
        None,
        ge=1,
        le=5,
        description="Nueva calificación del libro (1 a 5)"
    )


class LibroRead(LibroBase):
    """
    Esquema de salida (response).
    Incluye el ID generado por la base de datos.
    """
    id: int

    model_config = ConfigDict(from_attributes=True)
