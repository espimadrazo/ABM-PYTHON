import functions
import colorama

# Variables de almacenamiento
productos = []

# Programa
while True:
    functions.menu()

    opcion_menu= int(input("Ingrese el número de la opción que desea elegir: ").strip())

    match opcion_menu:

        # Agregar producto
        case 1:
            producto = functions.agregar_producto()
            productos.append(producto)
            print(colorama.Fore.GREEN + "Carga final de producto exitosa, para agregar otro vuelva a seleccionar opción 1" + colorama.Style.RESET_ALL)

        # Mostrar productos
        case 2:
            functions.mostrar_productos(productos)

        # Buscar producto
        case 3:
            functions.buscar_productos(productos)

        # Eliminar producto
        case 4:
            functions.mostrar_productos(productos)
            functions.eliminar_producto(productos)

        # Salir
        case 5:
            functions.terminar_programa()
            break

        case _:
            print("Ingrese una opción válida")
            continue

