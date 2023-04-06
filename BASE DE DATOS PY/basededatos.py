from os import system  
system ("cls")

import sqlite3
conexion = sqlite3.connect("basededatos.db")  #Se crea una base de datos
conexion.execute("create table if not exists articulos(Código integer primary key AUTOINCREMENT, descripcion text, precio real)")
# conexion.execute("CREATE TABLE IF NOT EXISTS Usuarios(nombre TEXT, edad INTEGER, email TEXT")
conexion.close()

