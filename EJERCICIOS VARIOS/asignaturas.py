# Salarios Jefes y empleados
import os
os.system ("cls")
print("Asignaturas para la inscripcion Año 2023")
print("Asignaturas Optativas: Informatica Grafica - Pruebas de Software - Networking - Usabilidad y Accesabilidad")
opcionElegida= input ("Escribe la asignatura optativa elegida: ")
asignatura= opcionElegida.lower()
if asignatura in ("informatica grafica" , "pruebas de software" , "networking" , "usabilidad y accesabilidad"):
    print("Asignatura Optatitva elegida: ",asignatura)
else:
    print("La asignatura elegida no está contemplada en la lista")    