from os import system
system ("cls")

def sumatoria (a,b):  #recibe parametros del usuario
   c= a +b
   return c
a= int(input("Ingrese el Primer Número: "))
b= int(input("Ingrese el Segundo Número: "))
x= sumatoria(a,b)
print(f"El Valor de la Suma es: {x}")

