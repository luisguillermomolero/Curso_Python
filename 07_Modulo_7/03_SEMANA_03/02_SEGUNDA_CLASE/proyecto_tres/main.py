from fastapi import FastAPI, Request
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
    return {"mensaje": "API con prueba de logs"}

@app.get("/log")
def log_demo():
    logging.info("Log de prueba desde la API Restful")
    return {"mensaje": "Log generado correctamente"}
