# main.py
# Punto de entrada de la aplicación FastAPI.

from fastapi import FastAPI

# Import del middleware CORS
from fastapi.middleware.cors import CORSMiddleware

from api.libros import router as libros_router

app = FastAPI(
    title="API Biblioteca Personal",
    description="Backend REST con FastAPI y MySQL",
    version="1.0.0"
)

#  Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200",  # Angular
        "http://localhost:5173",  # React (Vite)
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    """
    Endpoint de prueba para verificar que la API está activa.
    """
    return {"mensaje": "API Biblioteca activa 🚀"}

# Registro del router de libros
app.include_router(libros_router)
