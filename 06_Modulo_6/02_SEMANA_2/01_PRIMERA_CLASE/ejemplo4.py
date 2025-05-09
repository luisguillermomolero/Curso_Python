# Respuestas personalizadas con JSONResponse

from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

class ProductoEntrante(BaseModel):
    nombre: str
    precio: float

# .dict: pydantic v1
# .model_dump: pydantic v2

# Respuestas personalizadas con JSONResponse
@app.post("/producto")
def crear_producto(producto: ProductoEntrante):
    return JSONResponse(
        status_code=status.HTTP_201_CREATED, content=
        {
            "mensaje": "Producto creado", 
            "producto": producto.model_dump()
        }
        )

# Personalizar errores con HTTPException
@app.get("/producto/{id}")
def obtener_producto(id: int):
    if id != 1:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {
              "id": id, 
              "nombre": "Monitor"
           }
