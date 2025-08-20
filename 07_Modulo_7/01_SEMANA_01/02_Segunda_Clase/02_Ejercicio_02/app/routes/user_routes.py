from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from core.database import get_db
from models.user import User
from auth.auth_service import hashear_password, verificar_password
from auth.auth_handler import crear_token

router = APIRouter()

class LoginData(BaseModel):
    username: str
    password: str

@router.post("/register")
def register(data: LoginData, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == data.username).first()
    if user:
        raise HTTPException(status_code=400, detail="Usuario ya existe")
    hashed = hashear_password(data.password)
    nuevo_usuario = User(username= data.username, hashed_password=hashed)
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return{"mensaje": "Usuario registrado exitosamente"}

@router.post("/login")
def login(data: LoginData, db: Session = Depends(get_db)):
    user = db.query(User). filter(User.username == data.username).first()
    if not user or not verificar_password(data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Credencial inválida")
    token = crear_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

