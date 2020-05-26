from tkinter import *

root = Tk()

miFrame = Frame(root, width = 1000, height = 1000)
miFrame.pack()
miFrame.config(bg = "#E9C35F")

miImagen = PhotoImage(file = "Rammstein.png")


Label(miFrame, image = miImagen).place(x = 300, y = 300)
Label(miFrame, text = "Hola ._.XD", fg = "#D61021", font = ("Papyrus", 20)).place(x = 100, y = 200)

root.mainloop()

