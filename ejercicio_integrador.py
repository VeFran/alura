import tkinter as tk
from client.gui_app import Frame, barra_menu
from PIL import ImageTk, Image                #libreria para trabajar con imagenes

def main():
 ventana = tk.Tk()
 ventana.title("TURNOS ESTETICA")
 ventana.iconbitmap('EJERCICIO INTEGRADOR\ejercicio-integrador\img\logo.ico')
 
 ventana.resizable(1,1)   # aqui decimos que  se pueda modificar el tamaño de la ventana
 barra_menu(ventana)

 app = Frame(ventana = ventana)
 app.mainloop()  
  var
    
if __name__ == '__main__':
   main()