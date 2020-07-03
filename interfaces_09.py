from tkinter import *

root = Tk()

#Creando la barra de menus y colocandola en el root
menu_barra = Menu(root)
root.config(menu = menu_barra, width = 500, height = 500)
#Creando los menus para la barra
archivoMenu = Menu(menu_barra, tearoff = 0) #construimos un elemento y se le quita el primer subelemento lineal por defecto
archivoMenu.add_command(label = "Nuevo archivo") #a partir de aqui se hacen los subelementos
archivoMenu.add_command(label = "Guardar archivo")
archivoMenu.add_command(label = "Exportar")
archivoMenu.add_command(label = "Importar")
archivoMenu.add_separator() #Agrega un separador en los submenus
archivoMenu.add_command(label = "Cerrar")

archivoEdicion = Menu(menu_barra, tearoff = 0) 
archivoEdicion.add_command(label = "Copiar")
archivoEdicion.add_command(label = "Pegar")
archivoEdicion.add_separator()
archivoEdicion.add_command(label = "Cortar")
archivoEdicion.add_command(label = "Tranformar")


archivoHerramientas = Menu(menu_barra, tearoff = 0) #construimos un elemento

archivoAyuda = Menu(menu_barra, tearoff = 0) #construimos un elemento
archivoAyuda.add_command(label = "Acerca de..")
archivoAyuda.add_command(label = "Status")
archivoAyuda.add_command(label = "Documentacion")
archivoAyuda.add_command(label = "Preferencias")

#creando los textos para que puedan aparecer
menu_barra.add_cascade(label = "Archivo", menu = archivoMenu) #la variable que declaramos que pertenece a menu_barra se le asigna un texto
menu_barra.add_cascade(label = "Edicion", menu = archivoEdicion) #la variable que declaramos que pertenece a menu_barra se le asigna un texto
menu_barra.add_cascade(label = "Herramientas", menu = archivoHerramientas) #la variable que declaramos que pertenece a menu_barra se le asigna un texto
menu_barra.add_cascade(label = "Ayuda", menu = archivoAyuda) #la variable que declaramos que pertenece a menu_barra se le asigna un texto

root.mainloop()