import colorama
import sqlite3

# MENU
def menu():
    print("--Sistema de Gestión Básica De Productos--")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Modificar precio de producto")
    print("5. Eliminar producto")
    print("6. Salir")

# AGREGAR PRODUCTO
def agregar_producto():
    try:
        colorama.init()

        while True:
            conexion = sqlite3.connect("productos.db")
            cursor = conexion.cursor()

            nombre = input("Ingrese el nombre del producto: ").strip().lower()
            if nombre == "":
                print(colorama.Fore.RED + "Ingrese un nombre" + colorama.Style.RESET_ALL)
                continue
            else:
                print(colorama.Fore.GREEN + "Carga exitosa" + colorama.Style.RESET_ALL)

            categoria = input("Ingrese la categoría del producto: ").strip().lower()
            if categoria == "":
                print(colorama.Fore.RED + "Ingrese una categoría" + colorama.Style.RESET_ALL)
                continue
            else:
                print(colorama.Fore.GREEN + "Carga exitosa" + colorama.Style.RESET_ALL)

            precio = input("Ingrese el precio del producto sin '$' y sin centavos: ").strip()
            if precio.isdigit():
                precio = int(precio)
                if precio <= 0:
                    print(colorama.Fore.RED + "El precio no puede ser 0 o negativo" + colorama.Style.RESET_ALL)
                    continue
            else:
                print(colorama.Fore.RED + "Ingrese un precio válido" + colorama.Style.RESET_ALL)
                continue

            cursor.execute("INSERT INTO productos (nombre, categoría, precio) VALUES(?, ?, ?)", (nombre, categoria, precio))
            print(colorama.Fore.GREEN + "Carga final de producto exitosa" + colorama.Style.RESET_ALL)

            pregunta = input("¿Desea agregar otro producto? S/N").lower()
            if pregunta == "s":
                continue
            elif pregunta == "n":
                break
            else:
                print("Ingrese una opción válida")

        conexion.commit()

    except sqlite3.Error as e:
        print(f"Error: {e}")
        conexion.rollback()

    finally:
        conexion.close()

# MOSTRAR PRODUCTOS
def mostrar_productos():
    try: 
        colorama.init()

        conexion = sqlite3.connect("productos.db")
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM productos")
        lista_productos = cursor.fetchall()
        print("Lista total de productos:")
        for producto in lista_productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Categoría: {producto[2]}, Precio: {producto[3]}")
    
    finally:
        conexion.close()

# BUSCAR PRODUCTOS
def buscar_productos():
    try: 
        colorama.init()
        conexion = sqlite3.connect("productos.db")
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM productos")
        lista_productos = cursor.fetchall()
        busqueda = input("Ingrese el nombre del producto que desea buscar: ").strip().lower()
        if busqueda == "":
            print(colorama.Fore.RED + "Ingrese un nombre" + colorama.Style.RESET_ALL)
        else:
            for producto in lista_productos:
                if busqueda == producto[1]:
                    print(f"ID: {producto[0]}, Nombre: {producto[1]}, Categoría: {producto[2]}, Precio: {producto[3]}")
                else:
                    print(colorama.Fore.RED + "Producto no encontrado" + colorama.Style.RESET_ALL)
    finally:
        conexion.close()

# MODIFICAR PRECIO
def modificar_precio():
    try:
        colorama.init()
        conexion = sqlite3.connect("productos.db")
        cursor = conexion.cursor()

        while True:
            id = input("Ingrese el número de ID del producto que desea actualizar: ")
            if id.isdigit():
                id = int(id)
            else:
                print(colorama.Fore.RED + "Ingrese un ID válido" + colorama.Style.RESET_ALL)
                continue

            nuevo_precio = input("Ingrese el nuevo precio del producto sin '$' y sin centavos: ")
            if nuevo_precio.isdigit():
                nuevo_precio = int(nuevo_precio)
                if nuevo_precio <= 0:
                    print(colorama.Fore.RED + "El precio no puede ser 0 o negativo" + colorama.Style.RESET_ALL)
                    continue
                else:
                    cursor.execute("UPDATE productos SET precio = ? WHERE id = ?", (nuevo_precio, id))
                    print(colorama.Fore.GREEN + "Carga exitosa" + colorama.Style.RESET_ALL)
                    break
            else:
                print(colorama.Fore.RED + "Ingrese un precio válido" + colorama.Style.RESET_ALL)
                continue

        conexion.commit()

    except ValueError:
        print(colorama.Fore.RED + "Ingrese un número" + colorama.Style.RESET_ALL)

    except IndexError:
        print(colorama.Fore.RED + "Ingrese un número válido de índice" + colorama.Style.RESET_ALL)

    except sqlite3.Error as e:
        print(f"Error: {e}")
        conexion.rollback()

    finally:
        conexion.close()

# ELIMINAR PRODUCTO
def eliminar_producto():
    colorama.init()

    try:
        conexion = sqlite3.connect("productos.db")
        cursor = conexion.cursor()

        cursor.execute("BEGIN TRANSACTION")

        id = int(input("Ingrese el número de ID del producto que desea eliminar: "))
        cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
        print(colorama.Fore.GREEN + "Eliminación exitosa" + colorama.Style.RESET_ALL)

        conexion.commit()

    except ValueError:
        print(colorama.Fore.RED + "Ingrese un número" + colorama.Style.RESET_ALL)

    except IndexError:
        print(colorama.Fore.RED + "Ingrese un número válido de índice" + colorama.Style.RESET_ALL)

    except sqlite3.Error as e:
        print(f"Error: {e}")
        conexion.rollback()

    finally:
        conexion.close()

# TERMINAR PROGRAMA
def terminar_programa():
    print("Gestión finalizada")

# CASE _
def imprimir_error_opcion():
    print(colorama.Fore.RED + "Ingrese una opción válida" + colorama.Style.RESET_ALL)



