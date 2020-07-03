from tkinter import *

root = Tk()



my_frame = Frame(root)
my_frame.pack()

text_square_1 = Entry(my_frame)
text_square_1.grid(row = 0, column = 1, padx = 20, pady = 20)
text_square_1.config(fg = "red", justify = "center")

text_square_2 = Entry(my_frame)
text_square_2.grid(row = 1, column = 1, padx = 20, pady = 20)

text_square_3 = Entry(my_frame)
text_square_3.grid(row = 2, column = 1, padx = 20, pady = 20)
text_square_3.config(show = "*", bg = "#f1f1f1")

label_1 = Label(my_frame, text = "Nombre: ")
label_1.grid(row = 0, column = 0, sticky = "e", padx = 20, pady = 20)

label_2 = Label(my_frame, text = "Apellido: ")
label_2.grid(row = 1, column = 0, sticky = "e", padx = 20, pady = 20)

label_3 = Label(my_frame, text = "Password: ")
label_3.grid(row = 2, column = 0, sticky = "e", padx = 20, pady = 20)

root.mainloop()

