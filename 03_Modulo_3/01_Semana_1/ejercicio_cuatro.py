ventas_mensuales = [12000, 5000, 14000, 18000, 10000, 20000, 3000, 4000]

ventas_t2 = ventas_mensuales[3:6]
print("Ventas del trimestre 2:", ventas_t2)
ventas_top_lampda = [v for v in ventas_mensuales if v > 13000]
print("Ventas sobresalientes: ", ventas_top_lampda)

