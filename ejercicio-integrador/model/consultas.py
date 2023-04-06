from model.conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla():       #realiza conexion con DB
      conexion = ConexionDB()
    
      sql ="""CREATE TABLE if not exists turnos (id_turno INTEGER primary Key AUTOINCREMENT,
            servicio TEXT, dia TEXT, horario DATE)"""
    
      try:     
         conexion.cursor.execute(sql)
         conexion.cerrar()
         titulo='Crear Registro'
         mensaje= 'Se creo la tabla en la Bases detos'
         messagebox.showinfo(titulo, mensaje)
      except:     
         titulo='Crear Registro'
         mensaje= 'La tabla ya esta creada'
         messagebox.showwarning(titulo, mensaje)
       
       
       
       
def borrar_tabla():
    conexion = ConexionDB()
    
    sql= "DROP TABLE turnos"    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Borrar Registro'
        mensaje= 'La tabla de la Base de datos se borro con éxito' 
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Borrar Registro'
        mensaje = 'No hay tabla para borrar '
        messagebox.showerror(titulo, mensaje)
 
        
class Turno:  # constructor de obj igual a la tabla que tenemos en la DB
    def __init__ (self, servicio, dia, horario):
       self.id_turno= None  #algo vacío o nulo
       self.servicio= servicio
       self.dia= dia
       self.horario= horario       
    
    def __str__ (self):  #vamos a retornar inf formateada
        return f'Turno[{self.servicio}, {self.dia}, {self.horario}]'
    
    
def guardar(turno):
    conexion = ConexionDB()
    
    sql= ("INSERT INTO turnos (servicio, dia, horario) values (?,?,?)", ('servicio','dia', 'horario'))
    
    try:
        conexion.cursor.execute(sql) 
        conexion.cerrar()
    except:
        titulo= 'Conexion al Registro'
        mensaje='La tabla turnos no esta creada en la DB'    
        messagebox.showerror(titulo, mensaje)
        
# def listar():
#     conexion = ConexionDB
    
#     lista_turnos = []
#     sql = 'SELECT * FROM turnos'
    
#     try:
#         conexion.cursor.execute(sql)
#         lista_turnos = conexion.cursor.fetchall()
#         conexion.cerrar()
#     except:
#         titulo = 'Conexion al Registro'
#         mensaje = 'Crea la talba enla Base de Datos'
#         messagebox.showwarning(titulo, mensaje)
        
#     return listar_turnos        
            