from os import system
system ("cls")

def doblarNumero(nro):
 print(nro*2)
 
doblarNumero(4)

def mostrarNumero(num1,num2):

    return num1, num2

print (mostrarNumero(5,10))


def saludar(nombre, profesion):
 print(f"Hola {nombre}, tu profesion es {profesion}")
 
 
saludar(nombre="Ingrid", profesion="Estudiante")
saludar( profesion="Estudiante", nombre="Ingrid")
# saludar( profesion="Estudiante","Ingrid")