from fastapi import FastAPI
from routers import users, admin
from middleware.validate_token import ValidateTokenMiddleware

app = FastAPI()

app.add_middleware(ValidateTokenMiddleware)

app.include_router(users.router)
app.include_router(admin.router)

