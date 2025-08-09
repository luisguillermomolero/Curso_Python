from jose import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "tu_clave_secreta"
ALGORITHM = "HS256" # RS256
data = {
    "sub": "usuario123",
    "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
}

token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

print(f"\nToken:", token)