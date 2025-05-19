from database.base import Base, engine
from models.tarea import Tarea  # Asegúrate de tener este modelo

def init_db():
    Base.metadata.create_all(bind=engine)
    print("Base de datos inicializada correctamente")

if __name__ == "__main__":
    init_db()
