def mostrar_clientes(lista_clientes):
    for cliente in lista_clientes:
        print(f"- {cliente}")

def agregar_cliente(lista_clientes, nombre):
    
    # validacion de datos de entrada
    if isinstance(nombre, str) and 2 <= len(nombre) <= 50:
        lista_clientes.append(nombre.title())
        print(f"Cliente agregado: {nombre.title()}")
    else:
        print("Nombre invalido. El nombre debe tener una logitud mayor a 2 y menor de 50 caracteres")

def modificar_cliente(lista_clientes, indice, nuevo_nombre):
    if not (isinstance(nuevo_nombre, str) and 2 <= len(nuevo_nombre) <= 50):
        print("Nombre invalido. El nombre debe tener una logitud mayor a 2 y menor de 50 caracteres")
        return
    
    if 0 <= indice < len(lista_clientes):
        original = lista_clientes[indice]
        lista_clientes[indice] = nuevo_nombre.title()
        print(f"El cliente {original} fue modificado con éxitos. Nuevo nombre: {nuevo_nombre.title()}")
    else:
        print("Indice fuera de rango...")
    

def main():
    clientes = ["Ana", "Camila", "Alejandro", "David"]
    
    print("Clientes actuales:")
    mostrar_clientes(clientes)
    
    agregar_cliente(clientes, "emanuel")
    print("Lista de clientes actualizada:")
    mostrar_clientes(clientes)
    
    modificar_cliente(clientes, 4, "sardanapalo")
    print("Lista de clientes actualizada:")
    mostrar_clientes(clientes)

if __name__ == "__main__":
    main()
