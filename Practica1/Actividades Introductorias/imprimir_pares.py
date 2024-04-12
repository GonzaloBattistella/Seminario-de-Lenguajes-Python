"""
4. Cree un programa que dada una lista de números imprima sólo los que son pares.
Nota: utilice la sentencia continue donde haga falta.

"""

nums = [1,3,4,7,12,24,14,13,33,45,48,50,51]

print("Imprimo solo los numeros pares. ")

for i in nums:
    if not (i % 2 == 0):
        continue 
    else:
        print("numero", i)

"""
La sentencia continue, se salta todo el código restante en la iteración actual y 
vuelve al principio en el caso de que aún queden iteraciones por completar. 
"""