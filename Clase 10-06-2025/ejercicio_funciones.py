def valida_numero_entero_positivo(mensaje_input:str):
    """Valida un numero que sea positivo y entero."""
    while True:
        try:
            numero = int(input(mensaje_input))
            if numero <= 0:
                print("Solo puede ingresar numeros positivos.")
                continue
            break
        except ValueError:
            print("Solo se permiten numeros enteros.")
    return numero

#edad = valida_numero_entero_positivo("ingrese su edad: ")
#print(edad)


def valida_entrada_texto(mensaje_input:str):
    while True:
        texto = input(mensaje_input)
        if len(texto) > 1:
            print("El largo permitido para el texto es 1.")
            continue
        elif len(texto) == 0:
            print("El texto no puede estar vacio.")
            continue
        
        return texto
        
#valida_entrada_texto("Ingrese A o B o C: ")
        

