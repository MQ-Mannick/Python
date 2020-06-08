import sqlite3

conn = sqlite3.connect("GestionProductos") 

cursor = conn.cursor() 

cursor.execute('''

    CREATE TABLE productos (

        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_articulo VARCHAR(50) UNIQUE,
        precio_articulo INTEGER(50),
        cat_articulo VARCHAR(20)

    )

''') #unique impide que se repita la informacion, es decir, no puede existir dos con el mismo nombre

productos = [

    ("pelota", 100, "jugueteria"),
    ("pantalon", 500, "prendas"),
    ("microfono", 450, "musica"),
    ("guitarra", 230, "musica"),
    #("pantalon", 500, "prendas") da error porque no se puede repetir 

]

cursor.executemany('INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)', productos) #se inserta la lista con las llaves primarias 

conn.commit()

cursor.close() #cerrando el puntero
conn.close() #cerrando con la base de datos