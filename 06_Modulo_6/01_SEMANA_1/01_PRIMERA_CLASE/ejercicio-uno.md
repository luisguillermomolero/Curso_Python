# Documentación del Módulo ejercicio-uno

## Descripción General

Este módulo implementa una API RESTful para la gestión de clientes utilizando FastAPI. Proporciona operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para la gestión de clientes.

## Dependencias

- fastapi: Framework para construir APIs
- pydantic: Para validación de datos y serialización
- typing: Para tipos de datos opcionales

## Clases

### ClienteBase

Modelo base para los clientes.

**Atributos:**

- `nombre` (str): Nombre del cliente
- `edad` (int): Edad del cliente

### ClienteCreate

Modelo para la creación de clientes. Hereda de ClienteBase.

### ClienteUpdate

Modelo para la actualización de clientes.

**Atributos:**

- `nombre` (Optional[str]): Nuevo nombre del cliente (opcional)
- `edad` (Optional[int]): Nueva edad del cliente (opcional)

### ClienteResponse

Modelo de respuesta para los clientes.

**Atributos:**

- `id` (int): Identificador único del cliente
- `nombre` (str): Nombre del cliente
- `edad` (int): Edad del cliente

## Funciones

### crear_cliente

```python
async def crear_cliente(cliente: ClienteCreate) -> ClienteResponse
```

Crea un nuevo cliente en el sistema.

**Parámetros:**

- `cliente` (ClienteCreate): Datos del cliente a crear

**Retorna:**

- ClienteResponse: Cliente creado con su ID asignado

**Excepciones:**

- HTTPException: Si ocurre un error durante la creación (500)

### inicio

```python
async def inicio() -> dict
```

Endpoint de inicio de la API.

**Retorna:**

- dict: Mensaje de bienvenida

### listar_clientes

```python
async def listar_clientes() -> list[ClienteResponse]
```

Obtiene la lista de todos los clientes registrados.

**Retorna:**

- list[ClienteResponse]: Lista de todos los clientes

### obtener_cliente

```python
async def obtener_cliente(cliente_id: int) -> ClienteResponse
```

Obtiene un cliente específico por su ID.

**Parámetros:**

- `cliente_id` (int): ID del cliente a buscar

**Retorna:**

- ClienteResponse: Datos del cliente encontrado

**Excepciones:**

- HTTPException: Si el cliente no existe (404)

### actualizar_cliente

```python
async def actualizar_cliente(cliente_id: int, cliente_update: ClienteUpdate) -> ClienteResponse
```

Actualiza los datos de un cliente existente.

**Parámetros:**

- `cliente_id` (int): ID del cliente a actualizar
- `cliente_update` (ClienteUpdate): Datos a actualizar

**Retorna:**

- ClienteResponse: Cliente actualizado

**Excepciones:**

- HTTPException: Si el cliente no existe (404)

### eliminar_cliente

```python
async def eliminar_cliente(cliente_id: int) -> None
```

Elimina un cliente del sistema.

**Parámetros:**

- `cliente_id` (int): ID del cliente a eliminar

**Excepciones:**

- HTTPException: Si el cliente no existe (404)

## Variables Globales

### clientes

```python
clientes = {}
```

Diccionario que almacena los clientes en memoria.

### cliente_id_counter

```python
cliente_id_counter = 1
```

Contador para asignar IDs únicos a los clientes.

## Instancia de FastAPI

### app

```python
app = FastAPI(
    title="Cliente API",
    description="API para gestionar clientes",
    version="1.0.0"
)
```

Instancia principal de la aplicación FastAPI.

## Ejemplo de Uso

```bash
uvicorn ejercicio-uno:app --reload
```

## Notas

- La API utiliza almacenamiento en memoria, por lo que los datos se perderán al reiniciar el servidor
- Para producción, se recomienda implementar una base de datos persistente
- Todos los endpoints son asíncronos para mejor rendimiento
- La API incluye validación automática de datos usando Pydantic
