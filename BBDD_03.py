import sqlite3

conn = sqlite3.connect("GestionProductos") 

cursor = conn.cursor() 

cursor.execute('''

    CREATE TABLE productos (

        id_articulo VARCHAR(4) PRIMARY KEY,
        nombre_articulo VARCHAR(50), 
        precio_articulo INTEGER(50),
        cat_articulo VARCHAR(20)

    )

''')

productos = [

    ("AR01", "pelota", 100, "jugueteria"),
    ("AR02", "pantalon", 500, "prendas"),
    ("AR03", "microfono", 450, "musica"),
    ("AR04", "guitarra", 230, "musica")

]

cursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos) #se inserta la lista con las llaves primarias 

conn.commit()

cursor.close() #cerrando el puntero
conn.close() #cerrando con la base de datos