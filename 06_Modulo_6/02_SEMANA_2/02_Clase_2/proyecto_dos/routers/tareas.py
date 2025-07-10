from fastapi import APIRouter
from models import TareaEntrada, TareaSaliente

router = APIRouter()

tareas_db = []
id_actual = 1

@router.post("/tareas", response_model=TareaSaliente)
def crear_tarea(tarea: TareaEntrada):
    global id_actual
    nueva_tarea = TareaSaliente(id=id_actual,
                                titulo=tarea.titulo,
                                descripcion=tarea.descripcion,
                                completado=False
                                )
    tareas_db.append(nueva_tarea)
    id_actual += 1
    return nueva_tarea

@router.get("/tareas", response_model=list[TareaSaliente])
def listar_tareas():
    return tareas_db

