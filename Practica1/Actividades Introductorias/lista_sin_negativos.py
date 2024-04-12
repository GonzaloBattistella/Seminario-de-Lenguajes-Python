"""
5. Implementa un programa que solicite al usuario que ingrese una lista de números.
Luego, imprime la lista pero detén la impresión si encuentras un número negativo.
Nota: utilice la sentencia break cuando haga falta.

"""

numeros = []

num = int(input("Ingrese un numero: "))

while num >= 0:
    if(num < 0):
        break
    else:
        numeros.append(num)
        num = int(input("Ingrese un numero: "))

# Imprimo la lista.

for i in numeros:
    print(i)