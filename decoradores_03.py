def funcion_decoradora(funcion): 
    def funcion_interna(*args, **kwargs): #ademas de args se le pasa kwargs, parametros con llave valor

        print("Realizaremos un cálculo: ")
        
        funcion(*args, **kwargs) #Tambien aqui porque esta es la funcion pasada por parametro

        print("La ejecución ha terminado")

    return funcion_interna

@funcion_decoradora 
def suma(num_1, num_2):
    print(num_1 + num_2)

@funcion_decoradora
def resta(num_1, num_2):
    print(num_1 - num_2)

@funcion_decoradora
def potencia(base, exponente):
    print(pow(base, exponente))

suma(7,5)
resta(12, 10)
potencia(base = 5, exponente = 3) #Clave valor 