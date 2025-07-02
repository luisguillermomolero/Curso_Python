from fastapi import APIRouter, Depends
from app.auth.roles import require_role

router = APIRouter()

@router.get("/admin-data")
def get_admin_data(current_user=Depends(require_role("admin"))):
    return {"msg": "Datos solo para administradores"}
