from fastapi import FastAPI
import logging

logging.basicConfig(
    filename="api.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = FastAPI()

@app.get("/")
def root():
    return {"mensaje": "Bienvenido"}

@app.get("/log")
def log_demo():
    logging.info("Mensaje de prueba de logs informativos")
    return {"mensaje": "log generado de forma correcta"}
