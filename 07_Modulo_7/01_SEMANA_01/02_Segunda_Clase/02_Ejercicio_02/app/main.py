from fastapi import FastAPI, HTTPException
from core.database import Base, engine
from routes.user_routes import router as user_router
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

app = FastAPI()

try:
    Base.metadata.create_all(bind=engine)
    logger.info("Base de datos inicializada correctamente")
except Exception as e:
    logger.error(f"Error al inicializar la base de datos: {str(e)}")
    raise

app.include_router(user_router, prefix="/api/v1")