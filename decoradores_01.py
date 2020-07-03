def funcion_decoradora(funcion): #Esta es la funcion A, es la funcion que se llama para "decorar" una funcion B cualquiera
    def funcion_interna(): # Esta es la funcion C, es la que se encarga de decorar a B, retornandola despues con la func A

        #Acciones adicionales que decoran
        print("Realizaremos un cálculo: ")

        #La funcion pasada por parametro, esto es para especificar donde ira el resultado de la funcion B 
        funcion()

        #+Acciones adicionales que decoran
        print("La ejecución ha terminado")

    return funcion_interna #Se devuelve la funcion C como la funcion B decorada

@funcion_decoradora #Sintaxis para decorar la funcion
def suma():
    print(15 + 20)

@funcion_decoradora
def resta():
    print(15 - 20)

suma()
resta()