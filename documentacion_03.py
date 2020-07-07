#---------Documentacion para una funcion que comprueba el mail de un usuario respecto a la posicion de la arroba----------
def compruebaMail(mailUsuario):
    """
    la función comprueba mail evalúa un mail recibido en busca de la @,
    si tiene una arroba es correcto, si tiene más de una @ es incorrecto y
    si la arroba está al final es incorrecto 

    >>> compruebaMail("mann@gmail.com")
    True

    >>> compruebaMail("mann.gmail.com@")
    False

    >>> compruebaMail("mann.gmail.com")
    False

    >>> compruebaMail("mann@gmail@com")
    False

    """
    arroba = mailUsuario.count('@')

    if(arroba != 1 or mailUsuario.rfind('@') == (len(mailUsuario) - 1)): #se le coloca el -1 porque rfind no 
                                                                         #cuenta el ultimo caracter donde se encontro, 
                                                                         #por lo que len es un digito mayor y se le debe
                                                                         #restar uno para coincidir
        return False
    else:
        return True

import doctest
doctest.testmod()

