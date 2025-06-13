from jose import jwt
from datetime import datetime, timedelta,timezone
from fastapi import HTTPException
from jwt import PyJWTError 

SECRET_KEY = "clave_de_acceso"
ALGORITMO = "HS256"

def crear_token(datos: dict, expiracion: int = 30):
    to_encode = datos.copy()
    expiracion = datetime.now(timezone.utc) + timedelta(minutes=expiracion)
    to_encode.update({"exp": expiracion})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITMO)

def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITMO])
        return payload
    except PyJWTError:
        raise ValueError("\n\n\nToken invalido o expirado \n\n\n")

datos = {
    "sub": "usuario",
    "rol": "admin"
}

token_generado = crear_token(datos)

print("Token generado: " + token_generado)

try:
    payload = verificar_token(token_generado)
    print("\n\n\nToken verificado con éxito. Contenido:", payload, "\n\n\n")
except Exception as e:
    print("\n\n\nError al verificar el token:", e , "\n\n\n")
        
    