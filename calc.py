import random

def operaciones_basicas():

    print('''
    Que es lo que desea hacer?

    1.Sumar
    2.Restar
    3.Multiplicar
    4.Dividir

    ''')
    numero = input("Ingrese su numero -")

    while numero != "1" and numero != "2" and numero != "3" and numero != "4": 
        numero = input("Ingrese su numero: ")

    if numero == "1":
        return 1
    elif numero == "2":
        return 2
    elif numero == "3":
        return 3
    elif numero == "4":
        return 4




def valor_doble(numero):
    print("Escriba dos numeros:")

    num_1 = float(input("Ingrese su primer numero: "))
    num_2 = float(input("Ingrese su segundo numero: "))

    return num_1, num_2






def valor_unico():

    print("Escriba su numero:")

    num_1 = float(input("Ingrese su numero: "))

    print(num_1)










print('''
    __   ____  _        __  __ __  _       ____  ___     ___   ____    ____ 
   /  ] /    || |      /  ]|  |  || |     /    ||   \   /   \ |    \  /    |
  /  / |  o  || |     /  / |  |  || |    |  o  ||    \ |     ||  D  )|  o  |
 /  /  |     || |___ /  /  |  |  || |___ |     ||  D  ||  O  ||    / |     |
/   \_ |  _  ||     /   \_ |  :  ||     ||  _  ||     ||     ||    \ |  _  |
\     ||  |  ||     \     ||     ||     ||  |  ||     ||     ||  .  \|  |  |
 \____||__|__||_____|\____| \__,_||_____||__|__||_____| \___/ |__|\_||__|__|      
                                           
''')

print('''
¿Que es lo que desea hacer?

-Para comparar dos valores ingrese 1
-Para evluar uno solo ingrese 2

''')

opcion = ""

while opcion != "1" and opcion != "2":
    opcion = input("Ingrese el numero: ")

if opcion == "1":
    print("Has elegido el numero 1")
    num = operaciones_basicas()
    valor_doble(num)
else:
    print("Has elegido el numero 2")
    valor_unico()







