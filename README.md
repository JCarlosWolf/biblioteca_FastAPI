# 📚 Biblioteca Personal – Backend REST con FastAPI y MySQL

Backend RESTful desarrollado con **FastAPI** para gestionar una **biblioteca personal de libros**.  
Incluye un CRUD completo, validaciones, migraciones de base de datos y configuración CORS para consumo desde frontend (React / Angular).

---

## 🚀 Tecnologías utilizadas

- **FastAPI** – Framework web rápido y tipado
- **Uvicorn** – Servidor ASGI
- **SQLAlchemy** – ORM para MySQL
- **Alembic** – Migraciones de base de datos
- **Pydantic** – Validación de datos
- **MySQL** – Base de datos relacional
- **PyMySQL** – Conector MySQL
- **python-dotenv** – Variables de entorno
- **CORS Middleware** – Acceso desde frontend

---

## 📌 Funcionalidades

✔️ Crear libros  
✔️ Listar libros  
✔️ Obtener libro por ID  
✔️ Actualizar libros  
✔️ Eliminar libros  
✔️ Validaciones de datos  
✔️ Migraciones versionadas  
✔️ CORS configurado  

---

## 📊 Modelo de datos

**Tabla:** `libros`

| Campo  | Tipo    | Reglas |
|------|--------|-------|
| id | int | PK, autoincrement |
| titulo | string | obligatorio |
| autor | string | obligatorio |
| rating | int | entre 1 y 5 |

---

## 🧱 Estructura del proyecto

```text
biblioteca_fastapi/
│
├── main.py
├── database.py
├── schemas.py
├── .env
├── models/
│   └── libro.py
├── services/
│   └── libro_service.py
├── api/
│   └── libros.py
├── alembic/
├── alembic.ini
└── migrate.py
