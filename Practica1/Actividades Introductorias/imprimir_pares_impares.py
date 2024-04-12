"""
6. Modifique el ejercicio 4 para que dada la lista de número genere dos nuevas listas, una
con los número pares y otras con los que son impares. Imprima las listas al terminar de
procesarlas.

"""

numeros = [1,2,3,4,5,6,12,14,15,16,22,24,25,27,30,33,32,36,35,40,41]

num_impares = []
num_pares = []

for i in numeros:
    if i % 2 == 0:
        num_pares.append(i)
    else:
        num_impares.append(i)

#Imprimo la lista de numeros pares

print("Lista de numeros Pares: ")
print("")

for x in num_pares:
    print("_", x)

print("_" * 30)
#Imprimo la lista de numeros impares

print("")
print("Lista de numeros Impares: ")
print("")

for j in num_impares:
    print("_", j)

print("_" * 30)