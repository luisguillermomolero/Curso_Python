from jose import jwt
from jose.exceptions import JWTError
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException

SECRET_KEY =  "tu_clave_secreta"
ALGORITHM = "HS256"

def crear_token(datos: dict, expiracion: int = 30):
    to_encode = datos.copy()
    expire = datetime.now(timezone.utc) +timedelta(minutes=expiracion)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        return payload
    except JWTError:
        raise ValueError("Token invalido o expirado")

datos_usuario = {"sub": "usuario123", "rol": "admin"}

token_generado = crear_token(datos_usuario)
print(f"\n\nToken generado: {token_generado}")

try:
    payload = verificar_token(token_generado)
    print(f"\n\nToken verificado, payload => {payload}\n\n")
except ValueError as e:
    print(f"Error: {e}")

