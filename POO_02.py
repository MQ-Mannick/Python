#HERENCIA#
class Vehiculos():

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelerar = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelerar = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("En marcha:", self.enmarcha)
        print("Acelerando:", self.acelerar)
        print("Frenando:", self.frena)

class Moto(Vehiculos):
    pass


miMoto = Moto("Lambo", "CRT")
miMoto.estado()