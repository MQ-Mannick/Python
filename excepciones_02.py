import math

# def calculaRaiz(num):
#     if num < 0:
#         raise ValueError("el numero no puede ser negativo")
#     else:
#         return math.sqrt(num)

# valor = int(input("introduce: "))


#     try:
#         print(calculaRaiz(valor))
#     except ValueError as NegativeNumberError:
#         print(NegativeNumberError)


while True:
    num = int(input("introduce tu numero: "))
    if num < 0:
        print("El valor no puede ser negativo")
    else: 
        print(math.sqrt(num))
        break
        
    
        


        
            


