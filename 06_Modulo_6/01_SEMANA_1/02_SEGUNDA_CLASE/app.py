from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# Creart la instancia de FastAPI

app = FastAPI()

# Lista para almacenar los items
items = {}

# Modelo de Pydantic para crear y validar los items
class Item(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    impuesto: Optional[float] = None
    
@app.get("/")
def root():
    return {"Mensaje": "Bienvenidos a la API de Items"}

@app.get("/items/")
def get_all_items():
    if not items:
        raise HTTPException(status_code=404, detail="Ningún items encontrado")
    
    return{"Items": items}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return {"Item_id": item_id, "item": items[item_id]}

@app.post("/items/")
def create_items(item: Item):
    item_id = len(items) + 1
    items[item_id] = item
    return{"Mensaje": "Item creado", "item_id": item_id, "item": item}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    items[item_id] = item
    return {"mensaje": "Item actualizado", "item_id": item_id, "item": item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    del items[item_id]
    return {"mensaje": f"Item {item_id} eliminado"}

        