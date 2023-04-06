import sqlite3

class ConexionDB:    # creacion de constructor
    def __init__(self):
        self.base_datos= 'EJERCICIO INTEGRADOR\ejercicio-integrador\database\peliculas.db'  #la ruta debe ser no muy extensa
        self.conexion= sqlite3.connect(self.base_datos)
        self.cursor=self.conexion.cursor()
        
        
    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()
   
    

    
        
            
        
