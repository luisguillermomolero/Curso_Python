paciente = {
    "identificador1": {"nombre": "Carlos", "especie": "Perro", "edad": 4,"vacuna": True}
    }

# values(), items(), update(), pop(), keys()

# Mostrar cuales son las claves que tiene el diccionario paciente
print("Claves disponibles en el registro del paciente:")
for clave in paciente.keys():
    print(clave)

# Mostrar solo los valores pertenecientes a cada "clave"
print ("Valores disponibles en cada clave:")
for valor in paciente.values():
    print(valor)

paciente.update({
    "edad": 8,
    "especie": "Gaticu"
})

# Mostrar todos los pares clave-valor del diccionarioi paciente
print("Registro de informacion del diccionario paciente")
for clave, valor in paciente.items():
    print(f"clave: {clave} - valor: {valor}")
