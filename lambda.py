#---------------Funciones anónimas o funciones lambda--------------------
#Sirven para funciones simples, no para complejas
#---------------Ejemplo con área de triángulo----------------------------

# def area_triangulo(base, altura):
#     return (base*altura)/2

# area_triangulo = lambda base,altura:(base*altura)/2

#-------------------------Ejemplo de lambda al cubo----------------------

al_cubo = lambda numero:numero**3
print(al_cubo(3))

#-------------------------

destacar_valor = lambda comision:"¡{}! $".format(comision)
comision_01 = 33040
print(destacar_valor(comision_01))
