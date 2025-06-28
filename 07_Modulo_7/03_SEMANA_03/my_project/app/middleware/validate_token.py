from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from fastapi.responses import JSONResponse
class ValidateTokenMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        if request.url.path.startswith("/admin"):

            token = request.headers.get("Authorization")

            if token is None:
                return JSONResponse(
                    status_code=401,
                    content={"detail": "Token requerido"}
                )

        return await call_next(request)
