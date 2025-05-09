from pydantic import BaseModel

class TareaEntrante(BaseModel):
    titulo: str
    descripcion: str

class TareaSaliente(BaseModel):
    id: int
    titulo: str
    descripcion: str
    completado: bool

# ejemplo de un modelo para una API en produccion

class ProductoEntrante(BaseModel):
    nombre: str
    precio: float

class ProductoSaliente(BaseModel):
    id: int
    nombre: str
    precio: float
    disponibilidad: bool

