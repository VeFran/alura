from os import system  
system ("cls")

import sqlite3

conexion = sqlite3.connect("basededatos.db")
cursor= conexion.execute("select from * articulos")
for fila in cursor:
    print(fila)
conexion.close()