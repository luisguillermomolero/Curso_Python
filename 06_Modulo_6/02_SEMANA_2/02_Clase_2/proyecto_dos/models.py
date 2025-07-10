from pydantic import BaseModel, Field

class TareaEntrada(BaseModel):
    titulo: str = Field(..., min_length=3)
    descripcion: str =  Field(..., min_length=10)

class TareaSaliente(BaseModel):
    id: int
    titulo: str
    descripcion: str
    completado: bool