from tkinter import *

root = Tk()

my_frame = Frame(root, width = 1000, height = 1000)
my_frame.pack()

#CUADROS DE TEXTO

my_name = StringVar() #se declara my_name antes especificando que es texto

text_square_1 = Entry(my_frame, textvariable = my_name) #se asocia el valor de my_name
text_square_1.grid(row = 0, column = 1, padx = 20, pady = 20)
text_square_1.config(fg = "red", justify = "center")

text_square_2 = Entry(my_frame)
text_square_2.grid(row = 1, column = 1, padx = 20, pady = 20)
text_square_2.config(show = "*", bg = "#f1f1f1")

text_square_3 = Entry(my_frame)
text_square_3.grid(row = 2, column = 1, padx = 20, pady = 20)

text_square_4 = Entry(my_frame)
text_square_4.grid(row = 3, column = 1, padx = 20, pady = 20)

text_square_5 = Text(my_frame, width = 15, height = 7)
text_square_5.grid(row = 4, column = 1, padx = 20, pady = 20)

#AGREGANDO UN SCROLL AL AREA DEL TEXTO DEL COMENTARIO

vertical_scroll = Scrollbar(my_frame, command = text_square_5.yview) #se construye un scrollbar
vertical_scroll.grid(row = 4, column = 2, sticky = "nse") #se agrega el scrollbar con de norte a sur hacia el este
text_square_5.config(yscrollcommand = vertical_scroll.set) #agrega al cuadro un bloqueo antes de que se llene

#COLOCANDO LABELS ANTES DE LAS ENTRADAS DE TEXTO PARA INDICAR

label_1 = Label(my_frame, text = "Nombre: ")
label_1.grid(row = 0, column = 0, sticky = "e", padx = 20, pady = 20)

label_2 = Label(my_frame, text = "Password: ")
label_2.grid(row = 1, column = 0, sticky = "e", padx = 20, pady = 20)

label_3 = Label(my_frame, text = "Apellido: ")
label_3.grid(row = 2, column = 0, sticky = "e", padx = 20, pady = 20)

label_4 = Label(my_frame, text = "Direccion: ")
label_4.grid(row = 3, column = 0, sticky = "e", padx = 20, pady = 20)

label_6 = Label(my_frame, text = "Comentarios: ")
label_6.grid(row = 4, column = 0, sticky = "e", padx = 20, pady = 20)

#CREANDO BOTONES

def codigo_btn():
    my_name.set("Manuel")

btn_send = Button(root, text = "Enviar", command = codigo_btn)
btn_send.pack()

root.mainloop()
