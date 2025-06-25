from datetime import datetime, timedelta, timezone
from jose  import jwt, JWTError

SECRET_KEY = "cosita_rik"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTE = 30

def crear_token(data: dict, expiracion: int = ACCESS_TOKEN_EXPIRE_MINUTE):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expiracion)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithm=ALGORITHM)
        return payload
    except JWTError:
        return None