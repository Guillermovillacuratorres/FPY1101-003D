contador_producto  = 0
acumulador_total = 0
contador_venta = 0
calculo = 0
PRECIO_PRODUCTO = 100

while True:
    print("[1] - Registrar una nueva venta")
    print("[2] - Ver estadísticas actuales")
    print("[3] - Salir del programa")
    while True:
        try:
            opc = int(input("Seleccione una opcion: "))
            if opc != 1 and opc != 2 and  opc != 3:
                print("Opcion no valida (1-2-3)")
            else:
                break
        except:
            print("Solo se permiten numeros.")
    if opc == 1:
        contador_venta += 1
        while True:
            try:
                cantidad_productos = int(input("Ingrese la cantidad de productos a vender:"))
                if cantidad_productos <= 0:
                    print("No se permiten cantidades menores o iguales a cero.")
                else:
                    break
            except:
                print("Solo se permiten numeros.")
        for i in range(cantidad_productos):
            while True:
                nombre_producto = input("Ingrese el nombre del producto: ")
                if len(nombre_producto) <= 0:
                    print("El nombre del producto no debe estar vacio.")
                else:
                    break
            acumulador_total += PRECIO_PRODUCTO 
            contador_producto += 1
    if opc == 2:
        print(f"El total de las ventas es: ${acumulador_total}")
        print(f"Cantidad ventas {contador_venta}")
        print(f"Contador de productos: {contador_producto}")
        print(f"Calculo: {acumulador_total / contador_venta}")
    if opc == 3:
        break