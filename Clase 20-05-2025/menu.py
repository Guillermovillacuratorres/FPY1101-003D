while True:
    try:
        numero_uno = int(input("Ingrese el primer número:"))
        numero_dos = int(input("Ingrese el segundo número:"))
        break
    except ValueError:
        print("Error, Solo se permiten numeros enteros")
        continue


while True:
    print("*** MENU ****")
    print("[1] - Sumar")
    print("[2] - Restar")
    print("[3] - Multiplicar")
    print("[4] - Salir")
    try:
        opcion = int(input("Ingrese una opción:"))
    except ValueError:
        print("Error, Solo se permiten numeros enteros")
        continue
    if opcion == 1:
        print("El resultado de la suma es: ", numero_dos + numero_uno)
    elif opcion == 2:
        print("El resultado de la resta es: ", numero_dos - numero_uno)
    elif opcion == 3:
        print("El resultado de la multiplicación es: ", numero_dos * numero_uno)
    elif opcion == 4:
        print("Saliendo!!!!!!")
        break
    else:
        print("La opción ingresada no es valida, debe estar en el rango de 1 a 4.")