#GENERADOR DE PARES CON UN LIMITE FUNCION
# def generaPares(limite):
#     num = 1
#     List = []

#     while num <= limite:
#         List.append(num*2)
#         num += 1
#     return List

# print(generaPares(10))

#GENERADOR DE PARES CON GENERADOR 

def generaPares(limite):
    num = 1

    while num <= limite:

        yield num*2 #construye un objeto iterable
      
        num += 1

devuelvePares = generaPares(4) #guarda el objeto iterable python 

print(next(devuelvePares)) #devuelve el primer valor
print(next(devuelvePares)) #devuelve el secundo valor
print(next(devuelvePares)) #devuelve el tercer valor
print(next(devuelvePares)) #devuelve el cuarto valor
