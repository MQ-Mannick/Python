from tkinter import *

root = Tk()

opcion = IntVar() #declaramos una variable que almacenara valores de tipo entero

def imprimir():
    print(opcion.get()) #funcion que rescata el valor del radio elegido y lo imprime
    if opcion.get() == 1:
        etiqueta.config(text = "Tu genero es masculino") #imprime en el label final lo elegido
    elif opcion.get() == 2:
        etiqueta.config(text = "Tu genero es femenino") #imprime en el label final lo elegido
    else: 
        etiqueta.config(text = "Tu genero es Otro")

Label(root, text = "Genero: ").pack() #solo es un texto para indicar la eleccion

Radiobutton(root, text = "Masculino", variable = opcion, value = 1, command = imprimir).pack() #creamos un boton de radio y lo empaquetamos, despues si los pulsamos la variable es reemplazada por el valor del radio.
Radiobutton(root, text = "Femenino", variable = opcion, value = 2, command = imprimir).pack() #command permite que la funcion rescate el valor
Radiobutton(root, text = "Otro", variable = opcion, value = 3, command = imprimir).pack() 

etiqueta = Label(root) #etiqueta donde se escribiran los valores de la funcion

etiqueta.pack()
root.mainloop()