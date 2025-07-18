import sqlite3
import functions
import colorama

# Creación de tabla en base de datos
functions.crear_base_de_datos()

# Programa
while True:
    functions.menu()

    try:
        opcion_menu= int(input("Ingrese el número de la opción que desea elegir: ").strip())
        match opcion_menu:
            # Agregar producto
            case 1:
                functions.agregar_producto()

            # Mostrar total de productos
            case 2:
                functions.mostrar_productos()

            # Buscar producto
            case 3:
                functions.buscar_productos()

            # Modificar datos de producto
            case 4:
                functions.consultar_modificacion_datos()

            # Filtrar productos por cantidad
            case 5:
                functions.filtrar_productos_por_cantidad()

            # Eliminar producto
            case 6:
                functions.eliminar_producto()

            # Salir
            case 7:
                functions.terminar_programa()
                break

            case _:
                functions.imprimir_error_opcion()

    except ValueError:
        print(colorama.Fore.RED + "Ingrese un número de opción" + colorama.Style.RESET_ALL)

    except Exception as error:
        print(f"Ha ocurrido un error: {error}")




