from io import open


#----------------MODO ESCRITURA------------------------

# archivo_texto = open("archivo.txt", "w") #abre el archivo en modo escritura

# frase = "Hey bro nice dick" #una variable se denomina como string

# archivo_texto.write(frase) #se le agrega el string al txt

# archivo_texto.close() #se cierra el archivo

#----------------MODO LECTURA------------------------

# archivo_texto = open("archivo.txt", "r") #abre el archivo en modo lectura

# texto = archivo_texto.read() #almacena en una variable lo que lee

# archivo_texto.close() #cierra el archivo

# print(texto) #imprime el texto almacenado en la variable

#----------------MODO LECTURA: READLINES------------------------

# archivo_texto = open("archivo.txt", "r")

# lineas_texto = archivo_texto.readlines() #convierte las lineas de txt en lista

# archivo_texto.close()

# print(lineas_texto)
# print(lineas_texto[0])
# print(lineas_texto[1])

#----------------MODO APPEND: Agregar texto------------------------

# archivo_texto = open("archivo.txt", "a") #abre el archivo en modo agregar

# archivo_texto.write("\nno bro, just kidding xd") #agrega directamente texto

# archivo_texto.close()

#----------------SOLUCION DE READ CON EL CURSOR------------------------

# archivo_texto = open("archivo.txt", "r")

# archivo_texto.seek(5)

# print(archivo_texto.read())

# archivo_texto.seek(0) #devuelve el cursor al principio del texto

# print(archivo_texto.read())

#----------------DIFERENCIA ENTRE READ Y SEEK------------------------

# archivo_texto = open("archivo.txt", "r")

# print(archivo_texto.read(10)) #solamente lee hasta el caracter 5
# print(archivo_texto.read()) #termina de leer donde quedo el cursos despues de caracter 5

# archivo_texto.seek(10) #posiciona el cursor en el caracter 10
# print(archivo_texto.read()) #lee a partir de caracter 10

#----------------LEER EL ARCHIVO SIEMPRE A PARTIR DE LA MITAD DE ESTE------------------------

# archivo_texto = open("archivo.txt", "r")

# archivo_texto.seek(len(archivo_texto.read())/2) #con la funcion len agarra el texto leido de read y lo divide en 2

# print(archivo_texto.read())

#----------------CURSOR AL FINAL DE LA PRIMERA LINEA------------------------

# archivo_texto = open("archivo.txt", "r")

# archivo_texto.seek(len(archivo_texto.readline()))

# print(archivo_texto.read())

#----------------NUEVAS LINEAS SIN ALTERAR EL TEXTO------------------------

archivo_texto = open("archivo.txt", "r+") #r+ agrega el siguiente modo, de escritura

# archivo_texto.write("Wow bastate impresionante") #defecto: se coloca en la posicion 0, REEMPLAZANDO

lista_texto = archivo_texto.readlines() #se guarda la lista

lista_texto[0] = "Linea extra\n" #el indice de la lista donde agregar el texto

archivo_texto.seek(0) #mueve el cursor al principio

archivo_texto.writelines(lista_texto) #se le pasa la lista 

archivo_texto.close()




