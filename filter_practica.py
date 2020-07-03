#Aplicacion de la funcion filter, donde la utilidad seria que al instanciar la clase de empleado una cuantas veces, 
#filtre entonces aquellos empleados con un salario mayor a 20000$, para despues llamar al metodo del objeto Empleado

class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self): #define que al instanciar la clase cuando se imprime devuelve un string en  vez del objeto en cuestion
        return "{} que trabaja como {} tiene un salario de {}$".format(self.nombre, self.cargo, self.salario)

listaEmpleados = [
Empleado("Juan", "Ejecutivo", 20000),
Empleado("Bob", "CEO", 50000),
Empleado("Pepe", "Secretario", 10000),
Empleado("Armando", "Director", 15000),
Empleado("Ricardo", "Presidente", 30000)
]

empleados_con_salarios_altos = filter(lambda empleado: empleado.salario > 20000, listaEmpleados) #funcion anonima que indica que si el salario es mayor que 20000 de la lista, lo filtra

for empleado in empleados_con_salarios_altos:
    print(empleado)
