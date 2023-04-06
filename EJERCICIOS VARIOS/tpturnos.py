from os import system
system ("cls")
import tkinter as tk
## invocar metodos -> tk.funcion()

#Creacion de una ventana:
ventana = tk.Tk() #Creacion de una ventana, forma de representacion de los programas
ventana.title("Gestion de Turnos") #Titulo de la Ventana
ventana.geometry("500x300") #otra forma de geometria
ventana.config(width=500, height=400) #ancho y alto

etiqueta = tk.Label(text = "GESTION DE TURNOS")
etiqueta.place(x=80, y=50)
etiqueta.pack()

boton = tk.Button(text="Resultado", bg="pink", fg="black", command=ventana.iconify)
boton.place(x=10, y= 100)
boton.pack()

boton = tk.Button(text="Resultado", bg="pink", fg="black", command=ventana.iconify)
boton.place(x=10, y= 100)
boton.pack()


ventana.mainloop() #Metodo para mantener la ventana en funcionamiento se debe utilizar al finalizar la edicion de la ventana
