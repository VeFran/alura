import sqlite3
import tkinter as tk
from tkinter import Frame, ttk, messagebox
from time import localtime, asctime


def main():
  ventana = tk.Tk()
  ventana.title("Ejercicio Integrador")
  ventana.iconbitmap('img\cp-logo.ico')
  ventana.resizable(0,0)   # aqui decimos que no se pueda modificar el tamaño de la ventana
  
  
  ventana.mainloop()
  
if __name__ == '_main_':
   main()
  
