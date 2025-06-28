from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from app.config import SECRET_KEY, ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        user = payload.get("sub")

        role = payload.get("role")

        if user is None or role is None:
            raise credentials_exception()

        return {"username": user, "role": role}

    except JWTError:
        raise credentials_exception()

def credentials_exception():
    return HTTPException(
        # Código de estado HTTP 401: No autorizado
        status_code=status.HTTP_401_UNAUTHORIZED,

        # Mensaje de detalle que será enviado en la respuesta
        detail="Credenciales inválidas",

        # Encabezado que indica que se espera un token tipo Bearer en la autenticación
        headers={"WWW-Authenticate": "Bearer"},
    )
