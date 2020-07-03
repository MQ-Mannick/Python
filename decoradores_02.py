def funcion_decoradora(funcion): 
    def funcion_interna(*args): #Cuando la funcion que vamos a decorar trae argumentos se debe colocar *args, un numero indeterminado de parametros

        print("Realizaremos un cálculo: ")
        
        funcion(*args) #Tambien aqui porque esta es la funcion pasada por paramtro

        print("La ejecución ha terminado")

    return funcion_interna

@funcion_decoradora 
def suma(num_1, num_2):
    print(num_1 + num_2)

@funcion_decoradora
def resta(num_1, num_2):
    print(num_1 - num_2)

suma(7,5)
resta(12, 10)