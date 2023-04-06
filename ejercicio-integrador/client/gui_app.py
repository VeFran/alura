import tkinter as tk
from tkinter import ttk            #vamos a utilizar para armar tablas
from model.consultas import crear_tabla, borrar_tabla
from model.consultas import Turno, guardar



def barra_menu(ventana):
  barra_menu = tk.Menu(ventana)
  ventana.config(menu= barra_menu, width= 300, height= 300)
  
  menu_inicio = tk.Menu(barra_menu, tearoff = 0)
  barra_menu.add_cascade(label ='Inicio', menu= menu_inicio)
  
  
  menu_inicio.add_command(label='Registrar Turno', command = crear_tabla)
  menu_inicio.add_command(label='Eliminar Turno', command = borrar_tabla)
  menu_inicio.add_command(label='Salir', command = ventana.destroy)
   
  barra_menu.add_cascade(label ='Consultas')
  barra_menu.add_cascade(label ='Configuracion')  
  barra_menu.add_cascade(label ='Ayuda')
  
class Frame(tk.Frame):                 #va a heredear de la clase frame
  def __init__ (self, ventana= None):     #defino el Constructor
   
    super().__init__(ventana, width=480,height= 320,)
    
    
    
    self.ventana = ventana            
    self.pack()                     #empaqueto de manera directa, porque estamos aplicando la herencia
    self.config(bg= 'pink')
    
    self.campos_turnos()
    self.deshabilitar_campos()
    self.tabla_turnos()
      
    
  def campos_turnos(self):
    #label de cada campo
    self.label_servicio = tk.Label(self, text ='Servicio:')    
    self.label_servicio.config(font =('Arial',12, 'bold'))
    self.label_servicio.grid(row=0, column=0,padx= 10, pady= 10)  #estamos posicicionando el obj label en la grilla
    
    self.label_dia = tk.Label(self, text ='Dia:')    
    self.label_dia.config(font =('Arial',12, 'bold'))
    self.label_dia.grid(row=1, column=0, padx= 10, pady= 10)  #estamos posicicionando el obj label en la grilla  
     
    self.label_horario = tk.Label(self, text ='Horario:')    
    self.label_horario.config(font =('Arial',12, 'bold'))
    self.label_horario.grid(row=2, column=0, padx= 10, pady= 10)  #estamos posicicionando el obj label en la grilla  
    
         
    #Entrys de cada campo
    
    self.mi_servicio = tk.StringVar()
    self.entry_servicio = tk.Entry(self, textvariable=self.mi_servicio)
    self.entry_servicio.config(width=50, font=('Arial',12))
    self.entry_servicio.grid(row= 0, column= 1, padx=10, pady=10, columnspan=2)
    
    self.mi_dia = tk.StringVar()
    self.entry_dia = tk.Entry(self, textvariable=self.mi_dia )
    self.entry_dia.config(width=50, font=('Arial',12))
    self.entry_dia.grid(row= 1, column= 1, padx=10, pady=10,columnspan=2)
    
    self.mi_horario = tk.StringVar()
    self.entry_horario = tk.Entry(self, textvariable=self.mi_horario)
    self.entry_horario.config(width=50, font=('Arial',12))
    self.entry_horario.grid(row= 2, column= 1, padx=10, pady=10, columnspan=2)
    
    #botones
    
    self.boton_nuevo = tk.Button(self, text ="Nuevo", command= self.habilitar_campos)
    self.boton_nuevo.config(width = 20, font=('Arial',12, 'bold'), fg='white', bg='grey', cursor = 'hand2', activebackground ='magenta')
    self.boton_nuevo.grid(row=3, column=0, padx=10, pady=10)
    
    self.boton_guardar = tk.Button(self, text ="Guardar", command= self.guardar_datos)
    self.boton_guardar.config(width = 20, font=('Arial',12, 'bold'), fg='white', bg='grey', cursor = 'hand2', activebackground ='magenta')
    self.boton_guardar.grid(row=3, column=1, padx=10, pady=10)
    
    self.boton_cancelar = tk.Button(self, text ="Cancelar",command= self.deshabilitar_campos)
    self.boton_cancelar.config(width = 20, font=('Arial',12, 'bold'), fg='white', bg='grey', cursor = 'hand2', activebackground ='magenta')
    self.boton_cancelar.grid(row=3, column=2, padx=10, pady=10)
    
    
     
  def habilitar_campos(self):
    self.mi_servicio.set(' ')         #aqui limpio el entry de datos
    self.mi_dia.set(' ')
    self.mi_horario.set(' ')
    
    self.entry_servicio.config(state='normal')   
    self.entry_dia.config(state='normal')
    self.entry_horario.config(state='normal')
    
    self.boton_guardar.config(state='normal')
    self.boton_cancelar.config(state='normal')
  
  def deshabilitar_campos(self):
    self.mi_servicio.set(' ')         #aqui limpio el entry de datos
    self.mi_dia.set(' ')
    self.mi_horario.set(' ')
    
    self.entry_servicio.config(state='disabled')   
    self.entry_dia.config(state='disabled')
    self.entry_horario.config(state='disabled')
    
    self.boton_guardar.config(state='disabled')
    self.boton_cancelar.config(state='disabled')
  
  def guardar_datos(self):
    
    turno= Turno(
      self.mi_servicio.get(),
      self.mi_dia.get(),
      self.mi_horario.get(),
    )
    guardar(turno)   #aqui va realizar la insersion a la BD
    self.deshabilitar_campos()
    
  def tabla_turnos(self):
    #self.lista_turnos = listar()
    
    self.tabla= ttk.Treeview(self, column =('Servicio', 'Dia', 'Horario'))   
    self.tabla.grid(row= 4, column= 0, columnspan= 4)
    
    self.tabla.heading('#0', text= 'ID')    
    self.tabla.heading('#1', text= 'SERVICIO') 
    self.tabla.heading('#2', text= 'DIA')
    self.tabla.heading('#3', text= 'HORARIO')  
    
    
    
    #iterar la lista de peliculas
    # for p in self.lista_turnos:
      
    #   self.tabla.insert('', 0, text= p[0] , values = (p[1], p[2], p[3]))
   
    #Boton de Editar  que  se encuentra en el area de la tabla generada
    self.boton_editar = tk.Button(self, text ="Editar")
    self.boton_editar.config(width = 20, font=('Arial',12, 'bold'), fg='white', bg='grey', cursor = 'hand2', activebackground ='magenta')
    self.boton_editar.grid(row=5, column=0, padx=10, pady=10)   
  
    #Boton de Eliminar
    self.boton_eliminar = tk.Button(self, text ="Eliminar")
    self.boton_eliminar.config(width = 20, font=('Arial',12, 'bold'), fg='white', bg='grey', cursor = 'hand2', activebackground ='magenta')
    self.boton_eliminar.grid(row=5, column=1, padx=10, pady=10) 
    
    
  
     
   