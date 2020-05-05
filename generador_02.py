def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        #for letra in elemento:
            yield from elemento

ciudades_devueltas = devuelve_ciudades("Madrid", "Santiago", "Hawai")

print(next(ciudades_devueltas))