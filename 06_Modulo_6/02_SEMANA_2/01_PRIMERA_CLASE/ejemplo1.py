from pydantic import BaseModel

class Usuario(BaseModel):
    nombre: str
    edad: int

#usuario = Usuario("Luis", "25")
usuario = Usuario(nombre="Luis", edad="25")
print(usuario)