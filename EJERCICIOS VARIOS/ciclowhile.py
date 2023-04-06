import os
os.system ("cls")

#Ciclo While para sacar la licencia e conducir desde 16, con autorizacion

import math    #importamos una clase o funcion

nombre = input ("Ingrese su Nombre: ")
edad = int(input ("Ingrese su edad: "))
if edad < 16:
  print ("Ud no puede sacar su licencia de conducir")
else:
    while edad>= 16:
      if 18 >= edad and edad< 18:
          print ("Usted puede sacar su licencia de conducir con autorizacion de sus padres")
      
      elif 18 <= edad < 95:
          print ("Usted puede sacar su licencia de conducir")
          break;
    #nombre = input ("Ingrese su nombre")
    #edad = int(input ("Ingrese su edad: ")) 

print("La edad del aspirante es: " +str(edad))

