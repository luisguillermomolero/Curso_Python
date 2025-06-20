from passlib.context import CryptContext

CONTEXT_SCHEME = "bcrypt"
pwd_context = CryptContext(schemes=[CONTEXT_SCHEME], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verificar_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

contrasena_segura = "Mi super CLAVE"

hashear_clave_de_acceso = hash_password(contrasena_segura)
print("\n\n\nHash generado: ", hashear_clave_de_acceso, "\n\n\n")

clave_acceso = input("Ingrese su contraseña: ")

if verificar_password(clave_acceso, hashear_clave_de_acceso):
    print("¡Access granted!")
else:
    print("!Contraseña invalida!")