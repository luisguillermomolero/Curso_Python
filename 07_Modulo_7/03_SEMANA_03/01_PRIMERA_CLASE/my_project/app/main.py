from fastapi import FastAPI
from app.routers import users, admin
from app.middleware.validate_token import ValidateTokenMiddleware

app = FastAPI()

# Middleware personalizado
app.add_middleware(ValidateTokenMiddleware)

# Routers
app.include_router(users.router)
app.include_router(admin.router)
