import os
os.system ("cls")
#Calculo raiz cuadrada
import math

print("Programa de Cálculo de raíz cuadrada")
numero = int(input("Introduce un numero por favor: "))
intentos = 0
while numero < 0:
    print("No se puede hallar la raiz de un nro negativo")
    print("")
    print("Ingrese numero positivo")
    print("Tiene tres Intentos")
    if intentos == 2:
      print("Has consumido demasiados intentos. El programa ha finalizado")
      break
    numero = int(input("Introduce un número por favor:  "))
    if numero <0:
       intentos= intentos+1 
if intentos < 2:
   solucion = math.sqrt(numero)
   print("La raíz cuadra de " +str(numero)+ "  es: " +str(solucion))       