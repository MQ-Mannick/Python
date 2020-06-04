from tkinter import *
from tkinter import filedialog

root = Tk()

def abreFichero():
    fichero = filedialog.askopenfilename(title = "Abrir", initialdir = "C:", filetypes = (("Ficheros de word", "*.docx"), ("Ficheros de texto", "*.txt"), ("Todos los archivos", "*.*"))) 
        #"filedialog.askopenfilename" devuelve la ruta, por lo que se le asigna una variable
        #"initialdir" indica la ruta donde se abrira
        #"filetypes" nos pide que le demos una TUPLA(recordar que una tupla es una lista estatica) con al menos dos parametros, cada uno 
        # con el titulo de la eleccion seguido de la extension del tipo de archivos que queremos abrir
    print(fichero)

Button(root, text = "Abir fichero", command = abreFichero).pack()

root.mainloop()