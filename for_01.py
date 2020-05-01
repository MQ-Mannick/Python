
numeros = input("Ingrese numeros separados por comas porfavor: ")

lista_num = numeros.split(",")

valor_max = len(lista_num)

rango = range(1, valor_max + 1)

lista = list()

def indices():
    for i in rango:
        lista.append(i)
    return lista

lista_indices = indices()

print("Sus numeros son " + str(lista_num) + " y el numero de digitos que ingreso son " + str(valor_max))











    






    




