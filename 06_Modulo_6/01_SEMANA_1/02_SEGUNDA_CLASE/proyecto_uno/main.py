from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

items= {}

class Item(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    impuesto: Optional[float] = None

# Rutas (endpoints)

@app.get("/")
def root():
    return {"message": "Bienvenidos a las API de Items"}

@app.get("/items/")
def get_all_items():
    if not items:
        raise HTTPException(status_code=404, detail="No hay items que mostrar")
    return {"items": items}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Items no encontrado")
    return {"item_id": item_id, "item": items[item_id]}
        
@app.post("/items/")
def create_item(item: Item):
    item_id = len(items) + 1
    items[item_id] = item
    return {"mensaje": "Item creado", "item_id": item_id, "item": item}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Items no encontrado")
    items[item_id] = item
    return {"message": "Item actualizado con éxito", "item_id": item_id, "item": item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Items no encontrado")
    del items[item_id]
    return {"menssage": f"Item {item_id} eliminado"}
        
    