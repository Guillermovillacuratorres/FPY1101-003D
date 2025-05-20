while True:
    try:
        edad = int(input("Ingrese su edad:"))
    except ValueError as e:
        print("Error, no puedes ingresar letras. ")
    else:
        print("No hay error")
        break
    finally:
        print("Yo siempre me ejecuto!!!!")