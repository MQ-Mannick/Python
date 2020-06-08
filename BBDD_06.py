import sqlite3

conn = sqlite3.connect("GestionProductos") 

cursor = conn.cursor() 

cursor.execute("SELECT * FROM productos WHERE cat_articulo = 'musica'")

#SACAR LOS VALORES DE LA BASE DE DATOS
# productos = cursor.fetchall()
# print(productos)

#ACTUALIZAR LOS VALORES DE LOS PRODUCTOS
#cursor.execute("UPDATE productos SET precio_articulo = 120 WHERE nombre_articulo = 'pelota'")

#BORRAR REGISTROS
cursor.execute("DELETE FROM productos WHERE ID = 4")


conn.commit()

cursor.close() #cerrando el puntero
conn.close() #cerrando con la base de datos