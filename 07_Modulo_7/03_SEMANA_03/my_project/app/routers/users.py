from fastapi import APIRouter, Depends
from app.auth.roles import get_current_user

router = APIRouter()

@router.get("/datos-usuario")
def get_user_data(current_user: dict = Depends(get_current_user)):
    return {
        "usuario_actual":current_user["username"],
        "rol": current_user["role"]
    }

