#---------------Realizacion de tests dentro de la documentacion de la funcion

def areaTriangulo(base, altura):
    """
    Calcula el area de un triangulo 

    >>> areaTriangulo(3,6)
    8.0

    """
    #Los test se realizan con >>> NOMBREFUNCION(valores_test) y el RESULTADO esperado justo abajo

    return (base*altura)/2 #Se debe especificar exactamente este resultado en el test para que no de error

#print(areaTriangulo(2,4))

import doctest #modulo encargado de realizar las pruebas
doctest.testmod() #Al ejecutar el test se pueden obtener dos resultados
                    #NADA: significa que el test corre bien y el resultado esperado es el resultado dado por la funcion
                    #ERROR: significa que el resultado esperado no es igual al resultado dado por la funcion