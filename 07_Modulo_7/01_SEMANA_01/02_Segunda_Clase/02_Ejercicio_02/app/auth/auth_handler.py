from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError

SECRET_KEY = "clave_super_secreta"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def crear_token(data: dict, expiration: int = ACCESS_TOKEN_EXPIRE_MINUTES):
    to_encode = data.copy()
    expire =  datetime.now(timezone.utc) + timedelta(minutes=expiration)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None

