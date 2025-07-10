from fastapi.responses import JSONResponse
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Dict, Optional

app = FastAPI()

class RecursoCreate(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=50) # Nombre es requerido, entre 3 y 50 caracteres
    descripcion: Optional[str] = Field(None, max_length=200) # Descripción es opcional, máximo 200 caracteres

class RecursoResponse(RecursoCreate): # Hereda de RecursoCreate para reusar los campos
    item_id: int = Field(..., gt=0) # El ID del recurso, requerido y positivo

class UsuarioCreate(BaseModel):
    username: str = Field(..., min_length=4, max_length=16) # Nombre de usuario requerido, entre 4 y 16 caracteres
    email: str = Field(..., pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$") # Email requerido con formato de email
    edad: int = Field(..., gt=0, lt=120) # Edad requerida, mayor que 0 y menor que 120

class UsuarioResponse(UsuarioCreate): # Hereda de UsuarioCreate para reusar los campos
    user_id: int = Field(..., gt=0) # El ID del usuario, requerido y positivo

db_recursos: List[Dict] = []
next_recurso_id = 1

db_usuarios: List[Dict] = []
next_usuario_id = 1

@app.get("/")
def read_root():
    """
    Endpoint raíz que devuelve un mensaje de bienvenida.
    """
    return {"message": "¡Hola, mundo! Esta es tu API inicial."}

## Endpoints para Recursos

@app.post("/recurso/", response_model=RecursoResponse)
def create_recurso(recurso: RecursoCreate):
    global next_recurso_id
    new_item = recurso.model_dump()
    new_item["item_id"] = next_recurso_id
    db_recursos.append(new_item)
    next_recurso_id += 1
    
    response_content ={
        "mensaje": "Recurso creado con éxito",
        "recurso": new_item
    }
    return JSONResponse(content=response_content,status_code=status.HTTP_201_CREATED)

@app.get(
    "/recursos/",
    response_model=List[RecursoResponse], # Especifica que la respuesta es una lista de RecursoResponse
    summary="Obtener todos los recursos"
)
def get_all_recursos():
    """
    Recupera todos los recursos almacenados.
    """
    # Retorna la lista de diccionarios, Pydantic se encarga de la validación y serialización
    return db_recursos

