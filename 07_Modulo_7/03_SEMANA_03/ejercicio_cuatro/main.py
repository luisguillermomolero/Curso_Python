from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import logging

logging.basicConfig(
    filename="response.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = FastAPI()

@app.get("/")
def root():
    return{"mensaje":"Bienvenido"}

@app.get("/divide")
def divide(x: int, y: int):
    try:
        resultado = x / y
        logging.info(f"División exitosa: {x} / {y} = {resultado}")
        return {"resultado": resultado}
    except ZeroDivisionError:
        logging.warning(f"No se puede calcular división por cero: {x} / {y}")
        raise HTTPException(status_code=400, detail="No se puede dividir por cero")