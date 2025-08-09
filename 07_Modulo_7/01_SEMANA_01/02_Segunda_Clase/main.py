from fastapi import FastAPI, Depends, HTTPException
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "tu_clave_secreta"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
usuarios = {}

def hashear_password(password: str) -> str:
    return pwd_context.hash(password)

def verificar_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def crear_token(data: dict, expiration: int = ACCESS_TOKEN_EXPIRE_MINUTES):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expiration)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

usuarios["admin"] = hashear_password("1234")

class LoginData(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(datos: LoginData):
    user_pass = usuarios.get(datos.username)
    if not user_pass or not verificar_password(datos.password, user_pass):
        raise HTTPException(status_code=400, detail="Credencial Invalida...")
    
    token = crear_token({"sub": datos.username})
    
    return {"acceso token": token, "token_type": "bearer"}

