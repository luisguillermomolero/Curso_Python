from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import requests
from fastapi.responses import JSONResponse

class ValidateTokenMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        if request.url.path.startswith("/admin"):
            token = request.headers.get("Authorization")
            if token in None:
                return JSONResponse(
                    status_code=401,
                    content={"detail": "Token requerido"}
                )
        
        return await call_next(request)