# MENU
def menu():
    print("--Sistema de Gestión Básica De Productos--")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

# AGREGAR PRODUCTO
def agregar_producto():
    import colorama
    colorama.init()

    while True:
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

        precio = input("Ingrese el precio del producto sin centavos: ").strip()
        if precio.isdigit():
            precio = int(precio)
            if precio <= 0:
                print(colorama.Fore.RED + "El precio no puede ser 0 o negativo" + colorama.Style.RESET_ALL)
                continue
        else:
            print(colorama.Fore.RED + "Ingrese un precio válido" + colorama.Style.RESET_ALL)
            continue

        nuevo_producto = [nombre, categoria, precio]
        return nuevo_producto

# MOSTRAR PRODUCTOS
def mostrar_productos(productos):
    print("Lista total de productos:")
    for index, producto in enumerate(productos, start = 1):
        print(f"{index}.\t{producto[0]}\t{producto[1]}\t{producto[2]}")

# BUSCAR PRODUCTOS
def buscar_productos(productos):
    import colorama
    colorama.init()

    busqueda = input("Ingrese el nombre del producto que desea buscar: ").strip().lower()
    if busqueda == "":
        print(colorama.Fore.RED + "Ingrese un nombre válido" + colorama.Style.RESET_ALL)
    else:
        for producto in productos:
            if busqueda == producto[0]:
                print(f"{producto[0]}\t{producto[1]}\t{producto[2]}")
            else:
                print(colorama.Fore.RED + "Producto no encontrado" + colorama.Style.RESET_ALL)

# ELIMINAR PRODUCTO
def eliminar_producto(productos):
    import colorama
    colorama.init()

    try:
        eliminar = int(input("Ingrese el número del producto que desea eliminar según su índice: "))
        eliminar = (eliminar) - 1
        productos.pop(eliminar)
        print(colorama.Fore.GREEN + "Eliminación exitosa" + colorama.Style.RESET_ALL)
    except ValueError:
        print(colorama.Fore.RED + "Ingrese un número" + colorama.Style.RESET_ALL)
    except IndexError:
        print(colorama.Fore.RED + "Ingrese un número válido de índice" + colorama.Style.RESET_ALL)


# TERMINAR PROGRAMA
def terminar_programa():
    print("Gestión finalizada")




