import colorama
import sqlite3

# CONEXIÓN A BASE DE DATOS
conexion = sqlite3.connect("productos.db")
cursor = conexion.cursor()

# CREAR TABLA EN BASE DE DATOS
def crear_base_de_datos():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripción TEXT NOT NULL,
            categoría TEXT NOT NULL,
            precio REAL NOT NULL,
            cantidad INTEGER NOT NULL
        )
    """)

# MENU
def menu():
    print("--Sistema de Gestión Básica De Productos--")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Modificar información de producto")
    print("5. Buscar productos por unidades en stock")
    print("6. Eliminar producto")
    print("7. Salir")

# AGREGAR PRODUCTO
def agregar_producto():
    try:
        colorama.init()
        conexion = sqlite3.connect("productos.db")
        cursor = conexion.cursor()

        while True:
            # Agregar nombre
            while True:
                nombre = input("Ingrese el nombre del producto: ").strip().lower()
                if nombre == "":
                    print(colorama.Fore.RED + "Ingrese un nombre" + colorama.Style.RESET_ALL)
                else:
                    print(colorama.Fore.GREEN + "Nombre cargado" + colorama.Style.RESET_ALL)
                    break

            # Agregar descripción
            while True:
                descripcion = input("Ingrese una breve descripción del producto: ").strip().lower()
                if descripcion == "":
                    print(colorama.Fore.RED + "Ingrese una descripción" + colorama.Style.RESET_ALL)
                else:
                    print(colorama.Fore.GREEN + "Descripción cargada" + colorama.Style.RESET_ALL)
                    break

            # Agregar categoría
            while True:
                categoria = input("Ingrese la categoría del producto: ").strip().lower()
                if categoria == "":
                    print(colorama.Fore.RED + "Ingrese una categoría" + colorama.Style.RESET_ALL)
                else:
                    print(colorama.Fore.GREEN + "Categoría cargada" + colorama.Style.RESET_ALL)
                    break

            # Agregar precio
            while True:
                precio = float(input("Ingrese el precio del producto sin '$': "))
                if precio <= 0:
                    print(colorama.Fore.RED + "El precio no puede ser 0 o negativo" + colorama.Style.RESET_ALL)
                else:
                    print(colorama.Fore.GREEN + "Precio cargado" + colorama.Style.RESET_ALL)
                    break
            
            # Agregar cantidad
            while True:
                cantidad = int(input("Ingrese cantidad del producto: "))
                if cantidad < 0:
                    print(colorama.Fore.RED + "La cantidad no puede ser menor que 0" + colorama.Style.RESET_ALL)
                else:
                    print(colorama.Fore.GREEN + "Cantidad cargada" + colorama.Style.RESET_ALL)
                    break

            cursor.execute("BEGIN TRANSACTION")
            cursor.execute("INSERT INTO productos (nombre, descripción, categoría, precio, cantidad) VALUES(?, ?, ?, ?, ?)", (nombre, descripcion, categoria, precio, cantidad))

            conexion.commit()
            print(colorama.Fore.GREEN + "Carga final de producto exitosa" + colorama.Style.RESET_ALL)

            pregunta = input("¿Desea agregar otro producto? S/N").strip().lower()
            if pregunta == "s":
                continue
            elif pregunta == "n":
                break
            else:
                print("Ingrese una opción válida")

    except ValueError:
        print(colorama.Fore.RED + "Ingrese un valor válido" + colorama.Style.RESET_ALL)

    except sqlite3.Error as error:
        print(f"Ha ocurrido un error: {error}")
        conexion.rollback()

    except Exception as error:
        conexion.rollback()
        print(f"Ha ocurrido un error: {error}")

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
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Categoría: {producto[3]}, Precio: {producto[4]}, Cantidad: {producto[5]}")

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
                    print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Categoría: {producto[3]}, Precio: {producto[4]}, Cantidad: {producto[5]}")

    finally:
        conexion.close()

# MODIFICAR DATOS SUBMENÚ
def consultar_modificacion_datos():
    try:
        colorama.init()
        conexion = sqlite3.connect("productos.db")
        cursor = conexion.cursor()

        while True:
            mostrar_productos()
            id = int(input("Ingrese el número de ID del producto que desea actualizar: "))
            cursor.execute("SELECT EXISTS(SELECT 1 FROM productos WHERE id = ?)", (id,))
            consulta_id = cursor.fetchone()
            
            if consulta_id[0] == 1:
                while True:
                    print("1. Nombre")
                    print("2. Descripción")
                    print("3. Categoría")
                    print("4. Precio")
                    print("5. Cantidad")
                    print("6. Volver atrás")
                    dato_a_modificar = int(input("Ingrese el número de opción del dato que desea modificar: "))
                    match dato_a_modificar:
                        case 1:
                            def modificar_nombre():
                                nuevo_nombre = input("Ingrese el nuevo nombre del producto que desea actualizar: ").strip().lower()
                                if nuevo_nombre == "":
                                    print(colorama.Fore.RED + "Ingrese un nombre" + colorama.Style.RESET_ALL)
                                else:
                                    cursor.execute("BEGIN TRANSACTION")
                                    cursor.execute("UPDATE productos SET nombre = ? WHERE id = ?", (nuevo_nombre, id))
                                    print(colorama.Fore.GREEN + "Nombre modificado" + colorama.Style.RESET_ALL)

                                conexion.commit()
                            modificar_nombre()

                        case 2:
                            def modificar_descripcion():
                                nueva_descripcion = input("Ingrese la nueva descripción del producto que desea actualizar: ").strip().lower()
                                if nueva_descripcion == "":
                                    print(colorama.Fore.RED + "Ingrese una descripción" + colorama.Style.RESET_ALL)
                                else:
                                    cursor.execute("BEGIN TRANSACTION")
                                    cursor.execute("UPDATE productos SET descripción = ? WHERE id = ?", (nueva_descripcion, id))
                                    print(colorama.Fore.GREEN + "Descripción modificada" + colorama.Style.RESET_ALL)

                                conexion.commit()
                            modificar_descripcion()


                        case 3:
                            def modificar_categoria():
                                nueva_categoria = input("Ingrese la nueva categoría del producto que desea actualizar: ").strip().lower()
                                if nueva_categoria == "":
                                    print(colorama.Fore.RED + "Ingrese una categoría" + colorama.Style.RESET_ALL)
                                else:
                                    cursor.execute("BEGIN TRANSACTION")
                                    cursor.execute("UPDATE productos SET categoría = ? WHERE id = ?", (nueva_categoria, id))
                                    print(colorama.Fore.GREEN + "Categoría modificado" + colorama.Style.RESET_ALL)

                                conexion.commit()
                            modificar_categoria()

                        case 4:
                            def modificar_precio():
                                nuevo_precio = input("Ingrese el nuevo precio del producto sin '$': ")
                                nuevo_precio = float(nuevo_precio)
                                if nuevo_precio <= 0:
                                    print(colorama.Fore.RED + "El precio no puede ser 0 o negativo" + colorama.Style.RESET_ALL)
                                else:
                                    cursor.execute("BEGIN TRANSACTION")
                                    cursor.execute("UPDATE productos SET precio = ? WHERE id = ?", (nuevo_precio, id))
                                    print(colorama.Fore.GREEN + "Precio modificado" + colorama.Style.RESET_ALL)

                                conexion.commit()
                            modificar_precio()

                        case 5:
                            def modificar_cantidad():
                                nueva_cantidad = (input("Ingrese la nueva cantidad del producto que desea actualizar: "))
                                if nueva_cantidad.isdigit():
                                    nueva_cantidad = int(nueva_cantidad)
                                    if nueva_cantidad <= 0:
                                        print(colorama.Fore.RED + "La cantidad no puede ser 0 o menor que 0" + colorama.Style.RESET_ALL)
                                    else:
                                        cursor.execute("BEGIN TRANSACTION")
                                        cursor.execute("UPDATE productos SET cantidad = ? WHERE id = ?", (nueva_cantidad, id))
                                        print(colorama.Fore.GREEN + "Cantidad modificada" + colorama.Style.RESET_ALL)
                                else:
                                    print(colorama.Fore.RED + "Ingrese un valor válido" + colorama.Style.RESET_ALL)

                                conexion.commit()
                            modificar_cantidad()

                        case 6:
                            terminar_programa()
                            break

                        case _:
                            imprimir_error_opcion()
            else:
                print("ID de producto no encontrada")

            pregunta = input("¿Desea modificar producto? S/N").strip().lower()
            if pregunta == "s":
                continue
            elif pregunta == "n":
                break
            else:
                print("Ingrese una opción válida")

    except ValueError:
        print(colorama.Fore.RED + "Ingrese un valor válido" + colorama.Style.RESET_ALL)

    except sqlite3.Error as error:
        print(f"Ha ocurrido un error: {error}")
        conexion.rollback()

    except Exception as error:
        conexion.rollback()
        print(f"Ha ocurrido un error: {error}")

    finally:
        conexion.close()



"""
# MODIFICAR PRECIO
def modificar_precio():
    mostrar_productos()

    try:
        colorama.init()
        conexion = sqlite3.connect("productos.db")
        cursor = conexion.cursor()

        while True:
            id = int(input("Ingrese el número de ID del producto que desea actualizar: "))
            cursor.execute("SELECT EXISTS(SELECT 1 FROM productos WHERE id = ?)", (id,))
            consulta_id = cursor.fetchone()

            if consulta_id[0] == 1:
                nuevo_precio = input("Ingrese el nuevo precio del producto sin '$': ")
                nuevo_precio = float(nuevo_precio)
                if nuevo_precio <= 0:
                    print(colorama.Fore.RED + "El precio no puede ser 0 o negativo" + colorama.Style.RESET_ALL)
                else:
                    cursor.execute("BEGIN TRANSACTION")
                    cursor.execute("UPDATE productos SET precio = ? WHERE id = ?", (nuevo_precio, id))
                    print(colorama.Fore.GREEN + "Carga exitosa" + colorama.Style.RESET_ALL)
            else:
                print("ID de producto no encontrada")

            conexion.commit()

            pregunta = input("¿Desea modificar el precio de otro producto? S/N").strip().lower()
            if pregunta == "s":
                continue
            elif pregunta == "n":
                break
            else:
                print("Ingrese una opción válida")

    except ValueError:
        print(colorama.Fore.RED + "Ingrese un valor válido" + colorama.Style.RESET_ALL)

    except IndexError:
        print(colorama.Fore.RED + "Ingrese un número válido de índice" + colorama.Style.RESET_ALL)

    except sqlite3.Error as error:
        print(f"Ha ocurrido un error: {error}")
        conexion.rollback()

    except Exception as error:
        conexion.rollback()
        print(f"Ha ocurrido un error: {error}")

    finally:
        conexion.close()
"""

# BUSCAR PRODUCTO STOCK
def filtrar_productos_por_cantidad():
    try:
        colorama.init()
        conexion = sqlite3.connect("productos.db")
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM productos")
        lista_productos = cursor.fetchall()

        cantidad_producto = int(input("Ingrese el número de stock que desea consultar. La búsqueda devolverá todos los productos en stock con esa cantidad de unidades o menos: "))
        print("Productos:")
        for producto in lista_productos:
            if producto[5] <= cantidad_producto:
                print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Categoría: {producto[3]}, Precio: {producto[4]}, Cantidad: {producto[5]}")

    except ValueError:
        print(colorama.Fore.RED + "Ingrese un valor válido" + colorama.Style.RESET_ALL)

    except sqlite3.Error as error:
        print(f"Ha ocurrido un error: {error}")
        conexion.rollback()

    except Exception as error:
        conexion.rollback()
        print(f"Ha ocurrido un error: {error}")

    finally:
        conexion.close()

# ELIMINAR PRODUCTO
def eliminar_producto():
    try:
        colorama.init()
        conexion = sqlite3.connect("productos.db")
        cursor = conexion.cursor()

        while True:
            id = int(input("Ingrese el número de ID del producto que desea eliminar: "))
            cursor.execute("SELECT EXISTS(SELECT 1 FROM productos WHERE id = ?)", (id,))
            consulta_id = cursor.fetchone()

            if consulta_id[0] == 1:
                cursor.execute("BEGIN TRANSACTION")
                cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
                conexion.commit()
                print(colorama.Fore.GREEN + "Eliminación exitosa" + colorama.Style.RESET_ALL)

                mostrar_productos()

                pregunta = input("¿Desea eliminar otro producto? S/N").strip().lower()
                if pregunta == "s":
                    continue
                elif pregunta == "n":
                    break
                else:
                    print("Ingrese una opción válida")
            else:
                print("ID de producto no encontrada")

    except ValueError:
        print(colorama.Fore.RED + "Ingrese un número de ID" + colorama.Style.RESET_ALL)

    except IndexError:
        print(colorama.Fore.RED + "Ingrese un número válido de índice" + colorama.Style.RESET_ALL)

    except sqlite3.Error as error:
        print(f"Ha ocurrido un error: {error}")
        conexion.rollback()

    except Exception as error:
        conexion.rollback()
        print(f"Ha ocurrido un error: {error}")

    finally:
        conexion.close()

# TERMINAR PROGRAMA
def terminar_programa():
    print("Gestión finalizada")

# CASE _
def imprimir_error_opcion():
    print(colorama.Fore.RED + "Ingrese una opción válida" + colorama.Style.RESET_ALL)



