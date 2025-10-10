import subprocess
import sys

# Lista de dependencias necesarias para el proyecto
# Versiones compatibles para evitar errores de bcrypt con passlib
dependencias = [
    "python-jose[cryptography]==3.3.0\n",
    "passlib[bcrypt]==1.7.4\n",
    "bcrypt==4.0.1\n",  # Versión compatible con passlib 1.7.4
    "fastapi\n",
    "uvicorn\n",
    "pydantic\n",
    "sqlalchemy==2.0.23\n",
    "psycopg2-binary==2.9.9\n",
    "python-dotenv==1.0.0\n",
    "python-multipart==0.0.6\n",
    "pydantic-settings==2.1.0"
]

# Crear y escribir el archivo requirements.txt
with open("requirements.txt", "w", encoding="utf-8") as archivo:
    archivo.writelines(dependencias)

print("Archivo 'requirements.txt' generado exitosamente")
print("\nContenido generado:")
print("─" * 50)
with open("requirements.txt", "r", encoding="utf-8") as archivo:
    print(archivo.read())

# Instalar las dependencias
print("─" * 50)
print("\nInstalando dependencias...\n")

try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    print("\n¡Dependencias instaladas exitosamente!")
except subprocess.CalledProcessError as e:
    print(f"\nError al instalar dependencias: {e}")
except Exception as e:
    print(f"\nError inesperado: {e}")

