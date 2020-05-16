class Coche():
    def desplazamiento(self):
        print("Me desplazo con cuatro ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo con dos ruedas")

class Camion():
    def desplazamiento(self):
        print("Me desplazo con ocho ruedas")

# miVehiculo = Coche()
# miVehiculo.desplazamiento()

# miVehiculo2 = Moto()
# miVehiculo2.desplazamiento()

# miVehiculo3 = Camion()
# miVehiculo3.desplazamiento()

def desplazamientoVehiculo(vehiculo): #FUNC POLIMORFISMO
    vehiculo.desplazamiento()


miVehiculo = Camion()
desplazamientoVehiculo(miVehiculo)