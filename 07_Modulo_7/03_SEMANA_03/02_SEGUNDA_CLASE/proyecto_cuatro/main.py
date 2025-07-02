from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import logging

logging.basicConfig(
    filename="api.log",
    level= logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = FastAPI()

@app.get("/")
def root():
    return {"mensaje": "API con try y except (HTTPException)"}

@app.get("/divide")
def divide(x: int, y: int):
    try:
        resultado = x / y
        logging.info(f"División exitosa: {x} / {y} = {resultado}")
        return {"resultado": resultado}
    except ZeroDivisionError:
        logging.warning(f"Intento de división por cero: {x} / {y}")
        raise HTTPException(status_code=400, detail="No se puede dividir por cero")

