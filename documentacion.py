#-------------La triple comilla sirve para especificar documentacion asociada a cada funcion o clase--------------

import funciones_mat

class Areas():

    """Esta clase calcula las areas de distintas figura geometricas"""

    def areaCuadrado(self, lado):

        """Calcula el area de un cuadrado, con un parametro lado"""

        return "El area del cuadrado es: " + str(lado*lado)
    
    def areaTriangulo(self, base, altura):

        """Calcula el area de un triangulo, con un parametro base y altura"""

        return "El area del triangulo es: " + str((base*altura)/2)


#help(Areas) #Help es una funcion para revisar la documentacion asociada, en este caso la doc de la clase
#help(Areas.areaCuadrado)
help(funciones_mat)