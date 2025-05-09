from fastapi import FastAPI
from routers import tareas

app = FastAPI(title="API de Tareas")

app.include_router(tareas.router)

@app.get("/")
def leer_raiz():
    return {"mensaje": "Bienvenidos a la API de tareas."}