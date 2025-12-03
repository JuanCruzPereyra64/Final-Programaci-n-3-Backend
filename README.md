# 🚀 E-commerce API (Backend)

Este es el backend robusto y escalable para la plataforma de E-commerce, construido con **FastAPI** y **Python**. Maneja la lógica de negocio, gestión de productos, usuarios, carritos de compra y procesamiento de órdenes.

## 🛠️ Tecnologías Principales

*   **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (Alto rendimiento, fácil de usar).
*   **Lenguaje:** Python 3.11+.
*   **Base de Datos:** PostgreSQL.
*   **ORM:** SQLAlchemy (Gestión de modelos de datos).
*   **Validación:** Pydantic.
*   **Contenedorización:** Docker & Docker Compose.
*   **Migraciones:** Alembic.

## 📂 Estructura del Proyecto

```
backend/
├── controllers/    # Controladores de los endpoints (Lógica de rutas)
├── models/         # Modelos de base de datos (SQLAlchemy)
├── schemas/        # Esquemas de validación (Pydantic)
├── services/       # Lógica de negocio pura
├── repositories/   # Capa de acceso a datos
├── config/         # Configuración del entorno
└── main.py         # Punto de entrada de la aplicación
```

## 🚀 Cómo Ejecutar el Proyecto

### Opción 1: Docker (Recomendada)

La forma más sencilla de levantar todo el entorno (API + Base de Datos) es usando Docker.

1.  Asegúrate de tener Docker instalado.
2.  Desde la raíz del proyecto (una carpeta arriba), ejecuta:
    ```bash
    docker-compose up --build
    ```
3.  La API estará disponible en: `http://localhost:8000`
4.  Documentación interactiva (Swagger UI): `http://localhost:8000/docs`

### Opción 2: Ejecución Local (Manual)

1.  Crea un entorno virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```
2.  Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
3.  Configura las variables de entorno (crea un archivo `.env` basado en `.env.example`).
4.  Ejecuta el servidor:
    ```bash
    uvicorn main:app --reload
    ```

## 🧪 Endpoints Principales

*   **Productos:** `GET /products`, `POST /products`
*   **Categorías:** `GET /categories`
*   **Usuarios:** `POST /users/register`, `POST /users/login`
*   **Carrito:** `POST /cart/add`, `GET /cart`

## 📦 Despliegue (Deploy)

Este backend está optimizado para desplegarse en **Render** usando el `Dockerfile` incluido en la raíz de esta carpeta.
