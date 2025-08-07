from jose import jwt
from datetime import datetime, timezone, timedelta

SECRET_KEY = "tu_clave_secreta"
ALGORITHM = "HS256"

def crear_token(datos: dict, expiracion: int = 30):
    to_encode = datos.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expiracion)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    

datos_usuario ={
    "sub": "usuario123",
    "rol": "admin"
}

token_generado = crear_token(datos_usuario)
print(token_generado)

