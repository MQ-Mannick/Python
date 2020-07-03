import re

#-------------------------------------Metacaracteres : anclas y clases de caracteres---------------------------------

#-------------------------------------------- Metacaracter ^----------------------------------------------------------------

lista_nombres = ["Martin Picapiedra", "Sandra Enriquez", "Pablo Martin", "Ana Sandra Martin", "Enrique Goza", "Sandra Almibar"]

for elemento in lista_nombres:
    if re.findall('^Sandra', elemento): #Con el metacaracter ^ mirara en la lista pasada cual de los nombres coincide al INICIO con "Sandra" y devolvera el nombre completo
        print(elemento)

#Al ejecutar solo tirara aquellos nombre que coincidan al INICIO, es el caso de ana sandra martin, aunque tenga el str buscado no se imprime

#--------------------------------------------------------------Meta caracter $ ------------------------------------------------

for elemento in lista_nombres:
    if re.findall('Martin$', elemento): #Con el metacaracter $ mirara en la lista pasada cual de los nombres coincide al FINAL con "Martin" y devolvera el nombre completo
        print(elemento)

#Como se puede observar, martin picapiedra no se imprime ya que no cumple con la regla de estar al final del metacaracter

#------------------------------------------------------Clase de caracteres del tipo [xyz] -----------------------------------------------

lista_codigos = ["30eiiir-ie03", "3994jnjnee", "0394hubue-3", "eiieikk0001"]

for elemento in lista_codigos:
    if re.findall('[-]', elemento): #Los caracteres que le pasemos a la llave se deberan encontrar en cualquiera de los elementos, si existe, pues lo imprime, 
        print(elemento)

#Como se puede ver no importa el orden de los caracteres, siempre buscara en los elementos aquellos que coincidan, en este caso el caracter -

#------------------------------------------------Ejemplo numero 1 - Encontrar tanto niños como niñas en una lista-------------------------

lista_personas = ['niños', 'niñas', 'padres', 'hermanos', 'tios']

for elemento in lista_personas:
    if re.findall('niñ[oa]s', lista_personas) #imprimira tantos los niños como las niñas, pues como se dijo antes no importa el orden del corchete, buscara ambos
        print(elemento)
