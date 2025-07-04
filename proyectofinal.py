import sqlite3
import functions
import colorama

# Conexión a base de datos
connection = sqlite3.connect("productos.db")
cursor = connection.cursor()

# Creación de tabla en base de datos
cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        categoría TEXT NOT NULL,
        precio INTEGER NOT NULL
    )
""")

# Programa
while True:
    functions.menu()

    try:
        opcion_menu= int(input("Ingrese el número de la opción que desea elegir: ").strip())
        match opcion_menu:
            # Agregar producto
            case 1:
                producto = functions.agregar_producto()

            # Mostrar productos
            case 2:
                functions.mostrar_productos()

            # Buscar producto
            case 3:
                functions.buscar_productos()

            # Modificar precio producto
            case 4:
                functions.mostrar_productos()
                functions.modificar_precio()

            # Eliminar producto
            case 5:
                functions.mostrar_productos()
                functions.eliminar_producto()

            # Salir
            case 6:
                functions.terminar_programa()
                break

            case _:
                functions.imprimir_error_opcion()

    except ValueError:
        print(colorama.Fore.RED + "Ingrese un número" + colorama.Style.RESET_ALL)



