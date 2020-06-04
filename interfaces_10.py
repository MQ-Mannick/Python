from tkinter import *
from tkinter import messagebox


root = Tk()

def infoAcercaDe():
    messagebox.showinfo("IDE de textos mann", "IDE 2020 todos los derechos reservados")
def infoStatus():
    messagebox.showwarning("Licencia", "Licencia a punto de acabar")
def avisoSalir():
    valor = messagebox.askokcancel("Salir", "¿Desea salir de la aplicacion?")
    if valor == True:
        root.destroy()
def avisoImportar():
    valor = messagebox.askretrycancel("Reintentar", "No fue posible abrir la carpeta de archivos, ¿Desea reintentar?")
    if valor == True:
        messagebox.showinfo("Exito", "Operacion realizada con exito")

#Creando la barra de menus y colocandola en el root
menu_barra = Menu(root)
root.config(menu = menu_barra, width = 500, height = 500)
#Creando los menus para la barra

#menu de archivo-contiene mas submenus
archivoMenu = Menu(menu_barra, tearoff = 0) #construimos un elemento y se le quita el primer subelemento lineal por defecto
archivoMenu.add_command(label = "Nuevo archivo") #a partir de aqui se hacen los subelementos
archivoMenu.add_command(label = "Guardar archivo")
archivoMenu.add_command(label = "Exportar")
archivoMenu.add_command(label = "Importar", command = avisoImportar)
archivoMenu.add_separator() #Agrega un separador en los submenus
archivoMenu.add_command(label = "Salir", command = avisoSalir)

archivoEdicion = Menu(menu_barra, tearoff = 0) 
archivoEdicion.add_command(label = "Copiar")
archivoEdicion.add_command(label = "Pegar")
archivoEdicion.add_separator()
archivoEdicion.add_command(label = "Cortar")
archivoEdicion.add_command(label = "Tranformar")

#menu de herramientas-no contiene nada
archivoHerramientas = Menu(menu_barra, tearoff = 0) #construimos un elemento

#menu de ayuda-contiene 4 submenus
archivoAyuda = Menu(menu_barra, tearoff = 0) #construimos un elemento
archivoAyuda.add_command(label = "Acerca de..", command = infoAcercaDe) #suelta una ventana emergente llamando a la funcion
archivoAyuda.add_command(label = "Status", command = infoStatus)
archivoAyuda.add_command(label = "Documentacion")
archivoAyuda.add_command(label = "Preferencias")

#creando los textos para que puedan aparecer
menu_barra.add_cascade(label = "Archivo", menu = archivoMenu) #la variable que declaramos que pertenece a menu_barra se le asigna un texto
menu_barra.add_cascade(label = "Edicion", menu = archivoEdicion) #la variable que declaramos que pertenece a menu_barra se le asigna un texto
menu_barra.add_cascade(label = "Herramientas", menu = archivoHerramientas) #la variable que declaramos que pertenece a menu_barra se le asigna un texto
menu_barra.add_cascade(label = "Ayuda", menu = archivoAyuda) #la variable que declaramos que pertenece a menu_barra se le asigna un texto


root.mainloop()