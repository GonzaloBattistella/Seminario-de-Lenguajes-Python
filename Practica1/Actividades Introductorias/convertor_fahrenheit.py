"""
2. Haz un programa que pida al usuario que ingrese una temperatura en grados Celsius y
luego convierta esa temperatura a grados Fahrenheit, mostrando el resultado.

"""
celcius = float(input("Ingrese la temperatura en grados celcius: "))

while celcius != -999:
    print(celcius, "°C  ----> ", (celcius * 9/5) + 32, " °F ")
    print(" ")
    print("Si quiere continuar ingrese otra temperatura en grados celcius. De lo contrario ingrese -999 para terminar.")
    celcius = float(input("Ingrese la temperatura en grados celcius: "))
