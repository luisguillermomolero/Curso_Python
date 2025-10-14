import subprocess
import sys

# Lista de dependencias necesarias para el proyecto
# Versiones compatibles para evitar errores de bcrypt con passlib
dependencias = [
    "python-jose[cryptography]\n",
    "passlib\n",
    "bcrypt\n",
    "fastapi[standard]\n",
    "uvicorn[standard]\n",
    "sqlalchemy\n",
    "psycopg2-binary\n",
    "python-dotenv\n",
    "pydantic\n",
    "pydantic-settings\n",
    "python-multipart\n"
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
print("\nActualizando pyasn1-modules...\n")

try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pyasn1-modules"])
    print("\npyasn1-modules actualizado correctamente")
except subprocess.CalledProcessError as e:
    print(f"\nAdvertencia: No se pudo actualizar pyasn1-modules: {e}")

print("\nInstalando dependencias del proyecto...\n")

try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    print("\n¡Dependencias instaladas exitosamente!")
except subprocess.CalledProcessError as e:
    print(f"\nError al instalar dependencias: {e}")
except Exception as e:
    print(f"\nError inesperado: {e}")

# Mostrar versiones instaladas
print("\n" + "─" * 50)
print("\nVERSIONES INSTALADAS:")
print("─" * 50)

# Lista de paquetes principales a verificar
paquetes_principales = [
    "python-jose",
    "passlib",
    "bcrypt",
    "fastapi",
    "uvicorn",
    "sqlalchemy",
    "psycopg2-binary",
    "python-dotenv",
    "pydantic",
    "pydantic-settings",
    "python-multipart"
]

for paquete in paquetes_principales:
    try:
        resultado = subprocess.check_output(
            [sys.executable, "-m", "pip", "show", paquete],
            stderr=subprocess.STDOUT
        ).decode()
        
        # Extraer la versión del resultado
        for linea in resultado.split('\n'):
            if linea.startswith('Version:'):
                version = linea.split(':', 1)[1].strip()
                print(f"  {paquete:<25} {version}")
                break
    except subprocess.CalledProcessError:
        print(f"  {paquete:<25} No instalado")

print("─" * 50)
