import sqlite3

conn = sqlite3.connect("GestionProductos") 

cursor = conn.cursor() 

cursor.execute('''

    CREATE TABLE productos (

        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_articulo VARCHAR(50), 
        precio_articulo INTEGER(50),
        cat_articulo VARCHAR(20)

    )

''')

productos = [

    ("pelota", 100, "jugueteria"),
    ("pantalon", 500, "prendas"),
    ("microfono", 450, "musica"),
    ("guitarra", 230, "musica")

]

cursor.executemany('INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)', productos) #se inserta la lista con las llaves primarias 

conn.commit()

cursor.close() #cerrando el puntero
conn.close() #cerrando con la base de datos