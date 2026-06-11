diccionario = {
    "prducto1":[1,"producto-nombre",100,1500],
    "producto2": [2,"mouse",200,3000],
    "producto3": [2,"mouse",200,3000],
    "producto4": [2,"mouse",200,3000],
    "producto5": [2,"mouse",200,3000],
    "producto6": [2,"mouse",200,3000],
    "producto7": [2,"mouse",200,3000],
    "producto8": [2,"mouse",200,3000],
}

diccionario["prducto1"][1]="hola"

print(diccionario["producto2"][1])

contador = 0
for c,v in diccionario.items():
    if v[1] == "mouse":
        contador+=1
print("CONTADOR: ", contador)



print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())

