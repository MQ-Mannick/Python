class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self): 
        return "{} que trabaja como {} tiene un salario de {}$".format(self.nombre, self.cargo, self.salario)

listaEmpleados = [
Empleado("Juan", "Ejecutivo", 2045),
Empleado("Bob", "CEO", 5500),
Empleado("Pepe", "Secretario", 1300),
Empleado("Armando", "Director", 1950),
Empleado("Ricardo", "Presidente", 3025)
]

#supongamos que los empleados ahora tienen el salario mensual, y mensualmente una comision es agregada, pero solo para salarios bajos

#definimos una funcion que realizara el calculo de la comision, va a recibir por parametro un empleado, es decir, un elemento de lista, pero con el condicional del salario
def calculo_comision(empleado): 
    if empleado.salario <= 2000:
        empleado.salario = empleado.salario * 1.03
    return empleado

#a cada elemento de la lista de empleados le aplicara la funcion pasada por parametro, luego lo que va devolviendo lo almacenara en una nueva lista
listaEmpleados_comision = map(calculo_comision, listaEmpleados) 

#Bucle for para ver las nuevas comisiones
for empleado in listaEmpleados_comision:
    print(empleado)