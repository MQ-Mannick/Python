import math

def raizCuadrada(listaNumeros):
    """
    La funcion devuelve una lista con la raiz
    cuadrada de cada elemento de la lista que 
    se le entrega como parametro.

    >>> lista = []
    >>> for i in [4, 9, 16]:
    ...     lista.append(i)
    >>> raizCuadrada(lista)
    [2.0, 3.0, 4.0]

    >>> lista = [4, -9, 16]
    >>> raizCuadrada(lista)
    Traceback (most recent call last):
        ...
    ValueError: math domain error

    """

    #Lo anterior pudo haber sido mas claro pero era solo para mostrar las expresiones anidadas en bucles y condicionales con ... (tres puntos)
    #Los tres puntos tambien se usan para el manejo de errores en pruebas, donde solo importan las lineas que siempre se repiten, en este caso
    #Traceback y Valueerror(error de dominio de la raiz cuadrada), donde se colocan ... para especificar el contenido, que puede ser cualquier cosa.

    return [math.sqrt(n) for n in listaNumeros]

#print(raizCuadrada([9, -16, 25, 36, 100]))

import doctest
doctest.testmod()