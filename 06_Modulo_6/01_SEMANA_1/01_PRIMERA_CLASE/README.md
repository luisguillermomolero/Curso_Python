# API de Clientes

Esta es una API RESTful desarrollada con FastAPI para gestionar clientes. Proporciona operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para la gestión de clientes.

## Requisitos

- Python 3.7+
- FastAPI
- uvicorn

## Instalación

1. Instalar las dependencias:

```bash
pip install fastapi uvicorn
```

2. Ejecutar la API:

```bash
uvicorn ejercicio-uno:app --reload
```

La API estará disponible en `http://localhost:8000`

## Documentación de la API

La documentación interactiva está disponible en:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Modelos de Datos

### ClienteBase

```json
{
  "nombre": "string",
  "edad": "integer"
}
```

### ClienteCreate

```json
{
  "nombre": "string",
  "edad": "integer"
}
```

### ClienteUpdate

```json
{
  "nombre": "string (opcional)",
  "edad": "integer (opcional)"
}
```

### ClienteResponse

```json
{
  "id": "integer",
  "nombre": "string",
  "edad": "integer"
}
```

## Endpoints

### 1. Crear Cliente

- **Método**: POST
- **Ruta**: `/clientes`
- **Descripción**: Crea un nuevo cliente
- **Código de estado**: 201 (Created)
- **Request Body**:

```json
{
  "nombre": "Juan Pérez",
  "edad": 30
}
```

- **Response**:

```json
{
  "id": 1,
  "nombre": "Juan Pérez",
  "edad": 30
}
```

### 2. Obtener Todos los Clientes

- **Método**: GET
- **Ruta**: `/clientes`
- **Descripción**: Lista todos los clientes registrados
- **Código de estado**: 200 (OK)
- **Response**:

```json
[
  {
    "id": 1,
    "nombre": "Juan Pérez",
    "edad": 30
  }
]
```

### 3. Obtener Cliente por ID

- **Método**: GET
- **Ruta**: `/clientes/{cliente_id}`
- **Descripción**: Obtiene un cliente específico por su ID
- **Código de estado**: 200 (OK)
- **Parámetros de ruta**:
  - `cliente_id`: ID del cliente
- **Response**:

```json
{
  "id": 1,
  "nombre": "Juan Pérez",
  "edad": 30
}
```

### 4. Actualizar Cliente

- **Método**: PUT
- **Ruta**: `/clientes/{cliente_id}`
- **Descripción**: Actualiza un cliente existente
- **Código de estado**: 200 (OK)
- **Parámetros de ruta**:
  - `cliente_id`: ID del cliente a actualizar
- **Request Body**:

```json
{
  "nombre": "Juan Pérez Actualizado",
  "edad": 31
}
```

- **Response**:

```json
{
  "id": 1,
  "nombre": "Juan Pérez Actualizado",
  "edad": 31
}
```

### 5. Eliminar Cliente

- **Método**: DELETE
- **Ruta**: `/clientes/{cliente_id}`
- **Descripción**: Elimina un cliente existente
- **Código de estado**: 204 (No Content)
- **Parámetros de ruta**:
  - `cliente_id`: ID del cliente a eliminar

## Códigos de Error

- **404 Not Found**: Cuando el cliente no existe
- **500 Internal Server Error**: Cuando ocurre un error en el servidor

## Ejemplos de Uso

### Crear un nuevo cliente

```bash
curl -X POST "http://localhost:8000/clientes" \
     -H "Content-Type: application/json" \
     -d '{"nombre": "Juan Pérez", "edad": 30}'
```

### Obtener todos los clientes

```bash
curl -X GET "http://localhost:8000/clientes"
```

### Obtener un cliente específico

```bash
curl -X GET "http://localhost:8000/clientes/1"
```

### Actualizar un cliente

```bash
curl -X PUT "http://localhost:8000/clientes/1" \
     -H "Content-Type: application/json" \
     -d '{"nombre": "Juan Pérez Actualizado", "edad": 31}'
```

### Eliminar un cliente

```bash
curl -X DELETE "http://localhost:8000/clientes/1"
```

## Notas

- La API utiliza almacenamiento en memoria, por lo que los datos se perderán al reiniciar el servidor
- Para producción, se recomienda implementar una base de datos persistente
- Todos los endpoints son asíncronos para mejor rendimiento
- La API incluye validación automática de datos usando Pydantic
