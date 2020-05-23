import pickle

fichero = open("lista_nombres", "rb") # carga el fichero en modo lectura binaria

lista = pickle.load(fichero) # el encargado de transformar la lista de binario a lenguaje

print(lista) #imprime la variable que se le asigno a la carga

