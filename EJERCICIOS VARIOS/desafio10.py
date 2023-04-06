'''
Desafío 10:
Cargar un conjunto de notas utilizando una lista
Mostrar las notas cargadas en la lista.
Si se ingresa la nota cero sale.'''
from os import system
system("cls")

miLista=[]
numero=int(input("Ingrese una nota. Si ingresa cero(0) sale del programa"))
while numero !=0:
    miLista.append(numero)
    numero=int(input("Ingrese una nota. Si ingresa cero(0) sale del programa"))
print("Las notas ingresadas son: ")
print(miLista)