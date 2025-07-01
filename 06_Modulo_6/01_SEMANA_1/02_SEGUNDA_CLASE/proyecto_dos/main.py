from fastapi import FastAPI
from routes import router

app = FastAPI(title="Task system", description="Task API Restful")

app.include_router(router)