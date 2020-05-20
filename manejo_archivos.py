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

archivo_texto = open("archivo.txt", "a") #abre el archivo en modo agregar

archivo_texto.write("\nno bro, just kidding xd") #agrega directamente texto

archivo_texto.close()