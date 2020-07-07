#-----------Realizacion de MULTIPLES test dentro de la documentacion---------------------

def areaTriangulo(base, altura):
    """
    Calcula el area de un triangulo 

    >>> areaTriangulo(3,6)
    'El área del triángulo es: 9.0'

    >>> areaTriangulo(4,5)
    'El área del triángulo es: 10.0'

    >>> areaTriangulo(7,8)
    'El área del triángulo es: 28.0'

    """

    return 'El área del triángulo es: ' + str((base*altura)/2) #Hay que tener mucho cuidado, python interpreta strings con '' por defecto, el test debe ser = al resultado de return

import doctest 
doctest.testmod() 