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

##################################################################

class VElectricos(Vehiculos):

    def __init__(self, marca, modelo):

        super().__init__(marca, modelo)
        self.autonomia = 100
    
    def cargarEnergia(self):
        self.cargando = True

    def estado(self):
        super().estado()
        print("autonomia: ", self.autonomia)


##################################################################
print("------------------------------------------------------")
##################################################################


class furgoneta(Vehiculos):
    
    def carga(self, carga):
        self.cargado = carga
        
        if(self.cargado == True):
            return "La furgoneta esta cargada"
        else:
            return "no esta cargada"

Mifurgoneta = furgoneta("KFC","001")

Mifurgoneta.arrancar()
Mifurgoneta.estado()
print(Mifurgoneta.carga(True))


##################################################################
print("------------------------------------------------------")
##################################################################


class Moto(Vehiculos):

    hcaballito = ""
    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"

    def estado(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("En marcha:", self.enmarcha)
        print("Acelerando:", self.acelerar)
        print("Frenando:", self.frena) 
        print(self.hcaballito)       

miMoto = Moto("Lambo", "CRT")
miMoto.caballito()
miMoto.estado()

##################################################################
print("------------------------------------------------------")
##################################################################

class bicicletaElectrica(VElectricos,Vehiculos): #HERENCIA MULTIPLE
    pass

Mibici = bicicletaElectrica("Tesla", "AA0")
Mibici.estado()


