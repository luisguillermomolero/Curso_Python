from fastapi import FastAPI, Depends
from secutiry import authenticate

app = FastAPI()

@app.get("/")
def public_route():
    return {"message": "Bienvenido a nuestra API Pública sin contraseña"}

@app.get("/private")
def private_route(user: str = Depends(authenticate)):
    return {"message": f"Bienvenido {user} a nuestra API privada (protegida)"}

