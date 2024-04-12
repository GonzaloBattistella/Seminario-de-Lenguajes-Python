
#Funcion para determinar el goleador/a. Inciso 2
def info_goleador(info_jugadores):
    indice_max = info_jugadores["Goals"].index(max(info_jugadores["Goals"]))

    nombre = info_jugadores["Names"][indice_max]
    cant_goles = info_jugadores["Goals"][indice_max]

    print(f"El/La jugador/jugadora {nombre} es el/la goleador/a con {cant_goles} goles en la Temporada")



#Funcion para conocer el nombre del jugador/a mas Influyente en la temporada. Inciso 3
def mas_influyente(info_jugadores):
    suma_aux = 0
    suma_max = 0
    nombre = 0

    for i in range(len(info_jugadores["Names"])):
        nom_aux = info_jugadores["Names"][i]
        goles = info_jugadores["Goals"][i]
        goles_evitados = info_jugadores["Goals_avoided"][i]
        asistencia = info_jugadores["Assists"][i]

        suma_aux = goles * 1.5 + goles_evitados * 1.25 + asistencia

        if suma_aux > suma_max:
            suma_max = suma_aux
            nombre = nom_aux
    

    print(f"El/la jugador/a mas influyente de la temporada fue {nombre} con {suma_max} puntos")


#Funcion para conocer el promedio de goles del equipo en general.
def promedio_general (info_jugadores):
    suma_total_goles = sum(info_jugadores["Goals"])

    #Divido por 25 ya que fue la cantidad de partidos en la temporada
    promedio = suma_total_goles/25

    return promedio


#funcion para coonocer el promedio de goles por partido del goleador o goleadora.
def prom_goleador(info_jugadores):
    
    indice_max = info_jugadores["Goals"].index(max(info_jugadores["Goals"]))

    goles_max = info_jugadores["Goals"][indice_max]

    #Divido por 25 ya que fue la cantidad de partidos en la temporada
    promedio_goleador = goles_max / 25

    return promedio_goleador


