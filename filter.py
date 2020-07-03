#---------------------Funcion filter----------------------------------

#Definimos una funcion con restricciones devuelve solo los numeros pares
def numero_par(num):
    if num % 2 == 0:
        return True

#Definimos una variable con numeros en su interior
numeros = [13, 45, 77, 113, 12]

#Se utiliza la funcion filter, que itera el arreglo dentro de la funcion definida anteriormente y crea un nuevo arreglo con los valores que cumplieron la condicion

print(list(filter(numero_par, numeros))) #filter devuelve un OBJETO, pero se puede visualizar en formato de lista con la palabra LIST

#------------------------Integracion con funciones lambda--------------------------------------

print(list(filter(lambda numero_par: numero_par%2==0, numeros))) #Esto hace lo mismo pero con una funcion anonima