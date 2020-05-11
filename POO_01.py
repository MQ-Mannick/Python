class Coche():
    #PROPIEDADES
    #ESTADO INICIAL-------------------------------------
    def __init__(self):
        self.__largoChasis = 250   
        self.__anchoChasis = 120   
        self.__ruedas = 4           
        self.__en_marcha = False
    #---------------------------------------------------

    #COMPORTAMIENTO
    def arrancar(self, arrancamos): #SELF palabra reservada para definir metodos.
        self.__en_marcha = arrancamos

        if(self.__en_marcha) == True:
            chequeo = self.__chequeo_interno()

        if (self.__en_marcha and chequeo) == True:
            return "El coche está en marcha"

        elif(self.__en_marcha == True and chequeo == False):
            return "algo ha ido mal en el chequeo"

        else:
            return "El coche esta en pana"


    def estado(self):
        print("el coche tiene", self.__ruedas, "ruedas")
        print("el coche tiene un ancho de", self.__anchoChasis)
        print("el coche tiene un largo de", self.__largoChasis)



    def __chequeo_interno(self): #Metodo encapsulado
        print("realizando chequeo interno")

        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas":
            return True
        else:
            return False
     



miCoche = Coche() #INSTANCIAR LA CLASE, SE CREA UN OBJ
print(miCoche.arrancar(True))
miCoche.estado()

print("------------------------------------------------")

miCoche_2 = Coche() #INSTANCIA SECUNDO OBJETO
print(miCoche_2.arrancar(False))
miCoche_2.estado()

