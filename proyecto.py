productos = []

modelo_producto = {
    "Nombre": None,
    "Categoría": None,
    "Precio": None
}

"""
FIXME ver lo del numerador (que cada producto tenga su número en la lista)
"""

while True:
    print("-- Sistema de Gestión Básica De Productos --")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion_menu= int(input("Ingrese el número de la opción que desea elegir:").strip())

    match opcion_menu:
        case 1:
            while True:
                nuevo_producto = modelo_producto.copy()
                numerador = 0

                nuevo_producto["Nombre"] = input("Ingrese el nombre del producto").strip().lower()
                if nuevo_producto["Nombre"] == "":
                    print("Ingrese un nombre válido")
                    continue
                else:
                    print("Carga exitosa")

                nuevo_producto["Categoría"] = input("Ingrese la categoría del producto").strip().lower()
                if nuevo_producto["Categoría"] == "":
                    print("Ingrese una categoría válida")
                    continue
                else:
                    print("Carga exitosa")

                nuevo_producto["Precio"] = input("Ingrese el precio del producto sin centavos").strip()
                if (nuevo_producto["Precio"].isdigit()):
                    nuevo_producto["Precio"] = int(nuevo_producto["Precio"])
                    if nuevo_producto["Precio"] <= 0:
                        print("El precio no puede ser 0 o negativo")
                        continue
                else:
                    print("Ingrese un precio válido")
                    continue

                productos.append(nuevo_producto)

                carga_producto = input("¿Desea ingresar otro producto? S/N").strip().lower()
                if carga_producto == "s":
                    continue

                elif carga_producto == "n":
                    print("Carga de productos finalizada")
                    break

                else:
                    print("Ingrese una opción válida")
                    continue

        case 2:
            print("Lista total de productos:")
            for index, x in enumerate(productos, start=1):
                print(index, x)

        case 3:
            busqueda = input("Ingrese el nombre del producto que desea buscar").strip().lower()
            if busqueda == "":
                print("Ingrese un nombre válido")
                continue
            else:
                for producto in productos:
                    if busqueda == producto{"Nombre"}
                    print(producto)
                else:
                    print("Producto no encontrado")
         
        case 4:
            eliminar = input("Ingrese el número del producto que desea eliminar").strip()

        case 5:
            print("Gestión finalizada")
            break

        case _:
            print("Ingrese una opción válida")
            continue

