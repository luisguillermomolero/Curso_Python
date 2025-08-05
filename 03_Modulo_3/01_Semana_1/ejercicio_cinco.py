def agregar_turno(turnos, nombre, dia, turno):
    if not nombre or not dia or not turno:
        raise ValueError("Todos los campos son obligatorios")
    turnos.append([nombre.title(), dia.title(), turno.title()])

def insertar_turno(turnos, indice, nombre, dia, turno):
    if not nombre or not dia or not turno:
        raise ValueError("Todos los campos son obligatorios")
    if indice < 0 or indice > len(turnos):
        raise IndexError(f"El indice superior es de {len(turnos)} turnos registrados")
    turnos.insert(indice, [nombre.title(), dia.title(), turno.title()])
    
def eliminar_turno_por_nombre(turnos, nombre):
    for t in turnos:
        if t[0] == nombre.title():
            turnos.remove(t)
            return
    raise ValueError(f"El empleado {nombre} no existe")

def eliminar_ultimo_turno(turnos):
    if not turnos:
        raise IndexError("No hay turnos para eliminar")
    return turnos.pop()

def mostrar_turnos(turnos):
    print("\nTurnos asignados:")
    for t in turnos:
        print(f"{t[0]} - {t[1]} - {t[2]}")

def main():
    turnos = []
    
    try:
        agregar_turno(turnos, "Dayana", "Lunes", "Mañana")
        agregar_turno(turnos, "Andres", "Miercoles", "Noche")
        agregar_turno(turnos, "Walter", "Jueves", "Mañana")
        agregar_turno(turnos, "Alberto", "Viernes", "Noche")
        agregar_turno(turnos, "Luis", "Sábado", "Dia")
        mostrar_turnos(turnos)
        
        insertar_turno(turnos, 1, "Arley", "Martes", "Mañana")
        mostrar_turnos(turnos)
        
        eliminar_ultimo_turno(turnos)
        
        mostrar_turnos(turnos)
        
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")
    
if __name__ == "__main__":
    main()