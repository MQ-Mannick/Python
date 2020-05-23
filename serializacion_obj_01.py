import pickle

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


coche_1 = Vehiculos("Lambo", "reventon")
coche_2 = Vehiculos("BMW", "Carrere")
coche_3 = Vehiculos("Zonda", "cinque")

############################################

coches = [coche_1, coche_2, coche_3]

fichero = open("Fichero_coches", "wb")

pickle.dump(coches, fichero)

fichero.close()

del(fichero) 

############################################

fichero_abrir = open("Fichero_coches", "rb")

nuevos_coches = pickle.load(fichero_abrir)

fichero_abrir.close()

for i in nuevos_coches:
    print(i.estado())

