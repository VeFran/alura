from os import system
system ("cls")
import tkinter as tk


## invocar metodos -> tk.funcion()

#Creacion de una ventana:
ventana = tk.Tk() #Creacion de una ventana, forma de representacion de los programas
ventana.title("Cajero Virtual Automatico") #Titulo de la Ventana
ventana.geometry("400x300") #otra forma de geometria
ventana.config(width=400, height=400) #ancho y alto

etiqueta = tk.Label(text = "Soy una etiqueta")
etiqueta.place(x=10, y=10)
boton = tk.Button(text="Resultado", bg="gray", fg="red", command=ventana.iconify)
boton.place(x=10, y=50)
boton.pack()

etiqueta.pack()

ventana.mainloop() #Metodo para mantener la ventana en funcionamiento se debe utilizar al finalizar la edicion de la ventana
