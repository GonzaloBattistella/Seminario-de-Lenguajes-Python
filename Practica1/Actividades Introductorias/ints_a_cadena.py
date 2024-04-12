"""
7. Escribe un programa que tome una lista de números enteros como entrada del usuario.
Luego, convierte cada número en la lista a string y únelos en una sola cadena,
separados por guiones ('-'). Sin embargo, excluye cualquier número que sea múltiplo
de 3 de la cadena final.

"""

numeros = []
num = 0

num = int(input("Ingrese un numero entero. Ingrese -0 para Terminar la carga: "))
while num != -0:
    numeros.append(num)
    num = int(input("Ingrese un numero entero. Ingrese -0 para Terminar la carga: "))


# Convierto cada numero de la lista en string, excepto los numeros multiplos de 3.
cadena = ""
for i in numeros:
    if not i % 3 == 0:
       cadena += (str(i) + "-") 

print(cadena)