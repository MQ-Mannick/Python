import re

#-------------------Trabajando con rangos de caracteres -----------------------------------

lista_nombres = ["Ana", "Pedro", "Rosa", "Sandra", "Celia"]

for elemento in lista_nombres:
    if re.findall('[o-t]', elemento): #solo escogera aquellos nombres que contengan alguna de las letras de este rango de caracteres
        print(elemento)
    #Como se puede observar, ni celia ni ana se imprimen porque estan fuera del rango

print("--------------------------------")

for elemento in lista_nombres:
    if re.findall('^[O-T]', elemento): #esta expresion es sensible a mayusculas, por lo que si queremos los nombres que empiezen con un rango necesitamos especificar
        print(elemento)
    #Como se puede observar, se imprimen los nombres cuyo PRIMER caracter en MAYUSCULA se encuentra dentro del rango

print("--------------------------------")

for elemento in lista_nombres:
    if re.findall('[o-t]$', elemento): #Ahora le pedimos que imprima todos los nombres que terminen  con un caracter dentro de un rango
        print(elemento)
    #Como se puede observar, se imprimen los nombres cuyo ULTIMO CARACTER se encuentra dentro del RANGO, solo pedro cumple con esta regla

print("--------------------------------")

#------------------Ejemplo numero 1: codigos de empresa --------------------

lista_codigos = ["CH_1", "CH_2", "CH_3", "CH_4", "CH_5", "CH_6", "CH_A", "CH_B", "CH_C"]

for elemento in lista_codigos:
    if re.findall('CH_[1-3]', elemento): #En este caso imprimira solo los codigos que comprendan numero entre el  y el 3
        print(elemento)

print("--------------------------------")

for elemento in lista_codigos:
    if re.findall('CH_[^1-3]', elemento): #En este caso imprimira solo los codigos que estan fuera del rango especificado, negando con ^
        print(elemento)

print("--------------------------------")

for elemento in lista_codigos:
    if re.findall('CH_[1-3A-B]', elemento): #Para poder comprobar dos rangos al mismo tiempo se pasan los dos parametros seguidos
        print(elemento)
