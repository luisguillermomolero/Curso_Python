from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "mi_super_contrasena"
ALGORITHM = "HS256"

data = {
    "sub": "Carlitos",
    "role": "admin",
    "exp": datetime.now() + timedelta(minutes=30)
}

token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

print(token)