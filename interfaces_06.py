from tkinter import *

raiz = Tk()

#-------------------FRAME---------------------------------------------
miFrame = Frame(raiz)
miFrame.pack()
#---------------VARIABLE GLOBAL OPERACION/resultado--------------------
operacion = ""
resultado = 0
#------------------PANTALLA--------------------------------------------
numeroPantalla = StringVar()
pantalla = Entry(miFrame, textvariable = numeroPantalla)
pantalla.grid(row = 1, column = 1, padx = 10, pady = 10, columnspan = 4)
pantalla.config(background = "black", fg = "#03f943", justify = "right")

#----------------Pulsaciones del teclado------------------------

def numero_pulsado(num):
    global operacion
    if operacion != "": #lo sobreescribe si es diferente de cadena vacia
        numeroPantalla.set(num)
        operacion = "" #decirle que es cadena vacia para que no siga sobreescribiendo y pase al if
    else: #si no es diferente de cadeana vacia entonces lo agrega
        numeroPantalla.set(numeroPantalla.get() + num)

def suma(num):
    global operacion
    global resultado
    resultado = resultado + int(num)
    operacion = "suma"
    numeroPantalla.set(resultado)

def igual():
    global resultado
    numeroPantalla.set(resultado + int(numeroPantalla.get()))
    resultado = 0

#--------------BOTONES-----------------------------------------------
#------------fila-1------------------
btn_7 = Button(miFrame, text = "7", width = 3, command = lambda:numero_pulsado("7"))
btn_7.grid(row = 2, column = 1)

btn_8 = Button(miFrame, text = "8", width = 3, command = lambda:numero_pulsado("8"))
btn_8.grid(row = 2, column = 2)

btn_9 = Button(miFrame, text = "9", width = 3, command = lambda:numero_pulsado("9"))
btn_9.grid(row = 2, column = 3)

btn_div = Button(miFrame, text = "/", width = 3)
btn_div.grid(row = 2, column = 4)
#------------fila-2------------------
btn_4 = Button(miFrame, text = "4", width = 3, command = lambda:numero_pulsado("4"))
btn_4.grid(row = 3, column = 1)

btn_5 = Button(miFrame, text = "5", width = 3, command = lambda:numero_pulsado("5"))
btn_5.grid(row = 3, column = 2)

btn_6 = Button(miFrame, text = "6", width = 3, command = lambda:numero_pulsado("6"))
btn_6.grid(row = 3, column = 3)

btn_mul = Button(miFrame, text = "X", width = 3)
btn_mul.grid(row = 3, column = 4)
#------------fila-3------------------
btn_1 = Button(miFrame, text = "1", width = 3, command = lambda:numero_pulsado("1"))
btn_1.grid(row = 4, column = 1)

btn_2 = Button(miFrame, text = "2", width = 3, command = lambda:numero_pulsado("2"))
btn_2.grid(row = 4, column = 2)

btn_3 = Button(miFrame, text = "3", width = 3, command = lambda:numero_pulsado("3"))
btn_3.grid(row = 4, column = 3)

btn_res = Button(miFrame, text = "-", width = 3)
btn_res.grid(row = 4, column = 4)
#------------fila-4------------------
btn_0 = Button(miFrame, text = "0", width = 3, command = lambda:numero_pulsado("0")) #inicialmente que sea bloqueado y que exista un cero en pantalla
btn_0.grid(row = 5, column = 1)

btn_com = Button(miFrame, text = ".", width = 3, command = lambda:numero_pulsado(".")) #solo se puede pulsar una vez, con un cero ya puesto o con un numero
btn_com.grid(row = 5, column = 2)

btn_eq = Button(miFrame, text = "=", width = 3, command = lambda:igual())
btn_eq.grid(row = 5, column = 3)

btn_sum = Button(miFrame, text = "+", width = 3, command = lambda:suma(numeroPantalla.get()))
btn_sum.grid(row = 5, column = 4)






raiz.mainloop()