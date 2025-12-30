# database.py
# Configuración de la base de datos, sesión y prueba de conexión.

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# URL de conexión a MySQL usando PyMySQL
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Crear engine SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, future=True)

# Crear clase base para modelos
Base = declarative_base()

# Crear factory de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependencia para FastAPI
def get_db():
    """
    Genera una sesión de base de datos para cada petición y la cierra al finalizar.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Prueba rápida de conexión
if __name__ == "__main__":
    try:
        with engine.connect() as conn:
            print("Conexión a la base de datos exitosa!")
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
