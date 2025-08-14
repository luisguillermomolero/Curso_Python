from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from config import SECRET_KEY, ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(f"Payload recibido: {payload}")
        user = payload.get("sub")
        role = payload.get("role")
        print(f"User: {user} - Role: {role}")
        if user is None or role is None:
            raise credential_exception()
        return {"username": user, "role": role}
    except JWTError:
        raise credential_exception()

def credential_exception():
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales invalidas",
        headers={"www-authenticate": "Bearer"},
    )

