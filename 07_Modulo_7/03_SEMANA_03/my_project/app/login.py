from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "super_clave"
ALGORITHM = "HS256"

data = {
    "sub": "Carlitos",
    "role": "admin",
    "exp": datetime.now() + timedelta(minutes=30)
}

token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

print(token)