from fastapi import APIRouter, HTTPException
from models import Task
from data import tasks_db

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Bienvenidos a las API de Items"}

@router.get("/tasks")
def get_tasks():
    return tasks_db

@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks_db:
        if task.id == task_id:
            return {"message": "Task found", "Task": task}
    raise HTTPException(status_code=404, detail="Task not found")

@router.post("/tasks")
def create_task(task: Task):
    tasks_db.append(task)
    return {"message": "Task created", "task": task}

@router.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    for i, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db[i] = updated_task
            return {"message": "Task updated", "task": updated_task}
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db.pop()(i)
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found") 