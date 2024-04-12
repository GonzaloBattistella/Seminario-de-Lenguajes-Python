"""
1. Desarrolla un programa que solicite al usuario que ingrese su edad y luego calcule y
muestre cuántos años le faltan para alcanzar los 100 años.

"""
edad = int(input("Ingrese su edad."))
max_edad = 100

while edad != -1:
    print("Le faltan ", max_edad - edad, " para llegar a los 100 años! ")
    print("")
    print("Si quiere continuar, Ingrese su edad. de lo contrario ingrese -1 para terminar.")
    edad = int(input("Ingrese su edad."))