#importamos la libreria que contiene las expresiones regulares
import re 

#Una cadena de texto es declarada como variable
cadena = "Aprendiendo expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla muy bien equipado"

#el metodo .search admite lo que se busca y la cadena de texto donde se va a buscar, devuelve un objeto o None
#print(re.search("regulares", cadena))

#--------------Ejemplo 1 - Condicional para saber si el texto existe-------------------------------------------
# textoBuscar = "regulares"
# if re.search(textoBuscar, cadena) is not None:
#     print("La palabra existe")
#--------------------------------------------------------------------------------------------------------------


#---------------Ejemplo 2 - Almacenar el resultado dentro de una variable para usar metodos-------------------
# textoBuscar = "expresiones"
# textoEncontrado = re.search(textoBuscar, cadena)
# print(textoEncontrado.start()) #.start indica en que numero de caracter INICIAL se encontro el texto
# print(textoEncontrado.end()) #.start indica en que numero de caracter FINAL se encontro el texto
# print(textoEncontrado.span()) #.start indica en que numero de caracter INICAL y FINAL se encontro el texto
#--------------------------------------------------------------------------------------------------------------


#---------------Ejemplo 3 - Encontrar todas las coincidencias del texto-------------------
textoBuscar = "Python"
#el metodo .findall encuentra todas la coincidencias dentro de la cadena de texto, como parametro(texto a buscar, cadena), devuelve una lista
listaResultados = re.findall(textoBuscar, cadena)
print(len(listaResultados)) #como es una lista se pueden saber el numero de coincidencia con len()

