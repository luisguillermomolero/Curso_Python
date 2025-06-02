# Guía de Pruebas de API - Sistema de Tareas

Esta guía proporciona instrucciones paso a paso para probar todas las APIs disponibles en el sistema de gestión de tareas.

## Requisitos Previos

1. Asegúrate de tener instaladas todas las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

2. Configura la base de datos PostgreSQL con las siguientes variables de entorno (o usa los valores por defecto):

   - DB_USER=postgres
   - DB_PASSWORD=1126254560
   - DB_HOST=localhost
   - DB_PORT=5432
   - DB_NAME=tareas_db

3. Inicializa la base de datos:

   ```bash
   python init_db.py
   ```

4. Inicia el servidor:
   ```bash
   uvicorn main:app --reload
   ```

## Endpoints Disponibles

La API estará disponible en `http://localhost:8000`

### 1. Crear una Tarea

- **Endpoint**: POST `/tareas/`
- **Descripción**: Crea una nueva tarea
- **Cuerpo de la petición**:
  ```json
  {
    "titulo": "Mi primera tarea",
    "descripcion": "Esta es una descripción de prueba",
    "completado": false
  }
  ```
- **Respuesta esperada**:
  ```json
  {
    "id": 1,
    "titulo": "Mi primera tarea",
    "descripcion": "Esta es una descripción de prueba",
    "completado": false
  }
  ```

### 2. Listar Todas las Tareas

- **Endpoint**: GET `/tareas/`
- **Descripción**: Obtiene todas las tareas
- **Respuesta esperada**:
  ```json
  [
    {
      "id": 1,
      "titulo": "Mi primera tarea",
      "descripcion": "Esta es una descripción de prueba",
      "completado": false
    }
  ]
  ```

### 3. Obtener una Tarea Específica

- **Endpoint**: GET `/tareas/{tarea_id}`
- **Descripción**: Obtiene una tarea específica por su ID
- **Ejemplo**: GET `/tareas/1`
- **Respuesta esperada**:
  ```json
  {
    "id": 1,
    "titulo": "Mi primera tarea",
    "descripcion": "Esta es una descripción de prueba",
    "completado": false
  }
  ```

### 4. Actualizar una Tarea

- **Endpoint**: PUT `/tareas/{tarea_id}`
- **Descripción**: Actualiza una tarea existente
- **Ejemplo**: PUT `/tareas/1`
- **Cuerpo de la petición**:
  ```json
  {
    "titulo": "Tarea actualizada",
    "descripcion": "Nueva descripción",
    "completado": true
  }
  ```
- **Respuesta esperada**:
  ```json
  {
    "id": 1,
    "titulo": "Tarea actualizada",
    "descripcion": "Nueva descripción",
    "completado": true
  }
  ```

### 5. Eliminar una Tarea

- **Endpoint**: DELETE `/tareas/{tarea_id}`
- **Descripción**: Elimina una tarea específica
- **Ejemplo**: DELETE `/tareas/1`
- **Respuesta esperada**:
  ```json
  {
    "ok": true
  }
  ```

## Herramientas Recomendadas para Pruebas

1. **Postman**: Una herramienta popular para probar APIs
2. **cURL**: Para pruebas desde la línea de comandos
3. **FastAPI Swagger UI**: Accesible en `http://localhost:8000/docs`

## Ejemplos de cURL

### Crear una tarea

```bash
curl -X POST "http://localhost:8000/tareas/" -H "Content-Type: application/json" -d '{"titulo":"Nueva tarea","descripcion":"Descripción de prueba","completado":false}'
```

### Listar tareas

```bash
curl -X GET "http://localhost:8000/tareas/"
```

### Obtener una tarea específica

```bash
curl -X GET "http://localhost:8000/tareas/1"
```

### Actualizar una tarea

```bash
curl -X PUT "http://localhost:8000/tareas/1" -H "Content-Type: application/json" -d '{"titulo":"Tarea actualizada","descripcion":"Nueva descripción","completado":true}'
```

### Eliminar una tarea

```bash
curl -X DELETE "http://localhost:8000/tareas/1"
```

## Notas Importantes

1. Asegúrate de que el servidor esté en ejecución antes de realizar las pruebas
2. Los IDs de las tareas son autoincrementales
3. Todas las respuestas están en formato JSON
4. En caso de error, la API devolverá un código de estado HTTP apropiado y un mensaje de error
