from tkinter import *

root = Tk()

opcion_a = IntVar()
opcion_b = IntVar() #Variables de entorno que corresponderan a la opcion
opcion_c = IntVar()

def opciones():
    opcion_escogida = ""

    if(opcion_a.get() == 1):
        opcion_escogida = opcion_escogida + " Opcion A"
    if(opcion_b.get() == 1):
        opcion_escogida = opcion_escogida + " Opcion B"
    if(opcion_c.get() == 1):
        opcion_escogida = opcion_escogida + " Opcion C"
    texto_final.config(text = opcion_escogida)
    

frame = Frame(root) #Un frame para el root que va a contener algo
frame.pack()

Label(frame, text = "Elige una opcion o varias", width = 100).pack()


Checkbutton(frame, text = "A", variable = opcion_a, onvalue = 1, offvalue = 0, command = opciones).pack() #a diferencia del radio permite seleccionar y deseleccionar
Checkbutton(frame, text = "B", variable = opcion_b, onvalue = 1, offvalue = 0, command = opciones).pack() #variable asocia la variable global al checkbox
Checkbutton(frame, text = "C", variable = opcion_c, onvalue = 1, offvalue = 0, command = opciones).pack() #onvalue determina el valor que tendra cuando este presionado y offvalue cuando no esta seleccionado

texto_final = Label(frame) #aqui es donde se mostrara el resultado de la funcion
texto_final.pack()

root.mainloop()