def valida_numero():
    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion < 0:
                print("El valor no debe ser negativo.")
            elif opcion == 0:
                print("El valor no debe ser cero.")
            else:
                return opcion
        except:
            print("Solo se permiten numeros enteros")

def valida_string(msg:str):
    while True:
        valor = input(msg)
        if len(valor) < 0:
            print("El largo minimo es mayos a cero.")
        elif valor.isalpha() == False:
            print("Solo puede contener letras")
        else:
            return valor



lista = []


def agregar_elemento_lista(nombre:str):
    lista.append(nombre)

def mostrar_elementos_lista():
    contador = 0
    for i in lista:
        contador += 1
        print(f"[{contador}] - {i}")


while True:
    print("Sumar dos numeros")
    print("Agregar un elemento a la lista")
    print("Mostrar lista")
    print("opcion 3 ")

    opcion = valida_numero()

    if opcion == 1:
        n1 = valida_numero()
        n2 = valida_numero()

        print("La suma de los dos numeros es: ", n1 + n2)
    elif opcion == 2:
        valor = valida_string("Ingrese un nombre: ")
        agregar_elemento_lista(valor)
    elif opcion == 3:
        mostrar_elementos_lista()
    elif opcion == 4:
        break