from pydantic import BaseModel, ConfigDict

class TareaBase(BaseModel):
    titulo: str
    descripcion: str = ""
    completado: bool = False
    
class TareaCreate(TareaBase):
    pass

class TareaOut(TareaBase):
    id: int

model_config = ConfigDict(from_attributes=True)