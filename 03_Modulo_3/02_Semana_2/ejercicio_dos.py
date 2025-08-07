usuarios = {
    "usuario001": {"nombre":"Pedro", "telefono": 231564, "correo": "luis@gmail", "roles": ["admin"]},
    "usuario002": {"nombre":"Luis", "telefono": 87654321, "correo": "carlos@hotmail", "roles": ["cliente"]},
}

print(f"Nombre del usuario usuario001: {usuarios["usuario001"]["nombre"]}")

usuarios["usuario003"] = {
    "nombre":"Miguel", "telefono": 65487, "correo": "Miguel@gmail", "roles": ["admin", "soporte"],
}

print("Listado de usuarios registrados: ")
for user_id, datos in usuarios.items():
    print(f"Usuario: {user_id} - Información: {datos}")

print("Usuarios con rol de admin")
for user_id, datos in usuarios.items():
    if "admin" in datos.get("roles", []):
        print(f"Usuario - {user_id} - {datos['nombre']}")

