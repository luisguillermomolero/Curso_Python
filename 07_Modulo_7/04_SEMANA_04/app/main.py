from fastapi import FastAPI
from routes import auth_routes
from core.logger import init_looger
from database.session import Base, engine
from models import user_task

app = FastAPI()

Base.metadata.create_all(bind= engine)
init_looger()
app.include_router(auth_routes.router)
