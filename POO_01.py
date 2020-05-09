class Coche():
    #PROPIEDADES
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    en_marcha = False

    #COMPORTAMIENTO
    def arrancar(self): #SELF palabra reservada para definir metodos.
        self.en_marcha = True
    def estado(self):
        if (self.en_marcha) == True:
            return "El coche está en marcha"
        else:
            return "El coche esta en pana"

miCoche = Coche() #INSTANCIAR LA CLASE, SE CREA UN OBJ

miCoche.arrancar()
print(miCoche.estado())

