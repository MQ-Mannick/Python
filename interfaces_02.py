from tkinter import *

raiz = Tk()

raiz.title("Ventana numeros 2")
raiz.resizable(True, True)
raiz.iconbitmap("favicon.ico")
raiz.config(bg = "Black")

#AGREGANDO EL FRAME PARA LA VENTANA

miFrame = Frame()
miFrame.pack()

#-----------side posiciona el frame y anchor dirige hacia donde se pega. EJ: right n = esquina superior derecha------------
#miFrame.pack(side = "right", anchor = "n") 

#----------fill hace responsive al frame en la direccion que se le indique y expand lo verifica-------------
#miFrame.pack(fill = "both", expand = "True")

#-------------Asignando altura, anchura y color al frame-----------------------
miFrame.config(bg = "White")
miFrame.config(width = "1000", height = "1000")

#----------Cambiando el borde de la ventana-------------
miFrame.config(bd = 20)
miFrame.config(relief = "groove")

#-------------Cambiando el cursor al hover frame---------------------
miFrame.config(cursor = "hand2")


raiz.mainloop()