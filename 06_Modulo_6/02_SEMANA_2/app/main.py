from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import List, Dict, Optional

app = FastAPI()

# Modelo de entrada Post/Put
class RecursoCreate(BaseModel):
    nombre: str = Field(..., min_length=4, max_length=20)
    descripcion: Optional[str] = Field(None, max_length=200)

class RecursoResponse(RecursoCreate):
    item_id: int = Field(..., gt=0)

class UsuarioCreate(BaseModel):
    username: str = Field(..., min_length=5, max_length=20)
    email: str = Field(..., pattern=r"^[a-zA-Z09._%+-]+@[a-zA-Z0-9.-]+\[a-zA-Z]{2,}$")
    edad: int =  Field(..., gt=0, lt=100)

class UsuarioResponse(UsuarioCreate):
    user_id: int = Field(..., gt=0)

db_recursos: List[Dict] = []
next_recurso_id = 1

db_usuarios: List[Dict] = []
next_usuario_id = 1

@app.get("/")
def root():
    return {"mensage": "Uso de pydantic, HTTPException, JSONResponse y Field"}

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

@app.get("/recursos/")
def get_all_recursos():
    return db_recursos

@app.get("/recurso/{item_id}", response_model=RecursoResponse)
def read_recurso(item_id: int):
    if item_id <= 0:
        raise HTTPException(status_code=422, detail="Id de recurso invalido. Introduzca un número positivo")
    
    for item in db_recursos:
        if item["item_id"] == item_id:
            return item
    
    raise HTTPException(status_code=404, detail="Recurso no encontrado")
