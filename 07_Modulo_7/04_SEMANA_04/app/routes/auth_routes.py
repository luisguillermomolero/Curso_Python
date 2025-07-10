from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database.session import get_db
from services.auth_service import create_user, authenticate_user, create_access_token, get_current_user
from schemas.user_task import UserCreate, UserOut, Token
from models.user_task import User

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    if len(user.username) < 4 or len(user.username) >20:
        raise HTTPException(status_code=400, detail="El nombre de usuario debe ser mayor a 4 y menor a 20 caracteres")
    if len(user.password) < 6:
        raise HTTPException(status_code=400, detail="La contraseña debe ser mayor a seis caracteres")
    if user.role not in ["user", "admin"]:
        raise HTTPException(status_code=400, detail="Rol invalido")
    return create_user(user, db)

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm =  Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales invalidas")
    token =  create_access_token({"sub": user.username, "role": user.role}, db)
    return{"access_token": token, "token_type": "bearer"}    

@router.get("/me", response_model=UserOut)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.get("/admin")
def admin_route(current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Solo administradores")
    return {"msg": f"Bienvenido, admin {current_user.username}"}

    