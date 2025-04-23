peso = float(input("Ingrese su peso (KG):"))
altura = float(input("Ingrese su altura (Mts):"))

imc = peso / (altura * altura)

# peso 96  - altura 1.72  *2 2,9584   imc = 

if imc < 18.5:
    print("Bajo peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Peso normal")
elif imc >= 25 and imc <= 29.9:
    print("Sobrepeso")
else:
    print("Obesidad",imc)

