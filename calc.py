import math

def introduccion():

    print('''
    ¿Que es lo que desea hacer?

    -Para comparar dos valores ingrese a
    -Para evaluar uno solo ingrese b
    ''')

    opcion = input("Ingrese el numero: ")

    while opcion != "a" and opcion != "b":
        print("-----------------------------------")
        print("---Por favor ingrese valor valido---")
        opcion = input("Ingrese el numero: ")
    if opcion == "a":
        return "a"
    if opcion == "b":
        return "b"

def operaciones_basicas():

    print('''
    Que es lo que desea hacer?
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir 
    ''')
    indice = input("Ingrese el indice numerico: ")

    while indice != "1" and indice != "2" and indice != "3" and indice != "4": 
        print("-----------------------------------")
        print("---Por favor ingrese valor valido---")
        indice = input("Ingrese el indice numerico: ")

    if indice == "1":
        return 1
    elif indice == "2":
        return 2
    elif indice == "3":
        return 3
    elif indice == "4":
        return 4

def operaciones_complejas():

    print('''
    Que es lo que desea hacer?
    1. Raiz cuadrada
    2. Valor absoluto
    3. Porcentaje
    4. Cuadrado
    5. Cubo
    ''')
    indice = input("Ingrese el indice numerico: ")

    while indice != "1" and indice != "2" and indice != "3" and indice != "4" and indice != "5": 
        print("-----------------------------------")
        print("---Por favor ingrese valor valido---")
        numero = input("Ingrese el indice numerico: ")

    if indice == "1":
        return 1
    elif indice == "2":
        return 2
    elif indice == "3":
        return 3
    elif indice == "4":
        return 4
    elif indice == "5":
        return 5

def valor_doble(numero, num_doble_1, num_doble_2):

    if numero == 1:
        print(num_doble_1 + num_doble_2)
    if numero == 2:
        print(num_doble_1 - num_doble_2)
    if numero == 3:
        print(num_doble_1 * num_doble_2)
    if numero == 4:
        print(num_doble_1 / num_doble_2)


def valor_unico(numero, num_solo):

    if numero == 1:
        print(math.sqrt(num_solo))
    if numero == 2:
        print(abs(num_solo))
    if numero == 3:
        print("%",num_solo * 100)
    if numero == 4:
        print(num_solo * num_solo)
    if numero == 5:
        print(num_solo * num_solo * num_solo)
    
def pregunta_doble():
    print("Que desea hacer?")
    print('''
    -Para evaluar su resultado como valor unico indique x
    -Para agregar otro numero a su resultado indique y
    -Para realizar otra operacion indique z
    ''')
    indicacion = input("Indique su valor: ")

    while indicacion != "x" and indicacion !=  "y" and indicacion != "z":
        indicacion = input("Indique su valor: ")

    if indicacion == "x":
        return "x"
    if indicacion == "y":
        return "y"
    if indicacion == "z":
        return "z"

def pregunta_simple():
    print("Que desea hacer?")
    print('''
    -Para agregar un valor a su resultado indique x
    -Para evaluar nuevamente y
    -Para realizar otra operacion indique z
    ''')
    indicacion = input("Indique su valor: ")

    while indicacion != "x" and indicacion !=  "y" and indicacion != "z":
        indicacion = input("Indique su valor: ")

    if indicacion == "x":
        return "x"
    if indicacion == "y":
        return "y"
    if indicacion == "z":
        return "z"

print('''
    __   ____  _        __  __ __  _       ____  ___     ___   ____    ____ 
   /  ] /    || |      /  ]|  |  || |     /    ||   \   /   \ |    \  /    |
  /  / |  o  || |     /  / |  |  || |    |  o  ||    \ |     ||  D  )|  o  |
 /  /  |     || |___ /  /  |  |  || |___ |     ||  D  ||  O  ||    / |     |
/   \_ |  _  ||     /   \_ |  :  ||     ||  _  ||     ||     ||    \ |  _  |
\     ||  |  ||     \     ||     ||     ||  |  ||     ||     ||  .  \|  |  |
 \____||__|__||_____|\____| \__,_||_____||__|__||_____| \___/ |__|\_||__|__|      
                                           
''')

opcion = introduccion()
salida_doble = ""
salida_simple = ""

if opcion == "a":
    indice = operaciones_basicas()
    num_doble_1 = float(input("Ingrese su primer valor: "))
    num_doble_2 = float(input("Ingrese su secundo valor: "))
    valor_doble(indice, num_doble_1, num_doble_2)
    salida_doble = pregunta_doble()

if opcion == "b":
    indice = operaciones_complejas()
    num_solo = float(input("Ingrese un valor unico: "))
    valor_unico(indice, num_solo)
    salida_simple = pregunta_simple()


















# if opcion == "a":
#     print("-----------------------------------")
#     print("---Has elegido la opcion valor doble---")
#     num = operaciones_basicas()
#     num_doble_1 = float(input("Ingrese su primer numero: "))
#     num_doble_2 = float(input("Ingrese su secundo numero: "))
#     valor_doble(num, num_doble_1, num_doble_2)

# if opcion == "b":
#     print("-----------------------------------")
#     print("---Has elegido la opcion valor unico---")
#     num = operaciones_complejas()
#     num_solo = float(input("Ingrese un valor a calcular: "))
#     valor_unico(num, num_solo)







