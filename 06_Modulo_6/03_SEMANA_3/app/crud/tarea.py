from sqlalchemy.orm import Session
from models.tarea import Tarea
from schemas.tarea import TareaCreada

def crear_tarea(db: Session, tarea: TareaCreada):
    db_tarea = Tarea(**tarea.model_dump())
    db.add(db_tarea)
    db.commit()
    db.refresh(db_tarea)
    return db_tarea

def obtener_tareas(db: Session):
    return db.query(Tarea).all()

def obtener_tarea(db: Session, tarea_id: int):
    return db.query(Tarea).filter(Tarea.id == tarea_id).first()

def actualizar_tarea(db: Session, tarea_id: int, tarea_data: TareaCreada):
    tarea = db.query(Tarea).filter(Tarea.id == tarea_id).first()
    if tarea:
        for attr, value in tarea_data.dict().items():
            setattr(tarea, attr, value)
        db.commit()
        db.refresh()
    return tarea

def eliminar_tarea(db: Session, tarea_id: int):
    tarea = db.query(Tarea).filter(Tarea.id == tarea_id).first()
    if tarea:
        db.delete(tarea)
        db.commit()
    return tarea