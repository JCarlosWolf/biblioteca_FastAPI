# Personal Library API: RESTful Inventory Management Backend

**Developed by:** José Carlos Lobo  
**Main Stack:** Python | FastAPI | MySQL | SQLAlchemy | Alembic | Pydantic  

---

## Language / Idioma

* For technical and architectural documentation: 👉 **[Read in English](#english-version)**
* Para el caso de estudio orientado a negocio: 👉 **[Leer en Español](#spanish-version)**

---

<div id="english-version"></div>

# English Version

## 🎯 Executive Summary & Business Value

Even within simpler administrative scopes, inventory governance, data integrity, and structured persistence layer versioning are crucial factors for any corporate software ecosystem. A failure to accurately map internal catalogs or poor migration tracking results in database downtime and system inconsistencies.

Personal Library API is a production-style RESTful backend engineered to showcase high-quality standalone service design. Moving away from messy, unvetted scripts, this application structures a full CRUD data model using strict object-relational mapping (ORM), enforces typing validations, and leverages modern database evolution techniques to simulate micro-inventory tracking.

### 🏢 Technical Value Highlights:
* Data Schema Evolution: Database state tracking using versioned migrations, mitigating data-loss risk during structure changes.
* Cross-Origin Production Ready: Configured CORS middleware ensuring seamless integration with modern web frontends (React, Angular, or Vue).
* Safe Input Contract Enforcement: Request sanitization checking format rules before data reaches the transactional layer.

---

## 🚀 Key Features & Architectural Assets

* Full Resource Life Cycle (CRUD): Robust endpoints covering data entry creation, index filtering, precise resource targeting, updates, and secure deletion.
* Strict Input-Output Contracts: Powered by Pydantic schemas to shield the application layer from malicious or malformed parameters.
* Relational ORM Mapping: Utilizing SQLAlchemy to abstract raw queries into clean, object-oriented operations bound to a MySQL server.
* Professional Project Layout: Decoupled design separating endpoints, data schemas, domain entities, and operational service layers.

---

## 🛠️ Project Layout & Structure

Built following standard backend organizational layouts for enterprise maintainability:

Layout del Proyecto:
biblioteca_fastapi/
│
├── main.py                # Server initialization and CORS pipeline setups
├── database.py            # Session management and engine context bindings
├── schemas.py             # Data schema models and request validators
├── .env                   # Local infrastructure parameters
│
├── models/
│   └── libro.py           # Domain entity representations (SQLAlchemy Models)
├── services/
│   └── libro_service.py   # Context business logic transactions
├── api/
│   └── libros.py          # RESTful routing endpoints
│
├── alembic/               # Database structural change scripts
├── alembic.ini           # Migration engine configuration
└── migrate.py             # Evolutionary execution helper

---

## 📋 Quick Start & Local Deployment

### Prerequisites
* Python 3.10+
* Active MySQL Server instance

### 1. Installation
Comandos para ejecutar en consola:
git clone https://github.com/JCarlosWolf/biblioteca_fastapi.git
cd biblioteca_fastapi
python -m venv .venv

* Activar entorno virtual:
Windows: .venv\Scripts\activate
Linux/macOS: source .venv/bin/activate

Instalar dependencias:
pip install -r requirements.txt

### 2. Infrastructure Setup (.env)
Create a .env file in the root directory pointing to your local database:
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password_here
DB_NAME=library_db

### 3. Migrations & Server Execution
Apply migrations to build the schema automatically and spin up the server:
alembic upgrade head
uvicorn main:app --reload

Interactive Swagger Documentation UI: http://localhost:8000/docs

---

## ✉️ Contact & Process Consulting

* Developer: José Carlos Lobo
* Specialty: Secure API Architectures, Python Core Automation, & Relational Database Design.
* LinkedIn: www.linkedin.com/in/josé-carlos-lobo-473b458a

---
---

<div id="spanish-version"></div>

# Versión en Español: Caso de Estudio de Negocio

## 🎯 ¿Qué es Personal Library API? (Perspectiva de Negocio)

Incluso en los entornos administrativos más sencillos, el control de inventario, la integridad de los datos y el control evolutivo de las estructuras de almacenamiento son factores críticos. La falta de validación o un mal manejo de las actualizaciones en la base de datos se traduce de inmediato en inconsistencias del sistema y caídas operativas.

Personal Library API es un backend RESTful diseñado bajo estándares profesionales para la gestión automatizada de catálogos y almacenes de datos. Este proyecto implementa un flujo completo de operaciones CRUD (Creación, Lectura, Actualización y Eliminado) aplicando mapeo objeto-relacional (ORM), validaciones estrictas y control evolutivo de la base de datos para garantizar que la información corporativa se guarde siempre de forma segura y estructurada.

### 🏢 Impacto y Relevancia Técnica:
* Control de Cambios en Base de Datos (Migrations): Implementación de Alembic para versionar los esquemas de datos, asegurando que cualquier cambio de estructura se realice sin riesgo de pérdida de información.
* Integración Segura (CORS): Configuración nativa para permitir el consumo inmediato del backend desde cualquier interfaz o aplicación frontend moderna (React, Angular, etc.).
* Contratos de Datos Seguros: El sistema valida la información antes de que toque la base de datos, garantizando la consistencia del negocio y evitando inyecciones de datos corruptos.

---

## 🚀 Características Clave y Valor Empresarial

* Modelo de Datos Relacional: Arquitectura acoplada a un servidor MySQL a través de SQLAlchemy, abstrayendo consultas complejas en código limpio y mantenible.
* Validaciones de Negocio Estrictas: Reglas de negocio automatizadas (como la validación de puntuaciones de contenido de 1 a 5) mediante esquemas de Pydantic.
* Estructura Limpia Separada por Capas: Organización profesional que divide las rutas de la API, los esquemas de validación, los servicios de persistencia y las entidades del dominio, facilitando auditorías de código rápidas y escalabilidad a largo plazo.

---

## ✉️ Contacto y Consultoría de Automatización

* Desarrollador: José Carlos Lobo
* LinkedIn: www.linkedin.com/in/josé-carlos-lobo-473b458a
