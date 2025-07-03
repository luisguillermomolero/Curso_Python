from pydantic import BaseModel

class TareaEntrante(BaseModel):
    titulo: str
    descripcion: str

class TareaSaliente(BaseModel):
    id: int
    titulo: str
    descripcion: str
    completado: bool

