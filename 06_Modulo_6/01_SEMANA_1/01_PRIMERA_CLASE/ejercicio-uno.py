"""
API de Clientes

Este módulo implementa una API RESTful para la gestión de clientes utilizando FastAPI.
Proporciona operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para la gestión de clientes.

Módulos:
    fastapi: Framework para construir APIs
    pydantic: Para validación de datos y serialización
    typing: Para tipos de datos opcionales

Ejemplo de uso:
    >>> uvicorn ejercicio-uno:app --reload
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# Create FastAPI instance
app = FastAPI(
    title="Cliente API",
    description="API para gestionar clientes",
    version="1.0.0"
)

# Models
class ClienteBase(BaseModel):
    """
    Modelo base para los clientes.
    
    Attributes:
        nombre (str): Nombre del cliente
        edad (int): Edad del cliente
    """
    nombre: str
    edad: int

class ClienteCreate(ClienteBase):
    """
    Modelo para la creación de clientes.
    Hereda de ClienteBase.
    """
    pass

class ClienteUpdate(BaseModel):
    """
    Modelo para la actualización de clientes.
    
    Attributes:
        nombre (Optional[str]): Nuevo nombre del cliente (opcional)
        edad (Optional[int]): Nueva edad del cliente (opcional)
    """
    nombre: Optional[str] = None
    edad: Optional[int] = None

class ClienteResponse(ClienteBase):
    """
    Modelo de respuesta para los clientes.
    
    Attributes:
        id (int): Identificador único del cliente
        nombre (str): Nombre del cliente
        edad (int): Edad del cliente
    """
    id: int

    class Config:
        """Configuración del modelo Pydantic."""
        from_attributes = True

# In-memory storage (replace with database in production)
clientes = {}
cliente_id_counter = 1

# Routes
@app.post("/clientes", response_model=ClienteResponse, status_code=201)
async def crear_cliente(cliente: ClienteCreate) -> ClienteResponse:
    """
    Crea un nuevo cliente en el sistema.
    
    Args:
        cliente (ClienteCreate): Datos del cliente a crear
        
    Returns:
        ClienteResponse: Cliente creado con su ID asignado
        
    Raises:
        HTTPException: Si ocurre un error durante la creación (500)
    """
    global cliente_id_counter
    try:
        nuevo_cliente = ClienteResponse(
            id=cliente_id_counter,
            nombre=cliente.nombre,
            edad=cliente.edad
        )
        clientes[cliente_id_counter] = nuevo_cliente
        cliente_id_counter += 1
        return nuevo_cliente
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/", response_model=dict)
async def inicio() -> dict:
    """
    Endpoint de inicio de la API.
    
    Returns:
        dict: Mensaje de bienvenida
    """
    return {"mensaje": "Bienvenido a la API de Clientes"}

@app.get("/clientes", response_model=list[ClienteResponse])
async def listar_clientes() -> list[ClienteResponse]:
    """
    Obtiene la lista de todos los clientes registrados.
    
    Returns:
        list[ClienteResponse]: Lista de todos los clientes
    """
    return list(clientes.values())

@app.get("/clientes/{cliente_id}", response_model=ClienteResponse)
async def obtener_cliente(cliente_id: int) -> ClienteResponse:
    """
    Obtiene un cliente específico por su ID.
    
    Args:
        cliente_id (int): ID del cliente a buscar
        
    Returns:
        ClienteResponse: Datos del cliente encontrado
        
    Raises:
        HTTPException: Si el cliente no existe (404)
    """
    if cliente_id not in clientes:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return clientes[cliente_id]

@app.put("/clientes/{cliente_id}", response_model=ClienteResponse)
async def actualizar_cliente(cliente_id: int, cliente_update: ClienteUpdate) -> ClienteResponse:
    """
    Actualiza los datos de un cliente existente.
    
    Args:
        cliente_id (int): ID del cliente a actualizar
        cliente_update (ClienteUpdate): Datos a actualizar
        
    Returns:
        ClienteResponse: Cliente actualizado
        
    Raises:
        HTTPException: Si el cliente no existe (404)
    """
    if cliente_id not in clientes:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    
    cliente_actual = clientes[cliente_id]
    update_data = cliente_update.model_dump(exclude_unset=True)
    
    cliente_actualizado = cliente_actual.model_copy(update=update_data)
    clientes[cliente_id] = cliente_actualizado
    
    return cliente_actualizado

@app.delete("/clientes/{cliente_id}", status_code=204)
async def eliminar_cliente(cliente_id: int) -> None:
    """
    Elimina un cliente del sistema.
    
    Args:
        cliente_id (int): ID del cliente a eliminar
        
    Raises:
        HTTPException: Si el cliente no existe (404)
    """
    if cliente_id not in clientes:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    
    del clientes[cliente_id]
    return None

