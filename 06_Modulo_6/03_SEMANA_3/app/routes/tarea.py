from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.tarea import TareaCreate, TareaOut
from crud import tarea as crud_tarea
from database.session import get_db

router = APIRouter()

@router.post("/", response_model=TareaOut)
def crear(tarea: TareaCreate, db: Session = Depends(get_db)):
    return crud_tarea.crear_tarea(db, tarea)

@router.get("/", response_model=list[TareaOut])
def listar(db: Session = Depends(get_db)):
    return crud_tarea.obtener_tarea(db)

@router.get("/{tarea_id}", response_model=TareaOut)
def obtener(tarea_id: int, db: Session = Depends(get_db)):
    tarea = crud_tarea.obtener_tarea(db, tarea_id)
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea

@router.put("/{tarea_id}", response_model=TareaOut)
def actualizar(tarea_id: int, tarea: TareaCreate, db: Session = Depends(get_db)):
    tarea_actualizada =  crud_tarea.actualizar_tarea(db,tarea_id, tarea)
    if not tarea_actualizada:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea_actualizada

@router.delete("/{tarea_id}")
def eliminar(tarea_id: int, db: Session = Depends(get_db)):
    if not crud_tarea.eliminar_tarea(db, tarea_id):
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return {"OK": True}

