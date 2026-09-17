# Keskinube Backend

API REST desarrollada con Django y Django REST Framework para la gestión de negocios, productos, categorías y etiquetas.

El backend permite registrar usuarios, crear un negocio asociado a cada usuario, autenticarse mediante JWT y administrar productos pertenecientes únicamente al negocio autenticado.

## Tecnologías utilizadas

- Python
- Django
- Django REST Framework
- Simple JWT
- drf-spectacular
- SQLite
- Gunicorn
- Docker
- Git / GitHub

## Funcionalidades principales

- Registro de usuarios
- Autenticación mediante JWT
- Creación de negocio por usuario
- Gestión de categorías
- Gestión de etiquetas
- Gestión de productos
- Aislamiento de información por negocio
- Documentación automática con Swagger y ReDoc
- Contenerización con Docker

## Flujo principal

El flujo general de la aplicación es:

1. Registrar un usuario.
2. Iniciar sesión y obtener tokens JWT.
3. Crear un negocio asociado al usuario.
4. Crear categorías y etiquetas.
5. Crear y administrar productos.
6. Consultar únicamente la información perteneciente al negocio autenticado.

## Modelos principales

### User

Usuario personalizado basado en `AbstractUser`.

El correo electrónico es utilizado como campo principal de autenticación.

### Business

Representa el negocio perteneciente al usuario.

Cada usuario puede tener un negocio asociado.

### Category

Permite clasificar los productos de un negocio.

### Tag

Permite asignar etiquetas a los productos.

### Product

Representa los productos registrados en el sistema.

Incluye información como:

- Nombre
- Descripción
- SKU
- Precio de venta
- Costo
- Stock
- Tipo de producto
- Visibilidad
- Categoría
- Etiquetas

## Autenticación

La API utiliza autenticación JWT mediante Simple JWT.

### Obtener token

```http
POST /api/token/
```

Ejemplo:

```json
{
  "email": "usuario@email.com",
  "password": "password"
}
```

La respuesta incluye:

```json
{
  "refresh": "...",
  "access": "..."
}
```

Para acceder a endpoints protegidos se debe enviar:

```http
Authorization: Bearer ACCESS_TOKEN
```

### Renovar token

```http
POST /api/token/refresh/
```

## Endpoints principales

### Usuarios

```http
POST /api/users/register/
```

### Negocios

```http
POST /api/businesses/
```

### Productos

```http
GET /api/products/
POST /api/products/
GET /api/products/{id}/
PUT /api/products/{id}/
PATCH /api/products/{id}/
DELETE /api/products/{id}/
```

### Categorías

```http
GET /api/products/categories/
POST /api/products/categories/
GET /api/products/categories/{id}/
PUT /api/products/categories/{id}/
PATCH /api/products/categories/{id}/
DELETE /api/products/categories/{id}/
```

### Etiquetas

```http
GET /api/products/tags/
POST /api/products/tags/
GET /api/products/tags/{id}/
PUT /api/products/tags/{id}/
PATCH /api/products/tags/{id}/
DELETE /api/products/tags/{id}/
```

## Documentación de la API

Swagger:

```text
/api/docs/
```

ReDoc:

```text
/api/redoc/
```

Schema OpenAPI:

```text
/api/schema/
```

## Instalación local

Clonar el repositorio:

```bash
git clone https://github.com/Bet0os/keskinube-backend.git
cd keskinube-backend
```

Crear entorno virtual:

```bash
python -m venv venv
```

Activar el entorno en Windows:

```powershell
venv\Scripts\activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Aplicar migraciones:

```bash
python manage.py migrate
```

Ejecutar servidor:

```bash
python manage.py runserver
```

La API estará disponible en:

```text
http://127.0.0.1:8000/
```

## Docker

Construir la imagen:

```bash
docker build -t keskinube-backend .
```

Ejecutar el contenedor:

```bash
docker run --rm -p 8000:8000 keskinube-backend
```

El contenedor ejecuta automáticamente las migraciones y posteriormente inicia Gunicorn.

La API estará disponible en:

```text
http://127.0.0.1:8000/
```

## Pruebas

Para ejecutar las pruebas:

```bash
python manage.py test
```

## Seguridad

Los endpoints protegidos utilizan JWT.

Los recursos de productos, categorías y etiquetas se filtran utilizando el negocio asociado al usuario autenticado, evitando que un usuario pueda acceder a información perteneciente a otro negocio.

## Estructura principal

```text
keskinube-backend/
│
├── businesses/
├── config/
├── products/
├── users/
├── Dockerfile
├── manage.py
├── requirements.txt
├── REQUIREMENTS.md
├── TEST_PLAN.md
└── ER_DIAGRAM.md
```

## Diagramas y documentación

El repositorio contiene:

- `REQUIREMENTS.md` — requerimientos funcionales del proyecto.
- `TEST_PLAN.md` — plan de pruebas.
- `ER_DIAGRAM.md` — diagrama entidad-relación.

## Autor

Alberto Camacho

Proyecto desarrollado como parte de Residencias Profesionales 2026.