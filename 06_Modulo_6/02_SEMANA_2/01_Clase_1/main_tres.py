from pydantic import BaseModel, Field

class Usuario(BaseModel):
    username: str = Field(..., min_length=8, max_length=15)
    edad: int = Field(..., gt=17, lt=100)

class Reserva(BaseModel):
    cliente: str = Field(...,min_length=4)
    fecha: str = Field(..., regex=r"\\d{4}-\\{2}-\\{2}") # ALT 92
    personas: int = Field(..., ge=1, le=10)

