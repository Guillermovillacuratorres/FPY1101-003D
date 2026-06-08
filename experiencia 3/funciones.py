#Sin parametros - sin retorno
def sumar_dos_numeros():
    """Sumar dos numeros enteros"""
    print(10 + 10)


#Con argumentos - sin retorno
def sumar_dos_numeros_2(n1:int,n2:int):
    print(n1 + n2)

#Sin argumentos - con retorno
def sumar_dos_numeros_3()-> int:
    return 10 + 10




#Con argumentos - con retorno
def sumar_dos_numeros_4(n1, n2):
    return n1 + n2


sumar_dos_numeros()
sumar_dos_numeros_2(20,20)
resultado = sumar_dos_numeros_3()

print(resultado)



print()