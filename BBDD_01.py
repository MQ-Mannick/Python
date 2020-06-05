import sqlite3

miConexion = sqlite3.connect("PyFirst") #creando la base de datos / conectando con la base de datos

miCursor = miConexion.cursor() #creando el puntero para ejecutar consulta sql

#miCursor.execute("CREATE TABLE productos (nombre_articulo VARCHAR(50), precio INTEGER, seccion VARCHAR(20))") #query de tipo create para una tabla

miCursor.execute("INSERT INTO productos VALUES('microfono', '20000', 'musica')")
miConexion.commit()

miCursor.close() #cerrando el puntero
miConexion.close() #cerrando con la base de datos