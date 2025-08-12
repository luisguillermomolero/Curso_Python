biblioteca = {
    "L001": {
        "titulo": "Cien años de soledad",
        "autor": "Gabriel Garcia Márquez",
        "año": 1967,
        "disponible": True
    },
    "L002": {
      "titulo": "1984",
      "autor": "George Orwell",
      "año": 1949,
      "disponible": False
    },
    "L003":{
      "titulo"  : "Don quijote de la mancha",
      "autor": "Miguel de Cervantes",
      "año": 1605,
      "disponible": True
    }
}

def mostrar_libro(codigo):
    
    if codigo in biblioteca:
        libro = biblioteca[codigo]
        print(f"\nCódigo: {codigo}")
        print(f"Título: {libro['titulo']}")
        print(f"Autor: {libro['autor']}")
        print(f"Año: {libro['año']}")
        estado = "Disponible" if libro["disponible"] else "No disponible"
        print(f"Estado {estado}")
    else:
        print(f"El código {codigo} no fue encontrado")

def cambiar_disponibilidad(codigo):
    if codigo in biblioteca:
        estado_actual = biblioteca[codigo]["disponible"]
        biblioteca[codigo]["disponible"] = not estado_actual
        nuevo_estado = "Disponible" if not estado_actual else "No disponible"
        print(f"\nEstado actualizado del libro {codigo}: {nuevo_estado}")
    else:
        print(f"El código {codigo} no fue encontrado y no cambia la disponibilidad")

def main():
    mostrar_libro("L001")
    cambiar_disponibilidad("L001")
    mostrar_libro("L001")
    mostrar_libro("L999")
    cambiar_disponibilidad("L999")

if __name__ == "__main__":
    main()
    