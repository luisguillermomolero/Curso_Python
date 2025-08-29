from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import logging

logging.basicConfig(
    filename="auditoria.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = FastAPI(
    title="My API",
    description="Example",
    version="1.0"
)

class Factura(BaseModel):
    cliente: str
    total: float
    cantidad: int

facturas_db = {}
id_contador = 1


@app.middleware("http")
async def catch_all_exceptions(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        logging.error(f"Error interno del servidor: {str(e)}")
        return JSONResponse(status_code=500, content={"detalle": "Error interno del servidor"})

@app.get("/")
def root():
    return{"mensaje": "Bienvenidos"}

@app.post("/facturas")
def crear_factura(factura: Factura):
    global id_contador
    
    if factura.total < 0:
        raise HTTPException(status_code=400, detail="El total debe ser mayor a cero")
    
    if factura.cantidad <= 0:
        raise HTTPException(status_code=400, detail="La cantidad debe ser mayor a cero")
    
    factura_id = id_contador
    facturas_db[factura_id] = factura
    id_contador += 1
    
    precio_unitario = factura.total / factura.cantidad
    logging.info(f"Factura creada con éxito - Id: {factura_id} - Cliente: {factura.cliente} - Total: {factura.total:.2f} - Cantidad: {factura.cantidad} - Precio Unitario: {precio_unitario:.2f}")
    
    return {
        "id": factura_id,
        "cliente": factura.cliente,
        "precio_unitario": precio_unitario,
        "Total": factura.total
    }

@app.get("/facturas")
def obtener_facturas():
    return {
        "total": len(facturas_db),
        "facturas": [
            {
                "id": fid,
                "cliente": f.cliente,
                "total": f.total,
                "cantidad": f.cantidad,
                "precio_unitario": round(f.total / f.cantidad, 2)
            } for fid, f in facturas_db.items()
        ]
    }

@app.get("/facturas/{factura_id}")
def obtener_factura(factura_id: int):
    factura = facturas_db.get(factura_id)
    if not factura:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    return {
        "id": factura_id,
        "cliente": factura.cliente,
        "total": factura.total,
        "cantidad": factura.cantidad,
        "precio_unitario": round(factura.total / factura.cantidad, 2)
    }

@app.put("/facturas/{factura_id}")
def actualizar_factura(factura_id: int, factura: Factura):
    if factura_id not in facturas_db:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    if factura.total < 0 or factura.cantidad <= 0:
        raise HTTPException(status_code=400, detail="Datos invalidos")
    facturas_db[factura_id] = factura
    return {"mensaje": F"Factura {factura_id} actualizada correctamente"}

@app.delete("/facturas/{factura_id}")
def eliminar_factura(factura_id: int):
    if factura_id not in facturas_db:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    del facturas_db[factura_id]
    return {"mensaje": f"La factura {factura_id} fue eliminada"}

