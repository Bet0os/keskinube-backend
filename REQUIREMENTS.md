# Requerimientos del Proyecto - Keskinube Backend

## 1. Descripción general

Keskinube debe permitir que diferentes usuarios registren y administren la información de su propio negocio.

Toda la información del sistema debe quedar relacionada con el negocio del usuario autenticado.

Esto incluye:

- Productos
- Categorías
- Etiquetas

Un usuario no debe poder consultar, modificar o eliminar información perteneciente a otro negocio.

---

## 2. Flujo principal

El flujo principal del sistema será:

1. Registro de usuario.
2. Creación de negocio.
3. Inicio de sesión.
4. Creación de categorías.
5. Creación de etiquetas.
6. Registro de productos.
7. Consulta, edición y eliminación de productos.

---

## 3. Registro de usuario

El sistema debe permitir registrar un nuevo usuario.

Campos requeridos:

- First name
- Last name
- Email
- Password
- Confirm Password

Reglas:

- El email debe ser único.
- Password y Confirm Password deben coincidir.
- La contraseña debe almacenarse de forma segura.
- Si las contraseñas no coinciden, el registro debe rechazarse.

Endpoint:

POST /api/users/register/

---

## 4. Inicio de sesión

El usuario debe poder iniciar sesión utilizando:

- Email
- Password

La autenticación debe realizarse mediante JWT.

Cuando las credenciales sean correctas, la API debe devolver:

- Access Token
- Refresh Token

Endpoints:

POST /api/token/

POST /api/token/refresh/

---

## 5. Creación de negocio

Después del registro, el usuario debe poder crear su negocio.

Campo requerido:

- Nombre del negocio

Cada negocio debe quedar relacionado con el usuario autenticado.

El cliente no debe enviar manualmente el ID del usuario.

El backend debe obtenerlo desde:

request.user

Endpoint:

POST /api/businesses/

---

## 6. Separación de información por negocio

El sistema debe soportar múltiples negocios.

Cada usuario únicamente debe acceder a la información perteneciente a su propio negocio.

La separación debe aplicarse a:

- Productos
- Categorías
- Etiquetas

El backend debe filtrar los datos utilizando el negocio del usuario autenticado.

Ejemplo conceptual:

Product.objects.filter(
    business=request.user.business
)

Esto debe impedir que un usuario pueda acceder a datos pertenecientes a otro negocio.

---

## 7. Dashboard

De acuerdo con el diseño visual, el dashboard contiene diferentes opciones.

Para esta versión del backend únicamente se requiere soportar el flujo relacionado con la creación y administración de productos.

La función principal utilizada será:

Agregar producto

Otros elementos visuales como estadísticas, planes, navegación inferior o configuración no forman parte del alcance actual.

---

## 8. Tipo de producto

El diseño contempla los siguientes tipos:

- Producto simple
- Producto con modelos
- Producto con modelos y variantes

En esta versión únicamente se implementará:

Producto simple

Los demás tipos quedan fuera del alcance actual.

---

## 9. Registro de producto

El sistema debe permitir crear un producto simple.

Cada producto debe quedar relacionado automáticamente con el negocio del usuario autenticado.

Campos:

- Nombre
- Descripción
- SKU / Código
- Precio de venta
- Costo
- Stock
- Tipo de producto
- Visibilidad
- Categoría
- Etiquetas

---

## 10. Nombre del producto

El nombre del producto es obligatorio.

Ejemplo:

Laptop HP Pavilion 15

---

## 11. Descripción

El producto puede tener una descripción.

La descripción tendrá un máximo de 500 caracteres.

Ejemplo:

Laptop para uso general.

---

## 12. SKU / Código

El producto puede tener un código o SKU.

Ejemplo:

LAP-HP-001

Este campo puede ser opcional.

---

## 13. Precio de venta

Todo producto debe tener un precio de venta.

Ejemplo:

1299.00

Debe almacenarse como un valor decimal.

---

## 14. Costo

El producto puede tener un costo asociado.

Ejemplo:

950.00

Este campo puede ser opcional.

---

## 15. Stock

El producto debe almacenar la cantidad disponible.

Ejemplo:

15

El stock debe utilizar un número entero positivo.

---

## 16. Tipo de producto

El producto debe almacenar el tipo de producto.

Para esta versión únicamente se utilizará:

simple

---

## 17. Visibilidad del producto

El producto debe permitir indicar si se encuentra visible u oculto.

Este valor se manejará mediante un booleano.

Valores posibles:

true

false

Si is_visible es true, el producto se considera visible.

Si is_visible es false, el producto permanece registrado pero se considera oculto.

---

## 18. Categorías

El sistema debe permitir administrar categorías.

Cada categoría debe pertenecer al negocio del usuario autenticado.

Operaciones requeridas:

- Crear categoría
- Listar categorías
- Consultar categoría
- Actualizar categoría
- Eliminar categoría

Endpoints:

POST /api/products/categories/

GET /api/products/categories/

GET /api/products/categories/{id}/

PATCH /api/products/categories/{id}/

DELETE /api/products/categories/{id}/

---

## 19. Etiquetas

El sistema debe permitir administrar etiquetas.

Cada etiqueta debe pertenecer al negocio del usuario autenticado.

Ejemplos:

- Oferta
- Nuevo
- Destacado
- Promoción

Operaciones requeridas:

- Crear etiqueta
- Listar etiquetas
- Consultar etiqueta
- Actualizar etiqueta
- Eliminar etiqueta

Endpoints:

POST /api/products/tags/

GET /api/products/tags/

GET /api/products/tags/{id}/

PATCH /api/products/tags/{id}/

DELETE /api/products/tags/{id}/

---

## 20. Relación entre productos y categorías

Un producto puede pertenecer a una categoría.

La categoría utilizada debe pertenecer al mismo negocio que el producto.

Relación conceptual:

Business
|
Category
|
Product

---

## 21. Relación entre productos y etiquetas

Un producto puede tener varias etiquetas.

Una etiqueta puede estar asociada con varios productos.

Por lo tanto, existe una relación Many-to-Many.

La relación debe manejarse mediante una tabla intermedia llamada:

ProductTag

Relación conceptual:

Product
|
ProductTag
|
Tag

---

## 22. Relación del producto con el negocio

Cada producto debe quedar relacionado con el negocio del usuario autenticado.

El cliente no debe enviar manualmente el negocio.

El backend debe utilizar:

request.user.business

---

## 23. Operaciones de productos

La API debe permitir realizar las siguientes operaciones.

Crear producto:

POST /api/products/

Listar productos:

GET /api/products/

Consultar producto:

GET /api/products/{id}/

Actualizar producto:

PATCH /api/products/{id}/

Eliminar producto:

DELETE /api/products/{id}/

---

## 24. Autenticación de endpoints

Los endpoints privados deben requerir autenticación JWT.

El token debe enviarse mediante:

Authorization: Bearer <access_token>

Si el usuario no envía un token válido, la API debe rechazar la petición.

---

## 25. Seguridad entre negocios

Un usuario no debe poder acceder a información perteneciente a otro negocio.

Esto aplica a:

- Productos
- Categorías
- Etiquetas

Por ejemplo, si un producto pertenece a otro negocio, el usuario autenticado no debe poder:

- Consultarlo
- Modificarlo
- Eliminarlo

---

## 26. Validaciones principales

El backend debe validar:

- Que el email sea único.
- Que Password y Confirm Password coincidan.
- Que los endpoints privados requieran autenticación.
- Que los productos pertenezcan al negocio autenticado.
- Que las categorías pertenezcan al negocio autenticado.
- Que las etiquetas pertenezcan al negocio autenticado.
- Que no se pueda acceder a datos de otros negocios.
- Que los campos obligatorios estén presentes.
- Que el stock sea válido.
- Que los precios sean válidos.

---

## 27. Modelo de datos

Las entidades principales son:

- User
- Business
- Category
- Tag
- Product
- ProductTag

Relaciones principales:

User
|
Business
|
|-- Category
|
|-- Tag
|
|-- Product
     |
     ProductTag
     |
     Tag

---

## 28. Tecnologías

El backend se desarrollará utilizando:

- Python
- Django
- Django REST Framework
- Django ORM
- JWT
- SQLite

También se utilizarán:

- Swagger
- Pruebas automatizadas
- Docker
- Deployment

---

## 29. Alcance actual

Esta versión incluye:

- Registro de usuarios
- Login con JWT
- Creación de negocios
- Separación de datos por negocio
- Categorías
- Etiquetas
- Productos simples
- CRUD de productos
- CRUD de categorías
- CRUD de etiquetas
- Relación entre productos, categorías y etiquetas

---

## 30. Fuera del alcance

No se implementará en esta etapa:

- Productos con modelos
- Productos con variantes
- Estadísticas avanzadas
- Sistema de planes
- Interfaz gráfica
- Frontend
- Aplicación móvil

---

## 31. Criterios de aceptación

El backend se considera funcional cuando:

- Un usuario puede registrarse.
- Se validan las contraseñas.
- El usuario puede iniciar sesión.
- El login devuelve tokens JWT.
- El usuario puede crear un negocio.
- El negocio queda relacionado con el usuario.
- El usuario puede crear categorías.
- El usuario puede crear etiquetas.
- El usuario puede crear productos.
- Cada producto queda relacionado con su negocio.
- Los productos pueden tener categoría.
- Los productos pueden tener etiquetas.
- El usuario puede consultar sus productos.
- El usuario puede actualizar sus productos.
- El usuario puede eliminar sus productos.
- El usuario puede administrar categorías.
- El usuario puede administrar etiquetas.
- Un usuario no puede acceder a información de otro negocio.
- Los endpoints privados rechazan solicitudes sin autenticación.