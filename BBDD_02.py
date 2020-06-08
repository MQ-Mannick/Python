import sqlite3

miConexion = sqlite3.connect("PyFirst") #creando la base de datos / conectando con la base de datos

miCursor = miConexion.cursor() #creando el puntero para ejecutar consulta sql

variosProductos = [ #Array donde se colocan tuplas para insertar muchos valores

    ("Camiseta", 10, "Deportes"),
    ("Jarra", 30, "Greda"),
    ("Camion", 100, "Autos")

]

miCursor.executemany("INSERT INTO productos VALUES (?,?,?)", variosProductos)
#executemany permite ingresar varios
#despues de values los signos ? se colocan tantas veces como el numero de campos que contienen las tuplas
#en el segundo parametro se le entregan la lista con las tuplas dentro

miConexion.commit()

miCursor.close() #cerrando el puntero
miConexion.close() #cerrando con la base de datos