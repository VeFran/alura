''
#Desafío 10:
# Cargar un conjunto de notas utilizando una lista
# Mostrar las notas cargadas en la lista.
# Si se ingresa la nota cero sale.'''

from os import system
system("cls")

miLista=[]
n= int(input("Cuantas notas desea ingresar?: "))
if n!=0:
  for nota in range(n):
    nota = int (input("Ingrese una nota: "))
    if (nota > 0):
      miLista.append(nota)
    elif (nota== 0):
      nota = int(input("Ingrese nuevamente una nota: "))  
      miLista.append(nota)
    else: print ("Ha ingresado una nota invalida") 
  promedio = sum(miLista)/n              
      
  print("Las notas ingresadas son: ", miLista)
  print("El promedio de las notas es: ", promedio)
else: print ("Salir de la consulta")       
    
