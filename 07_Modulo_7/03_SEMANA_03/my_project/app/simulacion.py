from jose import jwt
from datetime import datetime, timedelta
from app.config import SECRET_KEY, ALGORITHM

usuario = "usuario1"
rol = "admin"

# Generar el payload con exp como timestamp
payload = {
    "sub": usuario,
    "role": rol,  # <-- aquí debe ser "role"
    "exp": int((datetime.now() + timedelta(minutes=30)).timestamp())
}

token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
print(token)