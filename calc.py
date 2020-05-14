import random

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
else:
    print("Has elegido el numero 2")



