tabla = int(input("Ingrese la tabla que desea multiplicar:"))
cantMultiplicar = int(input("Ingrese la cantidad que desea multiplicar:"))
for i in range(cantMultiplicar):
    print(f"{tabla} X {i+1} = {tabla * (i+1)}")