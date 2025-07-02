from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional

app = FastAPI()

class Recurso(BaseModel):
    nombre: str
    descripcion: Optional[str] = None

db: List[Dict] = []
next_item_id = 1

@app.get("/")
def read__root():
    return {"mensaje": "API de ejemplo para manejo de HTTPException"}

@app.get("/recursos/")
def get_all_recursos():
    return {"recursos": db}

@app.get("/recursos/{item_id}")
def read_item(item_id: int):
    if item_id < 0:
        raise HTTPException(status_code=422, detail="Id invalido")
    for item in db:
        if item["item_id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Recurso no encontrado")

@app.post("/recursos/")
def create_item(recurso: Recurso):
    global next_item_id
    new_item = recurso.model_dump()
    new_item["item_id"] = next_item_id
    db.append(new_item)
    next_item_id += 1
    
    print(f"Recurso recibido y agregado: {new_item}")
    return {"mensaje": "Recurso creado exitosamente", "data": new_item}

