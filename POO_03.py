class Persona():

    def __init__(self, nombre, edad, residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia

    def descripcion(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Residencia: ", self.residencia)

class Empleado(Persona):

    def __init__(self, nombre_empleado, edad_empleado, residencia_empleado, salario, antiguedad):

        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)

        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print("Salario: ", self.salario)
        print("Antiguedad: ", self.antiguedad)


Somebody = Empleado("Juan", 20, "Puente alto", 50000, 10)
Somebody.descripcion()

print("-----------------------------------------------------------------------------")

Alguien = Persona("Manuel", 16, "casa")
Alguien.descripcion()



