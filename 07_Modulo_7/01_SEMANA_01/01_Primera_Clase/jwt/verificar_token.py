from jose import jwt
from jose.exceptions import JWTError
from fastapi import HTTPException

SECRET_KEY = "tu_clave_secreta"
ALGORITHM = "HS256"

def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        return payload
    except JWTError:
        raise ValueError("Token inválido")

token_ejemplo ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c3VhcmlvMTIzIiwicm9sIjoiYWRtaW4iLCJleHAiOjE3NTQ0NDcxNTN9.1VSEjy-QOYVwsZ5H8qbg9CIM-EMPLNeyPDc06f0hfuY"

try:
    contenido =  verificar_token(token_ejemplo)
    print("Token verificado con éxito:", contenido)
except Exception as e:
    print("Error al verificar el token:", e)
    
