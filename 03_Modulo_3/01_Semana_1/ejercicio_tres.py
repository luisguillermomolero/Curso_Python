def registrar_empleado(nombre, cargo, salario):
    if not nombre or not cargo or salario <= 0:
        raise ValueError("Datos invalidos")
    return (nombre.title(), cargo.title(), float(salario))

def mostrar_emplados(empleados):
    print("\nRegistro de contratos laborales:")
    for i, emp in enumerate(empleados, start=1):
        nombre, cargo, salario = emp
        print(f"{i}. {nombre} - {cargo} - ${salario:.2f}")

def main():
    empleados = []
    
    try:
        empleados.append(registrar_empleado("Ana Garia", "Ingeniera de softfware", 8500))
        empleados.append(registrar_empleado("Luis Pérez", "Analista de datos", 8000))
        empleados.append(registrar_empleado("Juan González","Gerente de servicios", 12000))
        empleados.append(registrar_empleado("Leidy Saenz","Gerente de ventas", 9000))
    except ValueError as e:
        print(e)
        
    mostrar_emplados(empleados)

if __name__ == "__main__":
    main()
