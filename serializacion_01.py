import pickle

lista_nombres = ["Pedro", "Manuel", "Juan", "Pepe"] #se crea una variable array

fichero_binario = open("lista_nombres", "wb") #variable que permite la creacion del fichero en modo escritura binaria

pickle.dump(lista_nombres, fichero_binario) #el encargado de transformar el array a binario gracias a la variable open.

fichero_binario.close() #cierra el fichero

