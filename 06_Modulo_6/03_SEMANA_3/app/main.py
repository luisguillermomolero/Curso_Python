from fastapi import FastAPI
from routes import tarea
from fastapi.responses import Response
from database.init_db import init_db
from database.create import crear_base_de_datos
from config import settings

app = FastAPI()

# Crear la base de datos
crear_base_de_datos(
    settings.DB_NAME,
    settings.DB_USER,
    settings.DB_PASSWORD,
    settings.DB_HOST
)

# Inicializar la base de datos
init_db()

# Incluir las rutas
app.include_router(tarea.router, prefix="/tareas", tags=["Tareas"])

@app.get("/favicon.ico")
async def favicon():
    return Response(status_code=204)

@app.get("/")
def root():
    return {"mensaje": "API de Tareas operativa"}
