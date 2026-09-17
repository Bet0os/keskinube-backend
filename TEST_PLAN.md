# Test Plan - Keskinube Backend

## Objetivo

El objetivo de este plan de pruebas es comprobar que las funciones principales del backend trabajen correctamente y que la información de cada negocio permanezca separada entre usuarios.

## Pruebas

### TP-01 Registro de usuario

Se debe comprobar que un usuario pueda registrarse utilizando:

- First name
- Last name
- Email
- Password
- Confirm password

Resultado esperado:

El usuario se registra correctamente y la API responde con código 201.

---

### TP-02 Validación de contraseñas

Se debe comprobar que el registro sea rechazado cuando `password` y `confirm_password` sean diferentes.

Resultado esperado:

La API debe responder con un error de validación y no crear al usuario.

---

### TP-03 Inicio de sesión

Se debe comprobar que un usuario registrado pueda iniciar sesión utilizando su email y contraseña.

Resultado esperado:

La API debe devolver un access token y un refresh token JWT.

---

### TP-04 Creación de negocio

Se debe comprobar que un usuario autenticado pueda crear su negocio proporcionando únicamente el nombre.

Resultado esperado:

El negocio se crea correctamente y queda relacionado automáticamente con el usuario autenticado.

---

### TP-05 Creación de categoría

Se debe comprobar que un usuario autenticado pueda crear una categoría.

Resultado esperado:

La categoría se crea correctamente y queda relacionada con el negocio del usuario.

---

### TP-06 Creación de etiqueta

Se debe comprobar que un usuario autenticado pueda crear una etiqueta.

Resultado esperado:

La etiqueta se crea correctamente y queda relacionada con el negocio del usuario.

---

### TP-07 Creación de producto

Se debe comprobar que un usuario pueda registrar un producto con los campos definidos para producto simple.

Campos principales:

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

Resultado esperado:

El producto se crea correctamente y queda relacionado automáticamente con el negocio del usuario autenticado.

---

### TP-08 Consulta de productos

Se debe comprobar que un usuario autenticado pueda consultar los productos pertenecientes a su negocio.

Resultado esperado:

La API devuelve únicamente los productos relacionados con su negocio.

---

### TP-09 Actualización de producto

Se debe comprobar que un producto pueda ser modificado.

Resultado esperado:

Los datos enviados son actualizados correctamente.

---

### TP-10 Eliminación de producto

Se debe comprobar que un producto pueda ser eliminado.

Resultado esperado:

La API elimina el producto y responde con código 204.

---

### TP-11 CRUD de categorías

Se debe comprobar que las categorías puedan:

- Crearse
- Consultarse
- Actualizarse
- Eliminarse

Resultado esperado:

Todas las operaciones se realizan correctamente dentro del negocio autenticado.

---

### TP-12 CRUD de etiquetas

Se debe comprobar que las etiquetas puedan:

- Crearse
- Consultarse
- Actualizarse
- Eliminarse

Resultado esperado:

Todas las operaciones se realizan correctamente dentro del negocio autenticado.

---

### TP-13 Aislamiento entre negocios

Se deben crear dos usuarios con negocios diferentes.

El segundo usuario intentará consultar los productos, categorías y etiquetas creados por el primero.

Resultado esperado:

El segundo usuario no debe poder ver información perteneciente al negocio del primer usuario.

Las consultas deben devolver únicamente información de su propio negocio.

---

### TP-14 Acceso a endpoints protegidos

Se debe intentar acceder a endpoints protegidos sin enviar un token JWT.

Resultado esperado:

La API debe rechazar la petición por falta de autenticación.

---

## Criterio de aceptación

El backend se considera aprobado cuando:

- Los usuarios pueden registrarse e iniciar sesión.
- JWT protege los endpoints privados.
- Cada usuario puede crear su negocio.
- Los productos se relacionan con el negocio autenticado.
- Las categorías y etiquetas pertenecen al negocio correspondiente.
- Los usuarios no pueden acceder a información de otros negocios.
- Las operaciones principales de productos, categorías y etiquetas funcionan correctamente.