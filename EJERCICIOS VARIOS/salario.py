# Salarios Jefes y empleados
import os
os.system ("cls")
SalarioDirector = int (input ("Ingrese el salario del Director:"))
print ("El salario del Director es: ", SalarioDirector)
SalarioGerente = int (input ("Ingrese el salario del Gerente:"))
print ("El salario del Gerente es: ", SalarioGerente)
SalarioJefeArea = int (input ("Ingrese el salario del Jefe de Area:"))
print ("El salario del Jefe de Area es: ", SalarioJefeArea)
SalarioEncargado = int (input ("Ingrese el salario del Encargado:"))
print ("El salario del Encargado es: ", SalarioEncargado)
if SalarioDirector >SalarioGerente > SalarioJefeArea >SalarioEncargado:
   print ("Todo funciona bien en la empresa :)")
else:
    print ("Hay algo mal en la empresa :(")
