from pydantic import BaseModel, Field

# min_length: establece la longitud mínima permitida para una cadena (string).
# max_length: establece la longitud máxima permitida para una cadena.
# gt: "greater than" → debe ser mayor que un valor.
# lt: "less than" → debe ser menor que un valor.
# ge: "greater or equal" → debe ser mayor o igual que un valor.
# le: "less or equal" → debe ser menor o igual que un valor.
# pattern(): se usa para verificar que una cadena cumpla un formato específico

# regex(): pydantic v1
# pattern(): pydantic v2

class Usuario(BaseModel):
    username: str = Field(..., min_length=4, max_length=12)
    edad: int = Field(..., gt=17, lt=100)

class Reserva(BaseModel):
    cliente: str = Field(..., min_length=3)
    fecha: str = Field(..., pattern=r"\\d{4}-\\{2}-\\d{2}") # AAAA-MM-DD
    personas: int =  Field(..., ge=1, le=10)

