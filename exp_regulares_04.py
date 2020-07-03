import re

#---------------------Uso de la funcion MATCH -----------------------------

nombre_1 = "Sandra López"
nombre_2 = "Antonio Gómez"
nombre_3 = "María López"
nombre_4 = "Jara María"
nombre_5 = "Lara Gómez"

#-----------------match busca las coincidencias de caracteres dentro de un string, OJO, SOLO AL PRINCIPIO ----------------------

if re.match("Sandra", nombre_1, re.IGNORECASE): #Aqui se le pasa la cadena que se quiere busca al PRINCIPIO, el string y la condicíon de sensibilidad
    print("Se ha encontrado el nombre")
else:
    print("El nombre no se ha encontrado")

print("--------------------------------")

#----------------la variable match puede usar comodines como el . que reemplaza cualquier carácter -------------

if re.match(".ara", nombre_5, re.IGNORECASE): #reemplaze con nombre_5
    print("El nombre termina con ara")
else:
    print("El nombre no termina con ara")

print("-------------------------------------")

#-------------------------expresión regular DIGIT \d en combinacion con MATCH --------------------

cadena1 = "a3030300303"
cadena2 = "38210340390"

if re.match("\d", cadena1): #reemplazar con cadena2 para ver su uso
    print("El primer digito es numerico")
else:
    print("El primer digito no es numerico")

print("-------------------------------------")

#-------------expresion search al contrario que MATCH permite buscar en todo el string --------------------

if re.search("López", nombre_1, re.IGNORECASE): #reemplazar con cadena2 para ver su uso
    print("López existe")
else:
    print("López no existe")
