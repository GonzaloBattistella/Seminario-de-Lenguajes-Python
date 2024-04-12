import functions_inventory

inventario = {}

def main(inventario):
    name = input("INGRESE SU NOMBRE: ")

    print(f"BIENVENIDO {name} AL SISTEMA DE GESTION DE INVENTARIO")
    print("")

    print(f" MENU DE OPERACIONES")
    print("")

    print("1. AGREGAR UN PRODUCTO AL INVENTARIO")
    print("")
    print("2. ELIMINAR UN PRODUCTO DEL INVENTARIO")
    print("")
    print("3. MOSTRAR EL INVENTARIO")
    print("")
    print("4. SALIR DEL PROGRAMA ")
    print("")

    while True:
        option = int(input("INGRESE LA OPCION ELEGIDA: "))

        match option:
            case 1:
                print("")
                print(f"OPCION ELEGIDA {option}")
                functions_inventory.add_product(inventario)

            case 2:
                print("")
                print(f"OPCION ELEGIDA {option}")
                functions_inventory.delete_product(inventario)
            case 3:
                print("")
                print(f"OPCION ELEGIDA {option}")
                functions_inventory.show_inventory(inventario)
            
            case 4:
                print("")
                print(f"OPCION ELEGIDA {option}")
                print("SALIENDO DEL PROGRAMA. ")
                break

            case _:
                print("")
                print("OPCION INVALIDA, POR FAVOR INGRESE UNA OPCION VALIDA. ")
                print("")
            

        print("_" * 50)
        print("")

        print(f" MENU DE OPERACIONES")
        print("")

        print("1. AGREGAR UN PRODUCTO AL INVENTARIO")
        print("")
        print("2. ELIMINAR UN PRODUCTO DEL INVENTARIO")
        print("")
        print("3. MOSTRAR EL INVENTARIO")
        print("")
        print("4. SALIR DEL PROGRAMA ")
        print("")


main(inventario)