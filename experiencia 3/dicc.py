diccionario = {
    "nombre":"Juanito",
    "apellido":"Dias",
    "juegos_favoritos":["Minecraft", "Roblox"],
     "edad":12,
    "casado":False,
    "hermanos":[
        {
            "nombre":"Dieguito",
            "apellido":"Dias"
        },
        {
            "nombre":"Pedrito",
            "apellido":"Dias"
        }
    ]
}
print(diccionario["hermanos"][1]["nombre"])

for i in diccionario["hermanos"]:
    print(i["nombre"])