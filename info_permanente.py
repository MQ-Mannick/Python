import pickle

class Persona:

    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Se ha creado una nueva persona con el nombre de ", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:

    personas=[]

    def __init__(self):
        lista_personas_externo = open("fichero_personas", "ab+")
        lista_personas_externo.seek(0)
        try:
            self.personas = pickle.load(lista_personas_externo)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("El fichero esta vacío")
        finally:
            lista_personas_externo.close()
            del(lista_personas_externo)

    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonas_en_ficheroExterno()

    def mostrarPersonas(self):
        for i in self.personas:
            print(i)
    
    def guardarPersonas_en_ficheroExterno(self):
        lista_personas_externo = open("fichero_personas", "wb")
        pickle.dump(self.personas, lista_personas_externo)
        lista_personas_externo.close()
        del(lista_personas_externo)
    
    def mostrarPersonas_de_ficheroExterno(self):
        print("La info del fichero externo es la siguiente: ")
        for i in self.personas:
            print(i)
        

        
lista_1 = ListaPersonas()
Pedro = Persona("Pedro", "Masculino", 50)
lista_1.agregarPersonas(Pedro) 
lista_1.mostrarPersonas_de_ficheroExterno()



