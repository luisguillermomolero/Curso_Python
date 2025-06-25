from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from core.database import get_db
from models.user import User
from auth.auth_service import hashear_password, verificar_password
from auth.auth_handler import crear_token, verificar_token

router = APIRouter()

class LoginData(BaseModel):
    username: str
    password: str

