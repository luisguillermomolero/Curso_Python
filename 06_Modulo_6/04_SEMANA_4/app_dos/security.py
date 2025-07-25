from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPAuthorizationCredentials
from users_db import fake_users_db, pwd_context

security = HTTPBasic()

def authenticate(credentials: HTTPAuthorizationCredentials = Depends(security)):
    username = credentials.username
    password = credentials.password
    
    user = fake_users_db(username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario no encontrado",
            headers={"www-authenticate": "Basic"}
        )
    
    if not pwd_context.verify(password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Contraseña incorrecta",
            headers={"www-authenticate": "Basic"}
        )
    
    return user