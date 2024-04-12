dic_products = {}

#Funcion para agregar un producto al inventario.
def add_product(dic_products):
    product = input("INGRESE EL NOMBRE DEL PRODUCTO: ")
    amount = input("INGRESE LA CANTIDAD DEL PRODUCTO: ")

    #Verifico si el producto ingresado ya se encuentra en el diccionario.
    if product in dic_products:
        dic_products[product] += int(amount)
    else:
        dic_products[product] = int(amount)

    print("EL PRODUCTO SE AGREGO EXITOSAMENTE! ")  
    print("")


#Funcion para eliminar un producto del inventario.
def delete_product(dic_products):
    nombre = input(f"INGRESE EL NOMBRE DEL PRODUCTO A ELIMINAR: ")
    
    if nombre.lower() in dic_products:
        del dic_products[nombre]
        print(f"EL PRODUCTO {nombre} SE HA ELIMINADO CORRECTAMENTE. ")
    
    else:
        print(f"NO SE ENCONTRO EL PRODUCTO {nombre} EN EL INVENTARIO. ")
    
    print("")


#Funcion para mostrar el inventario
def show_inventory(dic_products):
    print("*" * 30)
    print(" INVENTARIO ")
    for nombre, amount in dic_products.items():
        print("-" * 30)
        print(f"{nombre}: {amount}")

    print("-" * 30)
    print("*" * 30)


    
