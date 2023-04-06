'''
Desafío 10:   CORREGIR BUSCAR BIEN EL ERROR
Cargar un conjunto de notas utilizando una lista
Mostrar las notas cargadas en la lista.
Si se ingresa la nota cero sale.'''
from os import system
system("cls")

miLista=[]
nota=int(input("Ingrese una nota. Si ingresa sale del programa "))

for nota in range(0,5): #puede ser una variante usar list try except no puedo introd letras y float por los promedios de notas
    miLista.append(nota)
    nota=int(input("Ingrese una nota. Si ingresa  sale del programa "))
    print("Las notas ingresadas son: ", miLista)


