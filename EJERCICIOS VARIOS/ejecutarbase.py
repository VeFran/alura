from os import system  
system ("cls")

import sqlite3

conexion=sqlite3.connect("basededatos.db")
conexion.execute("insert into articulos(descripcion, precio) values (?,?)", ('uvas', 15.75))
conexion.execute("insert into articulos(descripcion, precio) values (?,?)", ('mango', 10.75))
conexion.execute("insert into articulos(descripcion, precio) values (?,?)", ('durazno', 12.75))
conexion.commit()
conexion.close()