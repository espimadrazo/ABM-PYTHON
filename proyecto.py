productos = []

modelo_producto = {
    "Nombre": None,
    "Categoría": None,
    "Precio": None
}

numerador= 0

"""
FIXME agregar validación de datos a todos los inputs (lower, entero) if vacio or type num or "Ingrese un valor válido"
FIXME ver lo del numerador (que cada producto tenga su número en la lista)
"""

# MENÚ
print("-- Sistema de Gestión Básica De Productos --")
print("1. Agregar producto")
print("2. Mostrar productos")
print("3. Buscar producto")
print("4. Eliminar producto")
print("5. Salir")

opcion_menu= int(input("Ingrese el número de la opción que desea elegir:"))

while True:
    match opcion_menu:
        case 1:
            while True:
                nuevo_producto = modelo_producto.copy()
                numerador = 0

                carga_producto = input("¿Desea ingresar un producto? S/N").strip().lower()
                if carga_producto == "s":

                    nuevo_producto["Nombre"] = input("Ingrese el nombre del producto").strip()
                    if nuevo_producto["Nombre"] == "":
                        print("Ingrese un nombre válido")
                        continue
                    else:
                        print("Carga exitosa")

                    nuevo_producto["Categoría"] = input("Ingrese la categoría del producto").strip()
                    if nuevo_producto["Categoría"] == "":
                        print("Ingrese una categoría válida")
                        continue
                    else:
                        print("Carga exitosa")

                    nuevo_producto["Precio"] = int(input("Ingrese el precio del producto (sin centavos)"))
                    if nuevo_producto["Precio"] == "":
                        print("Ingrese un precio válido")
                        continue
                    else:
                        print("Carga exitosa")
                        productos.append(nuevo_producto)
                        numerador += 1
                        continue

                elif carga_producto == "n":
                    print("Carga de productos finalizada")
                    break

                else:
                    print("Ingrese una opción válida")
                    continue


        case 2:
            print("Lista total de productos:")
            for producto in productos:
                print(f"{numerador}. {producto}")

        case 3:
            busqueda = input("Ingrese el nombre del producto que desea buscar").strip()

        case 4:
            eliminar = input("Ingrese el número del producto que desea eliminar").strip()

        case 5:
            print("Gestión finalizada")
            break

        case _:
            print("Ingrese una opción válida")
            continue

