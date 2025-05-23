from sqlalchemy.orm import sessionmaker
from database.base import engine

SessionLocal = sessionmaker(autocommint=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()