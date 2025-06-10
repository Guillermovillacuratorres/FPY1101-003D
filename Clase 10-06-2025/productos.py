datos = {
    "productos":
    [
        {
            "id":1,
            "nombre":"Smart tv",
            "precio":5990,
            "cantidad":2
        },
        {
            "id":2,
            "nombre":"Iphone",
            "precio":100,
            "cantidad":45
        }
    ],
    "usuarios":
    [
        {
            "id":1,
            "correo":"",
            "edad":10,
            "contrasena":"",
            "colores":["azul","verde","amarillo"]
        }
    ]
}



def buscar_producto(id_producto:int)->dict:
    """Busca un producto y retorna el diccionario del producto encontrado."""
    for i in datos["productos"]:
        if i["id"] == id_producto:
            return i





while True:
    print("1 - Agregar producto")
    print("2 - Mostrar producto")
    print("3 - Editar producto")
    print("4 - Eliminar producto")
    print("5 - Salir")

    opcion = int(input("Seleccione una opción: "))


    if opcion == 1:
        id = int(input("Ingrese el id del producto: "))
        nombre = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        
        producto_agregar = {
            "id":id,
            "nombre":nombre,
            "precio":precio,
            "cantidad":cantidad
        }
        datos["productos"].append(producto_agregar)
        print("Producto agregado exitosamente!")
    
    elif opcion == 2:
        for i in datos["productos"]:
            print(f"NOMBRE: {i["nombre"]} - PRECIO: {i["precio"]}")

    elif opcion == 3:
        id = int(input("Ingrese el id del producto: "))

        pruducto_buscar = buscar_producto(id)
        if pruducto_buscar == None:
            print("Producto no encontrado!")
            continue
    

        nombre = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        pruducto_buscar["nombre"] = nombre
        pruducto_buscar["precio"] = precio
        pruducto_buscar["cantidad"] = cantidad
        print("producto actualizado correctamente!")


    elif opcion == 4:
        id = int(input("Ingrese el id del producto a eliminar: "))
        for i in datos["productos"]:
            if i["id"] == id:
                datos["productos"].remove(i)

    else:
        print("Opcion no valida!")

print(datos["productos"][1]["nombre"])