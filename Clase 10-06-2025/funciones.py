#Sin argumentos - sin retorno
def sumar():
    """Muestra la suma de dos numeros."""
    print(1+1)

sumar()


#Con argumentos - sin retorno
def sumar(n1:int,n2:int):
    """Suma dos numeros."""
    print(n1 + n2)

sumar(n2=100,n1=500)

#Sin argumentos - con retorno
def multiplicar() -> int:
    """Multiplica dos numeros"""
    return 10 * 2

multiplicacion = multiplicar()
print(multiplicacion)

#Con argumentos - con retorno
def multiplicar(n1:int,n2:int) -> int:
    """Multiplica dos numeros."""
    return(n1 * n2)

print(multiplicar(9,9))