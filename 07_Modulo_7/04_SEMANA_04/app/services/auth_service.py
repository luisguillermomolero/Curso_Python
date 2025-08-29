from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from models.user_task import User
from schemas.user_task import UserCreate
from core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from database.session import get_db

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def create_user(user: UserCreate, db: Session):
    hashed_pw = pwd_context.hash(user.username)
    db_user = User(username=user.username, hashed_password=hashed_pw, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(username: str, password: str, db: Session):
    user = db.query(User).filter_by(username=username).first()
    if not user or not pwd_context.verify(password, user.hashed_password):
        return None
    return user

def create_access_token(data: dict, db: Session):
    to_encode = data.copy()()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user = db.query(User).filter_by(username=payload["sub"]).first()
        if user is None:
            raise HTTPException(status_code=403, detail="Usuario no fue encontrado")
        return user
    except JWTError:
        raise HTTPException(status_code=403, detail="Token invalido")


    