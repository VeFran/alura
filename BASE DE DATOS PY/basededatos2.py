from os import system  
system ("cls")

import sqlite3

conexion = sqlite3.connect("basededatos2.db")  #Se crea una base de datos
conexion.execute("create table if not exists articulos(Código integer primary key AUTOINCREMENT, descripcion text, precio real)")
# conexion.execute("CREATE TABLE IF NOT EXISTS Usuarios(nombre TEXT, edad INTEGER, email TEXT")


conexion=sqlite3.connect("basededatos2.db")
conexion.execute("insert into articulos(descripcion, precio) values (?,?)", ('vasos', 15.75))
conexion.execute("insert into articulos(descripcion, precio) values (?,?)", ('platos', 10.75))
conexion.execute("insert into articulos(descripcion, precio) values (?,?)", ('cubiertos', 12.75))
conexion.commit()

conexion = sqlite3.connect("basededatos2.db")
cursor= conexion.execute("select from * articulos")
for fila in cursor:
    print(fila)
    
conexion.close()
